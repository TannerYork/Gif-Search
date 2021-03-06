[![Gif Search](https://circleci.com/gh/TannerYork/Gif-Search.svg?style=svg)](<LINK>) <br>
[![Gif Search](https://circleci.com/gh/TannerYork/Gif-Search.svg?style=shield)](<LINK>) <br>
![Gif Search](https://img.shields.io/docker/image-size/tannerwyork/gif-search/latest) <br>
![Gif Search Web](https://img.shields.io/website?down_color=red&down_message=offline&up_color=light%20green&up_message=online&url=https%3A%2F%2Fgif-search.caprover.dev.tanneryork.tech%2F)

# How to Use This Code

Create a .env file based on the .env.example file

## Docker
Clone or fork repo and make sure Docker is running. (Note: Speach Recognition does not work in docker continer)

#### Docker Compose 
```bash
docker-compose up -d
```
#### Docker Run
```bash
docker build -t gif-search_web .
docker run -p 8000:8000 --rm --name gif_container gif-search_wed
```

## Python/Pip
Install Flask, SpeechRecongition, PortAudio, and PyAudio modules:

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

Run the server:

```bash
flask run
```

# gif-search
<h3>You have options to use both Speech Recognition to look for the 
Gifs you want or you can also simply search in the search bar</h3>
