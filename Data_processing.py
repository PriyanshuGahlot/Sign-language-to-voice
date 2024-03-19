import os
import mediapipe as mp
import cv2
import pickle

data_dir = "./data"

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands()

data = []
labels = []

for dir in os.listdir(data_dir):
    for img_path in os.listdir(os.path.join(data_dir,dir)):
        temp = []
        img = cv2.imread(os.path.join(data_dir,dir,img_path))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        result = hands.process(img)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                #mp_drawing.draw_landmarks(img,hand_landmark,mp_hands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),mp_drawing_styles.get_default_hand_connections_style())
                for i in hand_landmarks.landmark:
                    x = i.x
                    y = i.y
                    temp.append(x)
                    temp.append(y)
            data.append(temp)
            labels.append(dir)

f = open("processed_data.pickle","wb")
pickle.dump({"data":data,"labels":labels},f)
f.close()