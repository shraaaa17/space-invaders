
# app.py
from flask import Flask
from game import start_game

app = Flask(__name__)
                                                                                                                      
@app.route('/start_game')
def initiate_game():
    start_game()  # Call the start_game function from game.py
    return 'Game started!'

if __name__ == '__main__':
    app.run(debug=True)

