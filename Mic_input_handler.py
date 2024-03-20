import pyttsx3
import time
from pygame import mixer
import os

tts = pyttsx3.init()
def play(output):
    mixer.init(devicename="CABLE Input (2- VB-Audio Virtual Cable)")
    tts.save_to_file(output, "output.wav")
    tts.runAndWait()
    mixer.music.load("output.wav")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(0.1)
    mixer.music.stop()
    mixer.quit()
    os.remove("output.wav")

def say(output):
    tts.say(output)
    tts.runAndWait()