from destinations import getDestinations
from amenities import getAmenityDataByLocation
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/destinations', methods=['GET'])
def test_destinations():
  sights = getDestinations()
  return jsonify([sight.toJSON().json for sight in sights])

@app.route('/api/amenities', methods=['GET'])
def test_amenities():
  data = getAmenityDataByLocation(48.134672, 11.568834)
  return jsonify([group.toJSON().json for group in data])

if __name__ == '__main__':
  app.run(debug=True, port=8080)