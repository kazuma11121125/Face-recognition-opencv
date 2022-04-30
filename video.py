import cv2

resize =4

#VideoCapture オブジェクトを取得
cap = cv2.VideoCapture('vtest.mp4')

#動画のプロパティを取得
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
#書き出し設定
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
writer = cv2.VideoWriter('movie_resied.mp4',fourcc, fps, (int(width/resize), int(height/resize)))

cap.isOpened()== False

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame,(int(width/resize), int(height/resize)))
    writer.write(frame)

writer.release()
cap.release()


cap = cv2.VideoCapture("movie_resied.mp4")
HAAR_FILE = "haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(HAAR_FILE)
if (cap.isOpened()== False):  
  print("ビデオファイルを開くとエラーが発生しました") 

while(cap.isOpened()):

    ret, frame = cap.read()
    if ret == True:
        face = cascade.detectMultiScale(frame)
        for x, y, w, h in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
        rects = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
        print('検出された人数\n: {}'.format(len(rects)))
        cv2.imshow("Video", frame)
    
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
    
    else:
        break

cap.release()

cv2.destroyAllWindows()