from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)


NFL_API_URL = 'https://api.example.com/nfl/stats'  
API_KEY = os.getenv('NFL_API_KEY')  

@app.route('/search-player', methods=['GET'])
def search_player():
    player_name = request.args.get('name')  
    if not player_name:
        return jsonify({"error": "Player name is required"}), 400
    
    
    response = requests.get(f'{NFL_API_URL}/player/search', params={'name': player_name},
                            headers={"Authorization": f"Bearer {API_KEY}"})

    
    if response.status_code == 200:
        return jsonify(response.json()) 
    else:
        return jsonify({"error": "Player not found or API error"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
