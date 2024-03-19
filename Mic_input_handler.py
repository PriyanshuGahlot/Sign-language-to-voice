import pyttsx3
import time
from pygame import mixer
import os

mixer.init(devicename = "CABLE Input (2- VB-Audio Virtual Cable)")
tts = pyttsx3.init()
def play(output):
    tts.save_to_file(output, "output.wav")
    tts.runAndWait()
    mixer.music.load("output.wav")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(2)
    mixer.music.stop()

def say(output):
    tts.say(output)
    tts.runAndWait()