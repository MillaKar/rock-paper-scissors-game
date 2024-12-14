from flask import Flask, render_template, request, jsonify
import os
from game_logic import getBotChoice, getWinner, ascii_art, choices

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('programming.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    player_choice = int(data['choice'])
    player_name = data['name']
    bot_choice = getBotChoice()

    player_art = ascii_art[player_choice]
    bot_art = ascii_art[bot_choice]

    result = getWinner(player_choice, player_name, bot_choice)

    return jsonify({
        'player_name': player_name,
        'player_choice': choices[player_choice],
        'player_art': player_art,
        'bot_choice': choices[bot_choice],
        'bot_art': bot_art,
        'result': result
    })

if __name__ == '__main__':
    app.run(debug=True)
