import cv2
import sys
from fisherfaces import *

class EnvironmentVariables:
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
        self.profileCascade = cv2.CascadeClassifier("haarcascade_profileface.xml")
        self.video_capture = cv2.VideoCapture(0)
        
    def captureVariables(self):
        while True:
            # Capture frame-by-frame
            ret, frame = self.video_capture.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            facesFront = self.faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )

            facesProfile = self.profileCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )
            print str(len(facesFront) + len(facesProfile))
    
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Advertisement', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything is done, release the capture
        self.video_capture.release()
        cv2.destroyAllWindows()

if __name__=="__main__":
    eV = EnvironmentVariables()
    eV.captureVariables()



    
    
