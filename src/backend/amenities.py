from collections import namedtuple
from dataclasses import dataclass, field
from enum import Enum
from typing import Final
from pathlib import Path
import os
from destinations import Destination
import osmnx as ox
from geopandas import GeoDataFrame


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
    kind: AmenityType
    status: AmenityStatus
    locations: list[Location] = field(default_factory=list)

def getAllAmenityData(address: str, radius: int = 300):
    """ TODO
    - parameters?
     """
    try:
        return ox.features.features_from_address(
            address, {'amenity': True}, dist=radius)
    except InsufficientResponseError:
        return []


def getWCData(df: GeoDataFrame) -> AmenityGroup:
    # TODO exception
    df2 = df[df['amenity'].isin(['toilets'])]
    
place = "Viktualienmarkt, Munich, Germany"
df = getAllAmenityData(place)
getWCData(df)
