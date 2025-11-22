from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
from OSMPythonTools.nominatim import Nominatim
import pprint

from flask import jsonify

class DestinationFromJson:
  name: str
  description: str
  website: str
  tag: str
  lat: float
  lon: float

  def __init__(self, jsondata):
    self.name = jsondata['name']
    self.tag = jsondata['type']
    self.lat = jsondata['lat']
    self.lon = jsondata['lon']
    self.description = ''
    self.website = ''
    
  def toJSON(self):
    return jsonify({
      'name': self.name,
      'description': self.description,
      'website': self.website,
      'tag': self.tag,
      'lat': self.lat,
      'lon': self.lon
    })

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
      'lat': float(self.lat),
      'lon': float(self.lon)
    })

def getDestinations(qstr: str = None):
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

  query2 = overpassQueryBuilder(
      elementType='node',
      area=areaId,
      selector='"leisure"',
      out='body'
  )

  explicitSearchDestinations = []
  if qstr is not None:
    query3 = nominatim.query(qstr)
    # print data found about the query:
    for x in query3:
      if 'München' in x.displayName():
        explicitSearchDestinations.append(DestinationFromJson(x.toJSON()))

  result2 = overpass.query(query2)
  leisure = result2.elements()

  return [Destination(sight) for sight in sights if 'name' in sight.tags()] + [Destination(l, tag_key='leisure') for l in leisure if 'name' in l.tags()] + explicitSearchDestinations