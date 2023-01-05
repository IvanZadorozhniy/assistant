'''Jarvis Assistant module'''
import logging

import pyautogui
import sounddevice as sd
import speech_recognition as sr
from TTS.api import TTS

import activity_api
import joke_api
import time_api
import wheather_api

SAMPLE_RATE = 16000


class Assistant():
    """
    Assistant
    """

    def __init__(self) -> None:
        self.modet_tts_name = TTS.list_models()[0]
        self.tts = TTS(self.modet_tts_name)
        self.speaker = self.tts.speakers[0]
        self.language = self.tts.languages[0]
        self.recogniser = sr.Recognizer()
        self.recogniser.energy_threshold = 4000

        self.wheather_api = wheather_api.WhetherApi()
        self.activity_api = activity_api.ActivityApi()
        self.joke_api = joke_api.JokeApi()
        self.time_api = time_api.TimeApi()

    def listen(self) -> str or bool:
        """
        listen Listen for audio .

        Returns:
            str or bool: [description]
        """
        try:
            with sr.Microphone() as source:
                logging.debug("Listening....")
                audio = self.recogniser.listen(source)
            try:
                logging.debug("Recognizing...")
                command = self.recogniser.recognize_google(
                    audio, language='en').lower()
                logging.debug('You said: %s', command)
            except Exception as err:
                logging.debug('Please try again %s', err)
                return False
            return command
        except Exception as err:
            logging.debug("Please try again %s", err)
            return False

    def say(self, text: str) -> bool:
        """say Say the given text .

        Args:
            text (str): [description]

        Returns:
            bool: [description]
        """
        speech_wav_format = self.tts.tts(
            text=text,
            speaker=self.speaker,
            language=self.language
        )

        sd.play(speech_wav_format, SAMPLE_RATE)

        status = sd.wait()
        return status

    def do_command(self, command: str) -> bool:
        """
        do_command Get the pyjokes command .

        Args:
            command (str): [description]

        Returns:
            bool: [description]
        """
        # FIXME: create methods or class for each command
        logging.debug(command)
        if "joke" in command:
            answer = self.joke_api.get_joke()
            self.say(answer)
        if "weather" in command:
            answer = self.wheather_api.get_description_of_current_wheather()
            logging.debug(answer)
            self.say(answer)
        if "current time" in command:
            answer = self.time_api.get_description_current_time()
            logging.debug(answer)
            self.say(answer)
        if "screenshot" in command:
            screenshot = pyautogui.screenshot()
            now = self.time_api.get_daytime_now()
            logging.debug(now)
            screenshot.save(f'{now}_screenshot.png')
            logging.debug("saved screenshot")
        if "bored" in command:
            answer = self.activity_api.get_some_activity()
            answer = f'''
                I think you can {answer}
            '''
            self.say(answer)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    jarvis = Assistant()
    jarvis.do_command("current time")
    jarvis.do_command("tell a joke")
    jarvis.do_command("what is the weather")
    jarvis.do_command("screenshot")
    jarvis.do_command("bored")
