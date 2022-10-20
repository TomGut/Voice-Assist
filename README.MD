<h1>AI Voice assistant</h1>

Simple voice recognition assistant made in Python 3.8 with pytorch (for commands recognition and classification) and nltk - intent based responses.
Case study of machine learning.

This kind of robot/assistant (intent based, predefined question sets) can be used in commercial facilities like store, bank etc. - it respond on simple questions, in a FAQ a like manner.

FOR NOW LINUX ONLY and polish language only. Implementing setup tools shortly to get in work smoothly on Windows.
<br>

## Table of contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Interaction with assistant](#interaction-with-assistant)

## General info

Communication with assistant by voice - speakers and mic needed.
Linux only at the moment. 
Polish language only.

Assistant capabilities (intent based):

* user greeting and goodbye
* self introduction
* capabilities presentation
* time annonucing
* date announcing
* week no announcing
* weather forecasting

## Technologies

Project created with:

* Python 3.8.10 (noted problems lower versions in regard to cooperation with nltk)
* Google SpeechRecognition
* Googe Text to speech (gTTS) 
* Playsound 
* PyAudio 
* PyTorch 
* nltk 


## Setup

### Prerequisites

* python 3.8 or higher
* pip for dependencies installation
* OpenWeather API key - see Install section
* network access for Google and Openweather API calls
* for now tested only on Linux, Windows version will follow shortly

### Install
Highly recommended to establish virtual env before installation.

1. Install codebase:

```
$ git clone https://github.com/forDeFan/Voice-Assist.git
$ cd Voice-Assist
$ pip3 install -r requirements.txt
```

Not required but advised to get your OpenWeather API key for weather forecasting functionality and store it into .env at repo root (see .env-example for reference).
<br>
You can use bash command:

```
$ touch .env && echo OPEN_WEATHER_APIKEY=your__openweather_api_key_here > .env
```

If problems with pyaudio installation on Linux platform:

```
$ apt-get install portaudio19-dev
$ pip3 install pyaudio
```

2. Getting the OpenWeather API key - to have operational weather forecasting functionality:

* https://openweathermap.org/
* make an free account
* store your API key in .env at folder root (see .env-example for reference).


## Interaction with assistant

When started - possible fraze for questions that robot will recognize - can be found in intents.json at "patterns" tag.
Examplionary questions that robot will recognize at the moment:

* Jak się nazywasz ?
* Co potrafisz ?
* Jaki dziś dzień ?
* Która godzina ?
* Jaka będzie dziś pogoda ?

<br>

To start assistant:

```
$ python3 assistant_run.py
```

If any new positions or tags added into intents.json - model have to be trained again.

In such case:

```
$ cd Voice-Assist
$ python3 src/train.py
```

