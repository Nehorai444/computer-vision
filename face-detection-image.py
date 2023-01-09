import cv2

##########################
####CREATED BY NEHORAI L.#
##########################


img = cv2.imread('./Nadia_Murad.jpg')

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

def face_detection(img):
    
    face_copy = img.copy()
    face_rects = face_cascade.detectMultiScale(face_copy)
    
    
    for(x,y,w,h) in face_rects:
        cv2.rectangle(face_copy,(x,y),(x+w,y+h),(255,255,255),10)
    return face_copy

img = face_detection(img)

while True:
    
    cv2.imshow('face_detection',img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
#DONE