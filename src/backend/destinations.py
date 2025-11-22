from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
from OSMPythonTools.nominatim import Nominatim
import pprint

from flask import jsonify

class Destination:
  name: str
  description: str
  website: str
  tag: str
  lat: float
  lon: float

  def __init__(self, element, tag_key: str = 'tourism'):
    tags = element.tags() if hasattr(element, "tags") else {}
    self.name = tags.get('name')
    self.description = tags.get('description')
    self.website = tags.get('website')
    self.tag = tags.get(tag_key)
    self.lat = element.lat() if hasattr(element, "lat") else None
    self.lon = element.lon() if hasattr(element, "lon") else None

  def toJSON(self):
    return jsonify({
      'name': self.name,
      'description': self.description,
      'website': self.website,
      'tag': self.tag,
      'lat': self.lat,
      'lon': self.lon
    })

def getDestinations():
  overpass = Overpass()
  nominatim = Nominatim()

  # Get area ID for a specific place
  areaId = nominatim.query('München').areaId()

  # Build query for tourism objects within the area
  query = overpassQueryBuilder(
      elementType='node',
      area=areaId,
      selector='"tourism"',
      out='body'
  )

  result = overpass.query(query)
  sights = result.elements()

  for sight in sights:
    print(sight.tags())

  return [Destination(sight) for sight in sights if 'name' in sight.tags()]