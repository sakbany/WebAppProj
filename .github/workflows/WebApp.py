from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)


NFL_API_URL = 'https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLPlayerList'  
API_KEY = os.getenv('b2ea909a78mshdcec5c927fe2abep115452jsn564e16b59c26')  

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
