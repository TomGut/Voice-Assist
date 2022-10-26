import json
import random

import torch
from pyowm.commons import exceptions as ex

from src.assistant import Assistant
from src.model import NeuralModel
from src.nltk_tools import NltkTools
from src.time_skill import TimeSkill
from src.weather_skill import WeatherSkill

if __name__ == "__main__":
    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    with open("intents/intents.json", "r") as f:
        intents = json.load(f)

    # Take trained model
    FILE = "data.pth"
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data["all_words"]
    tags = data["tags"]
    model_state = data["model_state"]

    model = NeuralModel(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    bot = Assistant("Zdzichu")
    nt = NltkTools()
    ts = TimeSkill()

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
        propability = probs[0][predicted.item()]
        # For testing.
        print("propability:", propability.item())

        if propability.item() > 0.75:
            for intent in intents["intents"]:
                if tag == intent["tag"]:
                    bot.respond(random.choice(intent["responses"]))
                    if tag == "goodbye":
                        loop_last = False
                    else:
                        if tag == "time":
                            bot.respond(ts.get_time())
                        if tag == "date":
                            bot.respond(ts.get_date())
                        if tag == "week":
                            bot.respond(ts.get_week_number())
                        if tag == "who_are_you":
                            bot.respond(bot.get_name())
                        if tag == "weather":
                            try:
                                bot.respond("Podaj miasto")
                                city = str(bot.listen().lower())
                                weather = WeatherSkill(city)
                                if weather.temp() is not None:
                                    bot.respond(
                                        "temperatura"
                                        + weather.temp()
                                        + " stopni celsjusza"
                                        + "a słońce wzejdzie o "
                                        + weather.sun_rise()
                                    )
                                else:
                                    # No API key in .env
                                    bot.respond(
                                        "Nie podałeś klucza OpenWeather API w zmiennej dotenv. Co robimy dalej ?"
                                    )

                            # If OpenWeather API wrong key provided.
                            except ex.UnauthorizedError:
                                bot.respond(
                                    "Nieprawidłowy klucz OpenWeather API. Co robimy dalej ?"
                                )

                        bot.respond("Co chciałbyś jeszcze wiedzieć ?")
        else:
            bot.respond("Nie rozumiem")
