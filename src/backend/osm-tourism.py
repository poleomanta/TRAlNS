from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
from OSMPythonTools.nominatim import Nominatim
import pprint

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
  tags = sight.tags()
  print('---')
  print(tags.get('name'))
  print(tags.get('tourism'))
  print(sight.lat())
  print(sight.lon())