from destinations import getDestinations
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/destinations', methods=['GET'])
def test():
  sights = getDestinations()

  return jsonify([sight.toJSON().json for sight in sights])

if __name__ == '__main__':
  app.run(debug=True, port=8080)