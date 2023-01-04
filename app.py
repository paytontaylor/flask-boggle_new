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

    return render_template("boggle.html", board=board)


@app.route('/check-word', methods=['POST'])
def check_word():
    board = session['board']
    word = request.get_json()['guess']
    result = boggle_game.check_valid_word(board, word)
    return jsonify(result=result)


@app.route('/get-stats')
def get_stats():
    final_score = request.json

    return jsonify(score=final_score)
