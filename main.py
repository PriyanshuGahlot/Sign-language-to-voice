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
            min_x, min_y = float('inf'), float('inf')
            max_x, max_y = float('-inf'), float('-inf')
            for idx, landmark in enumerate(hand_landmarks.landmark):
                # Get the pixel coordinates of the landmark
                height, width, _ = frame.shape
                cx, cy = int(landmark.x * width), int(landmark.y * height)
                print(f"Landmark {idx}: ({cx}, {cy})")

                # Draw a small circle at the landmark position
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)
            # for landmark in hand_landmarks.landmark:
            #     height, width, _ = frame.shape
            #     x, y = int(landmark.x * width), int(landmark.y * height)
            #     min_x = min(min_x, x)
            #     min_y = min(min_y, y)
            #     max_x = max(max_x, x)
            #     max_y = max(max_y, y)
            #
            # cv2.rectangle(frame, (int(0.7*min_x), int(0.7*min_y)), (int(max_x*1.1), int(max_y*1.1)), (0, 255, 0), 2)


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