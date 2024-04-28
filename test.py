import cv2
import numpy as np
out=cv2.VideoWriter()
cap = cv2.VideoCapture(0)
cap.set(3, 100)
cap.set(4, 200)
print('Width :' + str(cap.get(3)))
print('Height:' + str(cap.get(4)))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    

    frame = cv2.flip(frame,1)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()