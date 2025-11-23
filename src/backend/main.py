from destinations import getDestinations
from amenities import getAmenityDataByLocation
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests
from urllib import parse

app = Flask(__name__)

@app.route('/api/destinations', methods=['GET'])
def destinations():
  if 'query' in request.args:
    qstr = request.args.get('query') or ''
    qstr = parse.unquote(qstr)
  else:
    qstr = None
  sights = getDestinations(qstr=qstr)
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

@app.route('/api/autocomplete', methods=['GET'])
def autocomplete():
    query = parse.unquote(request.args.get('query') or '')

    api_key = API_KEY
    #48.10181/11.47591
    #48.2759/11.7111
    url = "https://api.openrouteservice.org/geocode/autocomplete?text=" + parse.quote(query) + "&boundary.rect.min_lat=48.10171&boundary.rect.min_lon=11.47581&boundary.rect.max_lat=48.27599&boundary.rect.max_lon=11.71119"
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == '__main__':
 load_dotenv() 
 API_KEY=os.getenv('API_KEY')
 app.run(debug=True, port=8080)