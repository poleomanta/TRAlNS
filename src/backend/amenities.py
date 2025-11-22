from collections import namedtuple
from dataclasses import dataclass, field
from enum import Enum
from typing import Final
from pathlib import Path
import os
import pandas as pd

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


def getAmenities(radius: int, data) -> AmenityGroup:
    # TODO generalise this
    # For now do WC as an example
    pass

def getFountainLocations() -> list[Location]:
    """Gets all fountains from file"""
    data = pd.read_csv("data/munich_opensource/trinkwasser/opendata_trinkwasserbrunnen.csv", usecols=["shape"])
    print(data)

os.chdir(Path("../../")) # Main repo
getFountainLocations()








