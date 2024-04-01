from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from urllib.parse import urlencode
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define the endpoint URL
ENDPOINT_URL = "https://atlas.mappls.com/api/places/search/json"
API_TOKEN = "05502e0e-7415-425e-86e2-b22b3e3a50e7"  # Replace with your actual API token

@app.route('/proxy', methods=['GET'])
def proxy_request():
    # Extract query parameter from request
    query = request.args.get("query")

    # Set headers with the API token
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }

    # Make a request to the endpoint
    response = requests.get(ENDPOINT_URL, params={"query": query}, headers=headers)

    # Return the response from the endpoint
    return jsonify(response.json())


# Define the endpoint URL
ENDPOINT_URL_2 = "https://apis.mappls.com/advancedmaps/v1"

@app.route('/proxy/<rest_key>/<resources>/driving/<geopositions>', methods=['GET'])
def proxy_request_2(rest_key, resources, geopositions):
    # Make a request to the endpoint
    response = requests.get(f"{ENDPOINT_URL_2}/{rest_key}/{resources}/driving/{geopositions}")

    # Return the response from the endpoint
    return jsonify(response.json())



if __name__ == '__main__':
    app.run(debug=True)
