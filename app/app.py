from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

NODEJS_BASE_URL = 'http://nodejs_microservice_url:port'

@app.route('/api/data', methods=['GET'])
def get_data():
    response = requests.get(f'{NODEJS_BASE_URL}/api/data')
    return response.json(), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
