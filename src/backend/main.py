from destinations import getDestinations
from amenities import getAmenityDataByLocation
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)

@app.route('/api/destinations', methods=['GET'])
def destinations():
  sights = getDestinations()
  return jsonify([sight.toJSON().json for sight in sights])

@app.route('/api/amenities', methods=['GET'])
def amenities():
  # http://127.0.0.1:8080/api/amenities?lat=48.134672&lon=11.568834
  lat = float(request.args.get('lat'))
  lon = float(request.args.get('lon'))
  radius = request.args.get('radius')
  if radius is None:
    # Default is 300 metres
    data = getAmenityDataByLocation(lat=lat,lon=lon)
  else:
    data = getAmenityDataByLocation(lat=lat,lon=lon, radius=int(radius))

  return jsonify([group.toJSON().json for group in data])

@app.route('/api/routes', methods=['POST'])
def route():
    points = request.get_json(force=True)
    points_array = [
        [point["lon"], point["lat"]]
        for point in points if point is not None
    ]

    api_key = API_KEY
    url = "https://api.openrouteservice.org/v2/directions/foot-walking/json"
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }
    payload = {"coordinates": points_array}

    response = requests.post(url, headers=headers, json=payload)
    return response.json()

if __name__ == '__main__':
 load_dotenv() 
 API_KEY=os.getenv('API_KEY')
 app.run(debug=True, port=8080)