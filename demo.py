import cv2

cap=cv2.VideoCapture(0)
cap.set(3,120)
cap.set(4,720)

while True:
    success, img=cap.read()
    cv2.imshow("Face Attendance",img)
    cv2.waitKey(1)
   