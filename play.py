import cv2

cap10 = cv2.VideoCapture('Face recognition.mp4')

while True:

    ret11, frame10 = cap10.read()
    if ret11 == True:

        cv2.imshow("Video", frame10)
        
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
    
    else:
        break

cap10.release()