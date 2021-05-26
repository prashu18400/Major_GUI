import numpy as np
import cv2
from model_load import model_load
from pre_process import pre_process

age = 0
global img
# def webcam_capture():
#     vid = cv2.VideoCapture(0)
#     while True:
#         ret, frame = vid.read()
#         cv2.imshow('frame', frame)
#         # stop the capture
#         if cv2.waitKey(1) & 0xff == ord('q'):
#             break
#     vid.release()
#     # destroy all the windows shown using destroy method in cv2
#     cv2.destroyAllWindows()

# Load the cascade
def webcam_capture():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # To capture video from webcam.
    cap = cv2.VideoCapture(0)

    # To use a video file as input
    # cap = cv2.VideoCapture('filename.mp4')
    model = model_load()
    model.summary()
    b = True
    while b:
        # Read the frame
        _, img = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            crop_face: object = img[y:y + h, x:x + w]
        # Display
        # cv2.imshow('img', img)
        a = pre_process(crop_face)
        predict = model.predict(np.array([a / 255]))
        age = int(np.round(predict[1][0]))
        # print(age)
        # cv2.imshow('face',crop_face)
        filename = 'save.jpg'
        cv2.imwrite(filename, crop_face)
        # Stop if escape key is pressed
        b = False
        if cv2.waitKey(30) & 0xff == 27:
            break
    # Release the VideoCapture object
    cv2.putText(img, str(age), (450, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('image', img)
    cv2.waitKey(2000)
    cap.release()
    cv2.destroyAllWindows()
    return age
