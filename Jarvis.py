# Only English
import speech_recognition as sr

from TTS.api import TTS

import sounddevice as sd

import pyjokes

SAMPLE_RATE = 16000


class Assistant():

    def __init__(self) -> None:
        self.modet_tts_name = TTS.list_models()[0]
        self.tts = TTS(self.modet_tts_name)
        self.speaker = self.tts.speakers[0]
        self.language = self.tts.languages[0]
        self.recogniser = sr.Recognizer()
        self.recogniser.energy_threshold = 4000

    def listen(self) -> str or bool:

        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = self.recogniser.listen(source)
            try:
                print("Recognizing...")
                command = self.recogniser.recognize_google(
                    audio, language='en').lower()
                print(f'You said: {command}')
            except:
                print('Please try again')
                return False
            return command
        except Exception as e:
            print(e)
            return False

    def say(self, text: str) -> bool:

        speech_wav_format = self.tts.tts(
            text=text,
            speaker=self.speaker,
            language=self.language
        )

        sd.play(speech_wav_format, SAMPLE_RATE)
        
        status = sd.wait()
        return status

    def do_command(self, command: str) -> bool:
        if "jokes" in command:
            status = self.say(pyjokes.get_joke())
            print(status)
