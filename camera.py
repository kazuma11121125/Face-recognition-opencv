import cv2
import time
import datetime
HAAR_FILE = "haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(HAAR_FILE)

FPS = 15
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, FPS)
print(cap.get(cv2.CAP_PROP_FPS))


while True:
    ret, frame = cap.read()

    face = cascade.detectMultiScale(frame)

    for x, y, w, h in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
    rects = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
    print('検出された人数\n: {}'.format(len(rects)))
    if len(rects) >=1:
        date = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"{date}.jpg"
        cv2.imwrite(path, frame)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):#qで終了
        break
    time.sleep(0.2)#処理能力の制限 CPUが限界になる　severで動かすのにはもっといる

cap.release()
cv2.destroyAllWindows() 