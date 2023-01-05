'''Jarvis Assistant module'''
import logging
import time
from datetime import datetime
import inflect
import pyjokes
import sounddevice as sd
import speech_recognition as sr
from TTS.api import TTS

import whether

SAMPLE_RATE = 16000
import activity_api
import pyautogui



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
        self.whether_api = whether.Whether()
        self.inflect_engine = inflect.engine()
        self.activity_api = activity_api.ActivityApi()

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

    def __number_to_words(self, number):
        """__number_to_words Convert number to words .

        Args:
            number ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self.inflect_engine.number_to_words(number)

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
            status = self.say(pyjokes.get_joke())
            logging.debug(status)
        if "weather" in command:
            wheather_info = self.whether_api.get_current_whether()

            temp = self.__number_to_words(wheather_info['current_temperature'])
            wind = self.__number_to_words(wheather_info['current_wind'])
            desc = wheather_info['weather_description']

            answer = f"""
                Today's whether is {desc}.
                The Temparature is {temp} degrees Celsius.
                The Wind is {wind} meters per second.
            """
            logging.debug(answer)
            self.say(answer)
        if "current time" in command:
            cur_time = time.localtime()

            hours = self.__number_to_words(time.strftime("%H", cur_time))
            minutes = self.__number_to_words(time.strftime("%M", cur_time))
            answer = f'''
                The current time is {hours} hours, and {minutes} minutes
            '''
            logging.debug(answer)
            self.say(answer)
        if "screenshot" in command:
            screenshot = pyautogui.screenshot()
            now = datetime.now()
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
    # jarvis.do_command("current time")
    # jarvis.do_command("tell a joke")
    # jarvis.do_command("what is the weather")
    # jarvis.do_command("screenshot")
    jarvis.do_command("bored")
