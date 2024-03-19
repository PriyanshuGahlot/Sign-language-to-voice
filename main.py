import os
from Mic_input_handler import play
from Mic_input_handler import say
import cv2
import mediapipe as mp
import pickle
import numpy as np
import threading


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True)

camera = cv2.VideoCapture(0)

model = pickle.load(open("model.p","rb"))["model"]

lastOutput = ""

while(True):
    temp = []
    _, frame = camera.read()
    frame = cv2.flip(frame, 1)
    result = hands.process(frame)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                      mp_drawing_styles.get_default_hand_landmarks_style(),
                                      mp_drawing_styles.get_default_hand_connections_style())
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                temp.append(x)
                temp.append(y)
        output = model.predict([np.asarray(temp)])
        if(output!=lastOutput):
            lastOutput = output
            print(output)
            threading.Thread(target=say, args=(output)).start()
            #threading.Thread(target=play, args=(output)).start()
            #play(output)


    cv2.imshow("Camera", frame)
    if (cv2.waitKey(1) == ord("q")):
        break

camera.release()
cv2.destroyWindow()
