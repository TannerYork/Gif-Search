# How to Use This Code

Install Flask, SpeechRecognition, PortAudio, and PyAudio modules:

```bash
pip3 install flask
```

```bash
pip3 install SpeechRecognition
```

```bash
brew install portaudio
brew link --overwrite portaudio
pip3 install portaudio
pip3 install pyaudio
```

You can test if the module is installed with the following command
```bash
python3 -m speech_recognition
```

Set up Flask to run in development environment:

```bash
export FLASK_ENV=development
```

Run the server:

```bash
flask run
```

# gif-search
<h3>You have options to use both Speech Recognition to look for the 
Gifs you want or you can also simply search in the search bar</h3>
