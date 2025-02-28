# Sign language to voice over any Application

This project enables real-time conversion of sign language into voice, enhancing communication for sign language users. It works seamlessly with any video conferencing platform (e.g., Google Meet, Zoom) by using the camera to capture gestures and converting them into speech. The generated voice is transmitted to the call receiver via a virtual input device. Users can customize gestures to suit their preferences, ensuring a personalized experience. Since it operates independently of specific applications, it remains highly reliable and compatible across various platforms.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required libraries.

```bash
pip install foobar
pip install opencv-python
pip install mediapipe
pip install scikit-learn
pip install matplotlib
pip install pygame
pip install pyttsx3
```

## Prerequisite

Installation and set up of a virtual audio cable is required.\
Download: [VB-Audio](https://vb-audio.com/Cable/)

## Usage
>Go to the `Data_Collection.py` file.
>- Change the `label` to whatever you what the hand sign to currespond to and `size` to the number of how many images gets stored in the dataset.
>- Make the curresponding hand sign in front of the camera then run the script.
>- Repeat this for all the hand signs you want the model to work on.
>
>Run `Data_processing.py`
>- This will extract all the data from the image using `mediapipe`.
>- Save it as `processed_data.pickle` using `pickle` for the ML model to be trained on.
>
>Run `Model_training.py`
>- This will create a `RandomForestClassifier` and train in on the `processed_data.pickle`
>- Save the model using `pickle` as `model.p` so that it does not need to be trained everytime before use.
>- Model accuracy will be displayed as output in the terminal.
>
>Run `main.py`
>- Loading of `model.p` using `pickle`
>- Camera capture will begin usign `cv2`
>- Taking the camera input which contains a hand sign made by the user and processing it with the help `mediapipe`
>- Processed data will go as input to the model and it will output the corresponding label to the hand sign as string.
>- Using `Mic_input_handler.py` the string output will get converted to audio output using `pyttsx3` and get piped to the users mic using `pygame` as mic input.
>- Result will be the reciver hearing the audio output piped to the mic though their speaker.



#### Demo of the project is available here: [LinkedIn Post](https://www.linkedin.com/posts/priyanshu-gahlot_machinelearning-signlanguage-accessibility-activity-7176229889316937728-hK5K?utm_source=share&utm_medium=member_desktop)

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
