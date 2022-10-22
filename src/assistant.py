import os
import random

from playsound import playsound
import speech_recognition as sr
from gtts import gTTS


class Assistant:
    """
    Class for bot/assistant mian functionalities.
    """

    _name = ""

    def __init__(self, name=None):
        self.sr = sr.Recognizer()
        self.mc = sr.Microphone()
        self.gs = gTTS
        if name is not None:
            self._name = name
        else:
            self._name = "Bot"

        with self.mc as mic:
            self.sr.adjust_for_ambient_noise(mic, 1)

    def get_name(self) -> str:
        """
        Gets bot name set by user in instantiation

        Returns:
            str: bot name
        """
        return self._name

    def respond(self, sentence: str):
        num = random.randint(0, 5)
        response = self.gs(text=sentence, lang="pl")
        file = str(num) + ".mp3"
        response.save(file)
        playsound(file, True)
        os.remove(file)

    def listen(self) -> str:
        """
        Speech recognition functionality - transalte voice fraze into text fraze.

        Returns:
            str: stringified vocal fraze
        """
        with self.mc as mic:
            audio = self.sr.listen(mic)
            phrase = ""
            try:
                phrase = self.sr.recognize_google(
                    audio, language="pl-PL"
                )
            except:
                print("Speech RC error")
                pass
        return phrase
