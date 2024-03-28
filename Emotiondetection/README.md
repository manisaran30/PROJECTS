1.The objective of project is to recognize facial emotions in real-time through a webcam.
2.I used OpenCV and Keras library for computer vision tasks for accessing webcam and keras deep learning library for building and training neural netwroks.
3.Included numpy for numerical computations,often used for handling arrays and matrices.
4.Downloaded pre-trained CNN model from JSON (facialemotionmodel.json) and its weights (facialemotionmodel.h5) using Keras.
5.Haar cascade classifier (haarcascade_frontalface_default.xml) is used for detecting faces in the webcam feed. Detected faces are framed with rectangles for visualization.
6.The used emotions are Angry,Disgust,Fear,Happy,Neutral,Sad,Surprise.
