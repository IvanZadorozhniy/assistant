'''Jarvis Assistant module'''
import speech_recognition as sr

from TTS.api import TTS

import sounddevice as sd

import pyjokes

SAMPLE_RATE = 16000


class Assistant():
    """Assistant
    """

    def __init__(self) -> None:
        self.modet_tts_name = TTS.list_models()[0]
        self.tts = TTS(self.modet_tts_name)
        self.speaker = self.tts.speakers[0]
        self.language = self.tts.languages[0]
        self.recogniser = sr.Recognizer()
        self.recogniser.energy_threshold = 4000

    def listen(self) -> str or bool:
        """listen Listen for audio .

        Returns:
            str or bool: [description]
        """
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = self.recogniser.listen(source)
            try:
                print("Recognizing...")
                command = self.recogniser.recognize_google(
                    audio, language='en').lower()
                print(f'You said: {command}')
            except Exception as err:
                print(f'Please try again {err =}')
                return False
            return command
        except Exception as err:
            print(f"Please try again {err =}")
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
        """do_command Get the pyjokes command .

        Args:
            command (str): [description]

        Returns:
            bool: [description]
        """
        if "jokes" in command:
            status = self.say(pyjokes.get_joke())
            print(status)