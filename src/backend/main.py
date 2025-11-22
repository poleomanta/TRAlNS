from destinations import getDestinations
from amenities import getAmenityDataByLocation
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/destinations', methods=['GET'])
def test_destinations():
  sights = getDestinations()
  return jsonify([sight.toJSON().json for sight in sights])

@app.route('/api/amenities', methods=['GET'])
def test_amenities():
  # http://127.0.0.1:8080/api/amenities?lat=48.134672&lon=11.568834
  lat = float(request.args.get('lat'))
  lon = float(request.args.get('lon'))
  radius = request.args.get('radius')
  if radius is None:
    # Default is 300 metres
    data = getAmenityDataByLocation(lat,lon)
  else:
    data = getAmenityDataByLocation(lat,lon, int(radius))

  return jsonify([group.toJSON().json for group in data])

if __name__ == '__main__':
  app.run(debug=True, port=8080)