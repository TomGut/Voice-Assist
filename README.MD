# AI Voice assistant

Simple voice assistant app created in Python with PyTorch and Speech Recognition.

## Table of contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Additional info](#additional-info)

## General info

Communication with assistant by voice - speakers and mic needed.

## Technologies

The project is created with:
* Python 3.8.1
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

## Recommended

Installation and running in virtual enviroment

### Install

```
$ mkdir voice_bot
$ cd voice_bot
$ git clone https://github.com/TomGut/Voice-Assist.git
$ pip install -r requirements.txt
$ python assistant_run.py

```

## Addidtional info

If any new records added into intents.json - model have to be trained again.
In such case:

```
$ python train.py

```