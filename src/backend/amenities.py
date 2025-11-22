from dataclasses import dataclass, field
from abc import abstractmethod
from enum import Enum

import osmnx as ox
from destinations import Destination
from geopandas import GeoDataFrame


# TODO this should be OSM geometry, POINT, POLYGON, etc
@dataclass
class Location:
    lat: float
    lon: float

class AmenityType(str, Enum):
    WC = "WC"
    FOUNTAIN = "FOUNTAIN"
    SPIELPLATZ = "SPIELPLATZ"
    PARK = "PARK"

""" Goal is to convey how good is the amenity status of a given type"""
class AmenityStatus(str, Enum):
    GOOD = "GOOD"
    DECENT = "DECENT"
    BAD = "BAD"
    UNKNOWN = "UNKNOWN"

@dataclass
class AmenityGroup:
    # Group all amenities of one type for a given location
    base_location: Location
    locations: list[Location] # TODO not accurate
    status: AmenityStatus = AmenityStatus.UNKNOWN

    @abstractmethod
    def getStatus(self) -> AmenityStatus:
        pass

    def __post_init__(self):
        self.status = self.getStatus()

@dataclass
class WCAmenityGroup(AmenityGroup):
    def getStatus(self) -> AmenityStatus:
        count = len(self.locations)
        print(count)

        if count >= 3:
            return AmenityStatus.GOOD
        elif count == 2:
            return AmenityStatus.DECENT
        else:
            return AmenityStatus.BAD

def getAllAmenityData(address: str, radius: int = 300):
    """ TODO
    - parameters
     """
    try:
        return ox.features.features_from_address(
            address, {'amenity': True}, dist=radius)
    except InsufficientResponseError:
        return []


def getWCData(df: GeoDataFrame, address) -> WCAmenityGroup:
    df2 = df[df['amenity'].isin(['toilets'])]

    # Status for toilets is good if there are more than 2 in 300m, decent if 1, bad if none
    locations = df2['geometry'].tolist()
    print(locations)
    return WCAmenityGroup(base_location=address, locations=locations)

    
place = "Viktualienmarkt, Munich, Germany"
df = getAllAmenityData(place)
group = getWCData(df, place)
print(group)
