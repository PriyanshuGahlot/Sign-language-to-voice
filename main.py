import cv2
import mediapipe as mp

# import pyttsx3
#
# tts = pyttsx3.init()
# tts.say("")
# tts.runAndWait()

hands = mp.solutions.hands.Hands()
camera = cv2.VideoCapture(0)

while(True):
    _, frame = camera.read()
    frame = cv2.flip(frame, 1)
    height, width, _ = frame.shape
    results = hands.process(frame)
    if results.multi_hand_landmarks:
        # Hands were detected
        for hand_landmarks in results.multi_hand_landmarks:
            drawing = mp.solutions.drawing_utils
            drawing.draw_landmarks(frame,hand_landmarks,mp.solutions.hands.HAND_CONNECTIONS,mp.solutions.drawing_styles.get_default_hand_landmarks_style(),mp.solutions.drawing_styles.get_default_hand_connections_style())
            print(hand_landmarks)


    cv2.imshow("Camera", frame)
    if (cv2.waitKey(1) == ord("q")):
        break

camera.release()
cv2.destroyWindow()


#to play mp3 file as mic input
# import time
# from pygame import mixer
#
# mixer.init(devicename = "CABLE Input (2- VB-Audio Virtual Cable)") # Initialize it with the correct device
# mixer.music.load("output.wav") # Load the mp3
# mixer.music.play() # Play it
#
# while mixer.music.get_busy():  # wait for music to finish playing
#     time.sleep(1)