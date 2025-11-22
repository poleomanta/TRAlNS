from dataclasses import dataclass, field
from abc import abstractmethod
from enum import Enum

import osmnx as ox

from osmnx.distance import great_circle, euclidean
from osmnx._errors import InsufficientResponseError
from destinations import Destination
from geopandas import GeoDataFrame
from shapely.geometry import LineString, Point, Polygon
from flask import jsonify


@dataclass
class Location:
    lat: float
    lon: float
    dist_from_origin: float = 0

    def toJSON(self):
        return jsonify({
        'lat': self.lat,
        'lon': self.lon,
        'dist_from_origin': self.dist_from_origin,
        })

def _osmgeo_to_location(item, origin: Location) -> Location:
    # ACHTUNG: seems like these geometry objects are (lon, lat)!!
    if isinstance(item, Point):
        lat=item.y
        lon=item.x
    elif isinstance(item, Polygon):
        #TODO get a center  
        first = item.exterior.coords[0]
        lat=first[1]
        lon=first[0]
    else:
        raise ValueError("Unknown geometry for amenity!")

    dist = great_circle(lat1=float(lat), lon1=float(lon), lat2=float(origin.lat), lon2=float(origin.lon))
    return Location(lat, lon, dist)

def _get_location_df(df: GeoDataFrame, origin: Location) -> list[Location]:
    return [_osmgeo_to_location(item, origin) for item in df['geometry'].tolist()]

class AmenityType(str, Enum):
    WC = "WC"
    FOUNTAIN = "FOUNTAIN"
    SPIELPLATZ = "SPIELPLATZ"
    PARK = "PARK"
    REST = "REST"

""" Goal is to convey how good is the amenity status of a given type"""
class AmenityStatus(str, Enum):
    GOOD = "GOOD"
    DECENT = "DECENT"
    BAD = "BAD"
    UNKNOWN = "UNKNOWN"

@dataclass
class AmenityGroup:
    # Group all amenities of one type for a given location
    kind: AmenityType
    locations: list[Location] # TODO not accurate
    status: AmenityStatus = AmenityStatus.UNKNOWN

    def __post_init__(self):
        self.status = self.getStatus()

    def getStatus(self) -> AmenityStatus:
        """Status is good if there are more than 2 in 300m, decent if 1, bad if none
        This can be implemented in subclasses if necessary
        """
        count = len(self.locations)
        if count >= 3:
            return AmenityStatus.GOOD
        elif count == 2:
            return AmenityStatus.DECENT
        else:
            return AmenityStatus.BAD

    def toJSON(self):
        return jsonify({
        'kind': self.kind,
        'status': self.status,
        'locations': self.locations,
        })

class AmenityFinder:
    def __init__(self, origin: Location, df: GeoDataFrame):
        self.origin = origin
        self.df = df

    def _getWCData(self) -> AmenityGroup:
        df2 = self.df[self.df['amenity'].isin(['toilets'])]
        return AmenityGroup(kind=AmenityType.WC, locations=_get_location_df(df2, self.origin))

    def _getFountainData(self) -> AmenityGroup:
        df2 = self.df[self.df['amenity'].isin(['water_point', 'drinking_water'])]
        return AmenityGroup(kind=AmenityType.FOUNTAIN, locations=_get_location_df(df2, self.origin))

    def _getRestData(self) -> AmenityGroup:
        df2 = self.df[self.df['amenity'].isin(['bench', 'shelter', 'lounger', 'lounge'])]
        return AmenityGroup(kind=AmenityType.REST, locations=_get_location_df(df2, self.origin))

    def getAmenityData(self) -> list[AmenityGroup]:
    # TODO add more amenitiess
    # https://wiki.openstreetmap.org/wiki/Key:amenity#Values
    # Also fix this class structure
        return [self._getWCData(), self._getFountainData(), self._getRestData()]

def getAmenityDataByLocation(lat: float, lon: float, radius: int = 300) -> list[AmenityGroup]:
    """ Get all amenities by address and distance radius
        Example: getAmenityDataByLocation(48.134672, 11.568834)
        - TODO different radius for different amenities?
     """
    try:
        df = ox.features.features_from_point(
            (lat, lon), {'amenity': True}, dist=radius)
    except InsufficientResponseError:
        return []

    finder = AmenityFinder(origin=Location(lat=lat, lon=lon), df=df)
    return finder.getAmenityData()

