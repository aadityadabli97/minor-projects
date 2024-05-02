from flask import Flask
import random

app = Flask(__name__)

random_number=random.randint(0,9)

@app.route("/")
def guess_number():
    return '<h1><b>Guess a number between 0 and 9</b></h1>'\
           '<iframe src="https://giphy.com/embed/3o7aCSPqXE5C6T8tBC" width="400" height="400"</iframe>'

@app.route("/<int:number>")
def check_number(number):
    if number< random_number:
        return '<h1 color="red"><b>Too low , try again !</b></h1>'\
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="400" height="400">'
    elif number > random_number:
        return '<h1 color="purple"><b>Too high , try again !</b></h1>'\
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="400" height="400">'
    else:
        return '<h1 color="green"><b>You found me !</b></h1>'\
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="400  " height="400">'


if __name__=="__main__":
    app.run(debug=True)