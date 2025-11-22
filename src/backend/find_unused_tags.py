from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
from OSMPythonTools.nominatim import Nominatim
import pprint

from destinations import Destination
from flask import jsonify


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

ret = [Destination(sight) for sight in sights if 'name' in sight.tags()]

tags_set = {
'alpine_hut',    
'apartment',
'aquarium',
'artwork',
'attraction',
'camp_pitch',
'camp_site',
'caravan_site',
'chalet',
'gallery',
'guest_house',
'hostel',
'hotel',
'information',
'motel',
'museum',
'picnic_site',
'theme_park',
'trail_riding_station',
'viewpoint',
'wilderness_hut',
'zoo',
'adult_gaming_center',
'amusent_arcade',
'bandstand',
'bathing_place',
'beach_resort',
'bird_hide',
'bleachers',
'beach_resort',
'bird_hide',
'bleachers',
'bowling_alley',
'dance',
'disc_golf_course',
'dog_park',
'escape_game',
'firepit',
'fishing',
'fitness_centre',
'fitness_station',
'garden',
'golf_course',
'hackerspace',
'high_ropes_course',
'horse_riding',
'ice_rink',
'marina',
'miniature_golf',
'nature_reserve',
'outdoor_seating',
'park',
'picnic_table',
'pitch',
'playground',
'resort',
'sauna',
'slipway',
'sports_centre',
'sports_hall',
'stadium',
'summer_camp',
'sunbathing',
'swimming_area',
'swimming_pool',
'tanning_salon',
'track',
'trampoline_park',
'water_park',
'wildlife_hide'
}

tags_present = set()

for det in ret:
tags_present.add(det.tag)

print(tags_set-tags_present)

# ignored_tags = {'wildlife_hide', 'alpine_hut', 'pitch', 'wilderness_hut', 'outdoor_seating', 'chalet', 'trail_riding_station', 'high_ropes_course', 'theme_park', 'slipway', 'horse_riding', 'fitness_centre', 'picnic_table', 'amusent_arcade', 'bandstand', 'motel', 'swimming_area', 'fishing', 'miniature_golf', 'resort', 'track', 'sports_centre', 'fitness_station', 'bowling_alley', 'sports_hall', 'bird_hide', 'nature_reserve', 'camp_pitch', 'playground', 'swimming_pool', 'dog_park', 'trampoline_park', 'adult_gaming_center', 'tanning_salon', 'beach_resort', 'bathing_place', 'escape_game', 'sunbathing', 'disc_golf_course', 'water_park', 'stadium', 'park', 'garden', 'bleachers', 'sauna', 'dance', 'firepit', 'marina', 'picnic_site', 'golf_course', 'zoo', 'summer_camp', 'hackerspace', 'ice_rink'}
