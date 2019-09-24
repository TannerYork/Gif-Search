#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, escape
import requests
import os

"""
The following function will take the speech input from the user
and store it in 'words' variable which we can later pass on
to the query string since it is stored as a string
"""


def recognize_speech():
    import speech_recognition as sr
    
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


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
"""
This is the homepage. It will call the Tenor API
and parse the returned JSON response and store the desired
gifs into a list which we will later show in our HTML file
"""
def index():
    print("Querying Tenor API...")
    query = request.args.get('query')
    key = "9KNYSIPBLNC1"
    limit = 12

    params = {
        "q": query,
        "key": key,
        "limit": limit
    }

    response = requests.get('https://api.tenor.com/v1/search', params=params)

    gifs = response.json()["results"]

    print("Rendering GIFs...")
    return render_template("index.html", gifs=gifs)

@app.route('/typeahead', methods=['POST', 'GET'])
def typeahead():
    key = "9KNYSIPBLNC1"
    user_input = ''
    if 'user_input' in request.form:
        user_input = request.form['user_input']
    response = requests.get(f'https://api.tenor.com/v1/search?key={key}&q={user_input}&limit={12}')
    gifs = response.json()["results"]
    return render_template("gif.html", gifs=gifs)

"""
The following function is for searching using Voice command.
This route will be used when the microphone Icon is pressed
it will call the previous speech function and pass the returned string as
a query string
"""
@app.route('/speak')
def speak():
    query = recognize_speech()
    return redirect('/?query=' + escape(query))

if __name__ == '__main__':
    print("Starting Flask server...")
    # host = os.getenv('IP', '0.0.0.0')  # slow to bind host 0.0.0.0
    port = int(os.getenv('PORT', 4444))
    app.run(port=port, debug=True)