import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import  storage
 
cred = credentials.Certificate("faceattendancerealtime-45fd2-firebase-adminsdk-rjc0b-b4ce7e8443.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-45fd2-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-45fd2.appspot.com"
})
 
 
# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    img = cv2.imread(os.path.join(folderPath, path))
    if img is not None:
        imgList.append(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        studentIds.append(os.path.splitext(path)[0])
 
        fileName = f'{folderPath}/{path}'
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_filename(fileName)
 
        # print(path)
        # print(os.path.splitext(path)[0])
print(studentIds)
 
 
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        encode = face_recognition.face_encodings(img)
        if len(encode) > 0:
            encodeList.append(encode[0])
 
    return encodeList
 
 
print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")
 
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
