<h1>AI Voice assistant</h1>

Simple voice recognition assistant made in Python 3.8 with pytorch (for commands recognition and classification) and nltk - intent based responses.
Case study of machine learning.

It's a simple console app.

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

* Python 3.8.10 (noted problems wih < versions in cooperation with nltk)
* Google SpeechRecognition 3.8.1
* Googe Text to speech (gTTS) 2.2.3
* Playsound 1.3.0
* PyAudio 0.2.11
* PyTorch 1.10.2
* nltk 3.6.7


## Setup

### Prerequisites

* python 3.8 or higher
* pip for dependencies installation
* OpenWeather API key - see Install section
* network access for Google and Openweather API calls

### Install
Highly recommended to establish virtual env before installation.

1. Install codebase:

```
$ git clone https://github.com/TomGut/Voice-Assist.git
$ cd Voice-Assist
$ pip install -r requirements.txt
```

Get your OpenWeather API key for weather forecasting functionality and
store it into .env at repo root

```
$ touch .env && echo OPEN_WEATHER_APIKEY=your__openweather_api_key_here > .env
```

If problems with pyaudio installation:

```
$ apt-get install portaudio19-dev
$ pip install pyaudio
```

2. Get OpenWeather API key if want to have weather forecasting functionality:

* https://openweathermap.org/
* make an free account
* store your API key in .env at folder root with key: OPEN_WEATHER_APIKEY=your__openweather_api_key_here


## Interaction with assistant

When started - possible question can be found in intents.json at "patterns" tag.

If any new positions or tags added into intents.json - model have to be trained again.
In such case:

```
$ python train.py
```

To start assistant:

```
$ python assistant_run.py
```
