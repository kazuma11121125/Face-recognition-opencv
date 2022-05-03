import cv2
import face_recognition
from PIL import Image, ImageFont, ImageDraw
from concurrent.futures import ThreadPoolExecutor
import glob

resize = 4
ok = False

PATHS = [
    "vtest.mp4",#ビデオデータ
    "movie_resied.mp4",  # 解像度変更したビデオデータ
    "image/elon_test.jpg"  # 対象人物指定画像

]
XML_PATH = "haarcascade_frontalface_default.xml"


# VideoCapture オブジェクトを取得
cap = cv2.VideoCapture(PATHS[0])

# 動画のプロパティを取得
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# 書き出し設定
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
writer = cv2.VideoWriter(PATHS[1],fourcc, fps, (int(width/resize), int(height/resize)))

cascade = cv2.CascadeClassifier(XML_PATH)
img1 = cv2.imread(PATHS[2])
rects1 = cascade.detectMultiScale(img1, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
print('[hog] 検出された対象人物人数: {}'.format(len(rects1)))

# 画質変換
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame,(int(width/resize), int(height/resize)))
    writer.write(frame)

writer.release()
cap.release()


cap = cv2.VideoCapture(PATHS[2])  # ビデオ読み込み

if not cap.isOpened():  
    print(f"{PATHS[2]} が正常に読み込めませんでした。")
    exit()

se = 0

def makevido():
    img_array = []
    for filename in sorted(glob.glob("Analysis_result_hog/*.jpg")):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    name = 'Face recognition.mp4'
    out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'MP4'), 5.0, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release
    global ok
    ok = True

while cap.isOpened():
    se = se+1
    ret, frame = cap.read()
    if ret == True:

        face = cascade.detectMultiScale(frame)
        for x, y, w, h in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
        rects = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
        print('検出された人数: {}'.format(len(rects)))
        ho = len(rects)
        if ho > 0:
            cascade = cv2.CascadeClassifier(XML_PATH)
            img1 = cv2.imread(PATHS[2])
            rects1 = cascade.detectMultiScale(img1, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
            print('[hog] 検出された対象人物人数: {}'.format(len(rects1)))
            print(f"[hog] {ho}")
            y = len(rects1)
            print(f"[hog] {y}")
            for i in range(ho):
                print(f"[hog] {i}")
                try:
                    for a in range(y):
                        # step1 画像読み込みとコンバート
                        img_elon = frame
                        img_test = face_recognition.load_image_file(PATHS[2])
                        img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)
                        # step2 顔認証
                        face_loc = face_recognition.face_locations(img_elon)[i]
                        # 128次元の顔エンコーディングのリスト
                        encode_elon = face_recognition.face_encodings(img_elon)[i]
                        cv2.rectangle(img_elon, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 255), 2)
                        print(f"[hog] {a}")
                        face_loc_test = face_recognition.face_locations(img_test)[a]
                        encode_elon_test = face_recognition.face_encodings(img_test)[a]

                        # print(encode_elon_test)
                        cv2.rectangle(img_test, (face_loc_test[3], face_loc_test[0]), (face_loc_test[1], face_loc_test[2]), (255, 0, 255), 2)

                        # ２つの画像が同一人物かの判定
                        results = face_recognition.compare_faces([encode_elon], encode_elon_test)
                        # 値が小さい程マッチしている
                        face_dis = face_recognition.face_distance([encode_elon], encode_elon_test)
                        print(f"[hog] {results, face_dis}")
                        p = 1 - face_dis[0]
                        probability = p*100
                        print(f"[hog] {probability}")
                        if results == [False]:
                            res = "No match."
                        elif results == [True]:
                            if probability < 60:
                                res = "little match"
                            elif probability > 60:
                                res = "Match found."
                        text = f"{res}:{probability}%"
                        resu = f'result_hog/{i}{a}{se}.jpg'
                        resu1 = f'result_hog/{i}{a}{se}_tm.jpg'
                        cv2.imwrite(resu, img_elon)
                        cv2.imwrite(resu1, img_test)
                        pic = Image.open(resu)
                        pic1 = Image.open(resu1)
                        img_resize = pic.resize((1000, 800))
                        img_resize1 = pic1.resize((400, 300))
                        reze = f'result_hog/{i}{a}{se}_ts.jpg'
                        reze1 = f'result_hog/{i}{a}{se}_tm_ts.jpg'
                        img_resize.save(reze)
                        img_resize1.save(reze1)

                        fnt = ImageFont.truetype("arial.ttf", 60)
                        # 画像ファイルを開く
                        photo_img = Image.open(reze)

                        # 中央に文字を入れるため、画像のサイズを保管しておく
                        img_size = photo_img.size

                        # ImageDraw.Drawに画像データを指定することで文字入れや描画ができるようになる
                        draw_img = ImageDraw.Draw(photo_img)

                        # 文字入れ　画像の中央に黒い文字を入れる
                        draw_img.text(
                            (img_size[0] / 2,img_size[1] / 2),
                            text,
                            font = fnt,
                            fill = 'red',
                            anchor = 'mm'
                            )

                        # 保存する
                        graw = f'result_hog/Analysis_result{i}{a}{se}.jpg'
                        photo_img.save(graw)
                        im1 = Image.open(graw)
                        im2 = Image.open(reze1)
                        completion = f'Analysis_result_hog/Analysis_result{i}{a}{se}.jpg'
                        back_im = im1.copy()
                        back_im.paste(im2, (590, 530))
                        back_im.save(completion, quality=95)
                except Exception as e:
                    print("[hog] error" + str(e))
    

cap10 = cv2.VideoCapture('Face recognition.mp4')


makevido()

while ok:

    ret11, frame10 = cap.read()
    if ret11 == True:

        cv2.imshow("Video", frame10)
        
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
    
    else:
        break

cap.release()

cv2.destroyAllWindows()
