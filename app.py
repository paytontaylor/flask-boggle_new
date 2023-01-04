from flask import Flask, render_template, session, request, jsonify
from boggle import Boggle

app = Flask(__name__)
boggle_game = Boggle()

app.secret_key = 'secret'


@app.route('/')
def show_board():
    """ Displays Game Board """
    board = boggle_game.make_board()
    session['board'] = board

    high_score = session.get('high-score', 0)
    times_played = session.get('times-played', 0)

    return render_template("boggle.html", board=board, high_score=high_score, times_played=times_played)


@app.route('/check-word', methods=['POST'])
def check_word():
    """ Checks if word is Valid or just Not on Board """
    board = session['board']
    word = request.get_json()['guess']
    result = boggle_game.check_valid_word(board, word)
    return jsonify(result=result)


@app.route('/check-score', methods=['POST'])
def get_stats():
    """ Checks for new high score and tracks times played """
    high_score = session.get('high-score', 0)
    times_played = session.get('times-played', 0)
    score = request.json['score']

    if score > high_score:
        high_score = score
        session['high-score'] = high_score

    result = session['high-score']
    session['times-played'] = times_played + 1

    return jsonify(high_score=result)
