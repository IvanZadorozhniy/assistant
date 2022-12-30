from TTS.api import TTS
import simpleaudio as sa
import sounddevice as sd
# Running a multi-speaker and multi-lingual model
SAMPLE_RATE = 16000
text_to_speech ='''
Some cool text. It works fine. Thank a lot.
'''
# List available 🐸TTS models and choose the first one
model_name = TTS.list_models()[0]
# Init TTS
tts = TTS(model_name)
# Run TTS
# ❗ Since this model is multi-speaker and multi-lingual, we must set the target speaker and the language
# Text to speech with a numpy output
wav = tts.tts(text_to_speech, speaker=tts.speakers[0], language=tts.languages[0])

sd.play(wav, SAMPLE_RATE)
status = sd.wait() 
# play_obj.wait_done()