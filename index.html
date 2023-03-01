from flask import Flask, jsonify, request
from game import generate_number, check_guess

app = Flask(__name__)

# The current game state, including the randomly generated number
# and the number of guesses the user has made so far
game_state = None

@app.route('/')
def index():
    # Display the game instructions and a form for the user to enter their guess
    return """
    <h1>Welcome to the Number Guessing Game!</h1>
    <p>Guess a 4-digit number, and I'll tell you how many digits are correct and in the right position ("xA") and how many digits are correct but in the wrong position ("yB").</p>
    <form method="POST">
        <input type="text" name="guess" placeholder="Enter your guess here">
        <button type="submit">Guess</button>
    </form>
    """

@app.route('/', methods=['POST'])
def guess():
    global game_state
    
    if game_state is None:
        # If this is the first guess, generate a new number and start the game
        game_state = {'number': generate_number(), 'num_guesses': 0}
        
    # Get the user's guess from the form data
    guess = request.form['guess']
    
    # Check the user's guess against the generated number
    result = check_guess(game_state['number'], int(guess))
    game_state['num_guesses'] += 1
    
    # Send the result of the guess back to the client
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
