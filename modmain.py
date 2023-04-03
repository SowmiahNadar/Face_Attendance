import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np
from datetime import datetime
import os
import webbrowser

cred = credentials.Certificate("faceattendancerealtime-45fd2-firebase-adminsdk-rjc0b-b4ce7e8443.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-45fd2-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-45fd2.appspot.com"
})

bucket = storage.bucket()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('E:\\Projects\\Files\\Resources\\background.png')

# Importing the mode images into a list
folderModePath = 'E:\\Projects\\Files\\Resources\\Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
# print(len(imgModeList))

# Load the encoding file
print("Loading Encode File ...")
file = open('E:\Projects\Files\EncodeFile1.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)
print("Encode File Loaded")

modeType = 0
counter = 0
id = -1
imgStudent = []

# Function to open data.html in a web browser
def open_report():
    webbrowser.open_new_tab('data.html')

while True:
    success, img = cap.read()

    imgS = cv2.resize(img,(0, 0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print("matches", matches)
            # print("faceDis", faceDis)

            matchIndex = np.argmin(faceDis)
            # print("Match Index", matchIndex)

        if matches[matchIndex]:
            # print("Known Face Detected")
            # print(studentIds[matchIndex])
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4,
        # Draw a rectangle around the face
        cv2.rectangle(imgBackground, (x1 + 50, y1 + 162), (x2 + 50, y2 + 162), (0, 255, 0), 2)

        # Display the student ID on top of the rectangle
        cv2.rectangle(imgBackground, (x1 + 50, y1 + 162 - 30), (x2 + 50, y1 + 162), (0, 255, 0), cv2.FILLED)
        cv2.putText(imgBackground, studentIds[matchIndex], (x1 + 50 + 6, y1 + 162 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

        # Set the ID of the recognized student and reset the counter
        id = studentIds[matchIndex]
        counter = 0

    else:
        counter += 1

        # Draw a rectangle around the face
        cv2.rectangle(imgBackground, (x1 + 50, y1 + 162), (x2 + 50, y2 + 162), (0, 0, 255), 2)

        # Display "Unknown" on top of the rectangle
        cv2.rectangle(imgBackground, (x1 + 50, y1 + 162 - 30), (x2 + 50, y1 + 162), (0, 0, 255), cv2.FILLED)
        cv2.putText(imgBackground, "Unknown", (x1 + 50 + 6, y1 + 162 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

        # Reset the ID if the same face is not detected for more than 10 frames
        if counter > 10:
            id = -1

        cv2.imshow("Video", imgBackground)

        # Create the attendance entry in the database and upload the image to the storage bucket
        if cv2.waitKey(1) & 0xFF == ord('q'):
            if id != -1:
                ref = db.reference('students/' + str(id) + '/attendance/' + datetime.now().strftime('%Y-%m-%d'))
                ref.set({
                    'time': datetime.now().strftime('%H:%M:%S'),
                    'status': 'present'
                })
                imgName = str(id) + "_" + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".jpg"
                cv2.imwrite(imgName, imgBackground)
                blob = bucket.blob(imgName)
                blob.upload_from_filename(imgName)
                os.remove(imgName)

            cap.release()
            cv2.destroyAllWindows()

            break

        # Switch to the next mode when "Space" is pressed
        if cv2.waitKey(1) == ord(' '):
            modeType += 1
            if modeType == len(imgModeList):
                modeType = 0

        # Display the report when "r" is pressed
        if cv2.waitKey(1) == ord('r'):
            open_report()
