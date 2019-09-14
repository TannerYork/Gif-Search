#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, escape
import requests
import json
import os


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


@app.route('/')
def index():
    """Return homepage."""
    return render_template("index.html", gifs=[])


@app.route('/speak')
def speak():
    # TODO: Extract query term from url
    query = recognize_speech()
    return redirect('/results?query=' + escape(query))


@app.route('/results')
def results():
    print("Querying Tenor API...")
    query = request.args.get('query')
    key = "9KNYSIPBLNC1"
    limit = 12

    # TODO: Make 'params' dict with query term and API key
    params = {
        "q": query,
        "key": key,
        "limit": limit
    }

    # TODO: Make an API call to Tenor using the 'requests' library
    response = requests.get('https://api.tenor.com/v1/search', params=params)

    # TODO: Get the GIFs from the search results
    gifs = response.json()["results"]

    print("Rendering GIFs...")
    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    return render_template("index.html", gifs=gifs)


if __name__ == '__main__':
    print("Starting Flask server...")
    # host = os.getenv('IP', '0.0.0.0')  # slow to bind host 0.0.0.0
    port = int(os.getenv('PORT', 4444))
    app.run(port=port, debug=True)

