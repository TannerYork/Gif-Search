from flask import Flask, render_template, request, redirect, escape
from dotenv import load_dotenv
import speech_recognition as sr
import requests
import os

load_dotenv()
TENOR_API_KEY = os.getenv('TENOR_API_KEY')
app = Flask(__name__)

def recognize_speech():
    """
    A function that will take the speech input from the user
    and store it in 'words' variable which we can later pass on
    to the query string since it is stored as a string
    """
    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for speech terms...")
        audio = r.listen(source)
    try:
        words = r.recognize_google(audio)
        print(f"You said: {words!r}")
        return words
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    The homepage route. This will call the Tenor API
    and parse the returned JSON response and store the desired
    gifs into a list which we will later show in our HTML file
    """
    print("Querying Tenor API...")
    query = request.args.get('query')
    key = TENOR_API_KEY
    limit = 12
    params = { "q": query, "key": key, "limit": limit}
    response = requests.get('https://api.tenor.com/v1/search', params=params)
    gifs = response.json()["results"]
    print("Rendering GIFs...")
    return render_template("index.html", gifs=gifs)

@app.route('/typeahead', methods=['POST', 'GET'])
def typeahead():
    key = TENOR_API_KEY
    user_input = ''
    if 'user_input' in request.form:
        user_input = request.form['user_input']
    response = requests.get(f'https://api.tenor.com/v1/search?key={key}&q={user_input}&limit={12}')
    gifs = response.json()["results"]
    return render_template("gif.html", gifs=gifs)

@app.route('/speak')
def speak():
    """
    A function for searching gifs using Voice command.
    This route will be used when the microphone Icon is pressed
    it will call the previous speech function and pass the returned string as
    a query string
    """
    query = recognize_speech()
    return redirect('/?query=' + escape(query))

if __name__ == '__main__':
    print("Starting Flask server...")
    # host = os.getenv('IP', '0.0.0.0')  # slow to bind host 0.0.0.0
    port = int(os.getenv('PORT', 4444))
    app.run(port=port, debug=True)