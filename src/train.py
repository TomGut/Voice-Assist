import json

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

from model import Neural_Model
from nltk_tools import Nltk_Tools

with open("intents/intents.json", "r") as f:
    data = json.load(f)

all_words = []
tags = []
xy = []
nl = Nltk_Tools()

for intent in data["intents"]:
    tag = intent["tag"]
    tags.append(tag)

    for pattern in intent["patterns"]:
        word = nl.tokenize(pattern)
        all_words.extend(word)
        xy.append((word, tag))

ignore_words = ["?", "!", ".", ","]
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


class Chat_Dataset(Dataset):
    def __init__(self) -> None:
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples


dataset = Chat_Dataset()
train_loader = DataLoader(
    dataset=dataset, batch_size=8, shuffle=True, num_workers=2
)

hidden_size = 8
output_size = len(tags)
input_size = len(x_train[0])
learning_rate = 0.001
epoch_num = 1000

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = Neural_Model(input_size, hidden_size, output_size).to(device)

# Loss and optimizer
crit = nn.CrossEntropyLoss()
opt = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Training loop
for epoch in range(epoch_num):
    for (words, labels) in train_loader:
        words = words.to(device, dtype=torch.float)
        labels = labels.to(device)

        # Forward
        outputs = model(words)
        loss = crit(outputs, labels)

        # Backoward and optimizer step
        opt.zero_grad()
        loss.backward()
        opt.step()

    if (epoch + 1) % 100 == 0:
        print(f"epoch {epoch+1}/{epoch_num}, loss={loss.item():.4f}")

print(f"final loss, loss={loss.item():.4f}")

# Save trained model
data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "output_size": output_size,
    "hidden_size": hidden_size,
    "all_words": all_words,
    "tags": tags,
}

FILE = "data.pth"
torch.save(data, FILE)
