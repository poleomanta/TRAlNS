from collections import namedtuple
from dataclasses import dataclass, field
from enum import Enum
from typing import Final
from pathlib import Path
import os

import osmnx as ox


# WC, trinkwasser, spielplatz, benches and parks

# Separate querying from finding logic
# Amenity types
class AmenityType(str, Enum):
    WC = "WC"
    FOUNTAIN = "FOUNTAIN"
    SPIELPLATZ = "SPIELPLATZ"
    PARK = "PARK"

# TODO consider if class with more info location specific
@dataclass
class Location:
    # By default the datasets use
    # https://en.wikipedia.org/wiki/European_Terrestrial_Reference_System_1989
    lat: float
    lon: float

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

def point_to_location(entry: str) -> Location:
    # POINT (692441.0257008562 5331488.180897921)
    print(entry)
    print(entry[6:-1].split(' '))
    (lat, lon) = entry[6:-1].split(' ')
    return Location(lat=lat, lon=lon)

def getFountainLocations() -> AmenityGroup:
    """Gets all fountains from file"""
    # Build query for desired objects within the area
    query = overpassQueryBuilder(
        elementType='node',
        area=areaId,
        selector='"amenity"',
        out='body'
    )

    result = overpass.query(query)
    wcs = result.elements()

    for wc in wcs:
        tags = wc.tags()
        print('---')
        print(tags.get('name'))
        print(tags.get('amenity'))
        print(wc.lat())
        print(wc.lon())


# get building details from address within 1000 m
place = "Viktualienmarkt, Munich, Germany"
gdf = ox.features.features_from_address(
    place, {'amenity': 'bench'}, dist=300)

# print first 5 building details
print(gdf.head(5))

