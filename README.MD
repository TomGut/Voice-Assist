# AI Voice assistant

Simple voice recognition assistant made in Python 3.8 with pytorch (for commands recognition and classification) and nltk - intent based responses.
Case study of machine learning.

## Table of contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Additional info](#additional-info)

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
* OpenWeather API key - fell free to use provided or change for yours
* network access for Google and Openweather API calls

### Install
Highly recommended to establish virtual env before installation.

```
$ git clone https://github.com/TomGut/Voice-Assist.git
$ cd Voice-Assist
$ pip install -r requirements.txt
$ python assistant_run.py
```

OpenWeather API key to get if needed:

1. https://openweathermap.org/
2. make account
3. get your free API key and put it into weather_skill.py



## Additional info

If any new records added into intents.json - model have to be trained again.
In such case:

```
$ python train.py
```