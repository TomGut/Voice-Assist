
import json

import numpy as np

from nltk_tools import Nltk_Tools

with open('intents/intents.json', 'r') as f:
    data = json.load(f)

all_words = []
tags = []
xy = []
nl = Nltk_Tools()

for intent in data['intents']:
    tag = intent['tag']
    tags.append(tag)

    for pattern in intent['patterns']:
        word = nl.tokenize(pattern)
        all_words.extend(word)
        xy.append((word, tag))

ignore_words = ['?', '!', ".", ","]
all_words = [nl.stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

x_train = []
y_train = []

for (pattern_sentence, tag) in xy:
    bag = nl.bag_of_words(pattern_sentence, all_words)
    x_train.append(bag)
    label = tags.index(tag)
    y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)
