import cv2

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

def face_detection(img):
    
    face_copy = img.copy()
    face_rects = face_cascade.detectMultiScale(face_copy)
    
    
    for(x,y,w,h) in face_rects:
        cv2.rectangle(face_copy,(x,y),(x+w,y+h),(255,255,255),10)
    return face_copy

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read(0)
    frame = face_detection(frame)

    cv2.imshow('Video Face_Detect', frame)

    k = cv2.waitKey(1)
    if k  & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()