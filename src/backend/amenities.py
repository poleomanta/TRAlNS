from dataclasses import dataclass, field
from abc import abstractmethod
from enum import Enum

import osmnx as ox

from destinations import Destination
from geopandas import GeoDataFrame
from shapely.geometry import LineString, Point, Polygon
from flask import jsonify


@dataclass
class Location:
    lat: float
    lon: float

    def toJSON(self):
        return jsonify({
        'lat': self.lat,
        'lon': self.lon,
        })

def _osmgeo_to_location(item) -> Location:
    if isinstance(item, Point):
        return Location(lat=item.x, lon=item.y)
    elif isinstance(item, Polygon):
        #TODO get a center
        first = item.exterior.coords[0]
        return Location(lat=first[0], lon=first[1])
    else:
        raise ValueError("Unknown geometry for amenity!")

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

def _get_location_df(df: GeoDataFrame) -> list[Location]:
    return [_osmgeo_to_location(item) for item in df['geometry'].tolist()]

def _getWCData(df: GeoDataFrame) -> AmenityGroup:
    df2 = df[df['amenity'].isin(['toilets'])]
    return AmenityGroup(kind=AmenityType.WC, locations=_get_location_df(df2))

def _getFountainData(df: GeoDataFrame) -> AmenityGroup:
    df2 = df[df['amenity'].isin(['water_point', 'drinking_water'])]
    return AmenityGroup(kind=AmenityType.FOUNTAIN, locations=_get_location_df(df2))

def _getRestData(df: GeoDataFrame) -> AmenityGroup:
    df2 = df[df['amenity'].isin(['bench', 'shelter', 'lounger', 'lounge'])]
    return AmenityGroup(kind=AmenityType.REST, locations=_get_location_df(df2))

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

    # TODO add more amenitiess d
    return [_getWCData(df), _getFountainData(df), _getRestData(df)]

