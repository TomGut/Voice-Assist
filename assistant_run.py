import json

import torch
import random

from src.assistant import Assistant
from src.model import Neural_Model
from src.nltk_tools import Nltk_Tools
from src.time_skill import Time_Skill

if __name__ == "__main__":
    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    with open("intents/intents.json", "r") as f:
        intents = json.load(f)

    FILE = "data.pth"
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data["all_words"]
    tags = data["tags"]
    model_state = data["model_state"]

    model = Neural_Model(input_size, hidden_size, output_size).to(
        device
    )
    model.load_state_dict(model_state)
    model.eval()

    bot = Assistant("Zdzichu")
    nt = Nltk_Tools()
    ts = Time_Skill()

    command = ""
    WAKE = bot.get_name()
    bot.respond("Możesz mówić")

    loop_last = True
    while loop_last:
        command = bot.listen().lower()
        command = nt.tokenize(command)

        X = nt.bag_of_words(command, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device, dtype=torch.float)

        output = model(X)
        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]
        # For testing.
        print("predicted: ", tag)

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        # For testing.
        print("prob:", prob.item())

        if prob.item() > 0.80:
            for intent in intents["intents"]:
                if tag == intent["tag"]:
                    bot.respond(random.choice(intent["responses"]))
                    if tag == "time":
                        bot.respond(ts.get_time())
                    if tag == "date":
                        bot.respond(ts.get_date())
                    if tag == "week":
                        bot.respond(ts.get_week_number())
                    if tag == "who_are_you":
                        bot.respond(bot.get_name())
                    if tag == "goodbye":
                        loop_last = False
        else:
            bot.respond("Nie rozumiem")
