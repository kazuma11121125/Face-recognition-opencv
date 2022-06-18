import cv2
import face_recognition
from PIL import Image, ImageFont, ImageDraw
from concurrent.futures import ThreadPoolExecutor
import glob
import time
ok = False

PATHS = [
    "vtest.mp4",#ビデオデータ
    "vtest_set.mp4",  # 解像度変更したビデオデータ
    "image/elon_test.png"  # 対象人物指定画像

]
XML_PATH = "haarcascade_frontalface_default.xml"

cap100= cv2.VideoCapture(PATHS[0])

# 動画のプロパティを取得
width = int(cap100.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap100.get(cv2.CAP_PROP_FRAME_HEIGHT))
#fps = cap.get(cv2.CAP_PROP_FPS)
fps = 10
saizu = (720,480)
# 書き出し設定
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
writer = cv2.VideoWriter(PATHS[1],fourcc, fps, saizu)
frame_sec_all_1 = cap100.get(cv2.CAP_PROP_FRAME_COUNT)
# 画質変換
o = 0
while True:
    print(f"[hog] 現在 {o}/{frame_sec_all_1}")
    o = o+1
    ret, frame = cap100.read()
    if not ret:
        break
    frame = cv2.resize(frame,saizu)
    writer.write(frame)

writer.release()
cap100.release()

cascade = cv2.CascadeClassifier(XML_PATH)
img1 = cv2.imread(PATHS[2])
rects1 = cascade.detectMultiScale(img1, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
print('[hog] 検出された対象人物人数: {}'.format(len(rects1)))


cap20 = cv2.VideoCapture(PATHS[1])  # ビデオ読み込み
print(cap20)
if not cap20.isOpened():  
    print(f"{PATHS[1]} が正常に読み込めませんでした。")
    exit()
frame_sec_all = cap20.get(cv2.CAP_PROP_FRAME_COUNT)

se,noe,frame_sec,v = 0,0,0,0

# ビデオ出力先ファイルの指定
name = 'Face recognition hog.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter(name,fourcc,30,(1000, 800))

while (cap20.isOpened()):
    try:
        frame_sec = frame_sec+1
        print(f"[hog] 現在{frame_sec}/{frame_sec_all}")
        se = se+1
        ret1, frame = cap20.read()
        print(ret1)
        if ret1 == False:break
        face = cascade.detectMultiScale(frame)
        for x, y, w, h in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
        rects = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
        print('[hog] 検出された人数: {}'.format(len(rects)))
        ho = len(rects)
        if ho ==0:
            cv2.imwrite(f"Analysis_result_hog/none/Analysis_result{i}{a}{se}{noe}.jpg",frame)
            cv2.imwrite(f"video_picture/{v}.jpg",frame)
            img = cv2.imread(f"Analysis_result_hog/none/Analysis_result{i}{a}{se}{noe}.jpg")
            noe = noe+1
            video.write(img)
        if ho > 0:
            cascade = cv2.CascadeClassifier(XML_PATH)
            img1 = cv2.imread(PATHS[2])
            rects1 = cascade.detectMultiScale(img1, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
            y = len(rects1)
            if y == 0:
                print("[hog] 対象人物が検出されませんでした")
                break
            if y >0:
                print(f"[hog] 対象人物 {y}人")
                for i in range(ho):
                    print(f"[hog] 検出された {i+1}人目")
                    try:
                        for a in range(y):
                            print(f"[hog] 対象人物 {y}人目")
                            # step1 画像読み込みとコンバート
                            img_elon = frame
                            img_test = face_recognition.load_image_file(PATHS[2])
                            img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)
                            # step2 顔認証
                            face_loc = face_recognition.face_locations(img_elon)[i]
                            # 128次元の顔エンコーディングのリスト
                            encode_elon = face_recognition.face_encodings(img_elon,model="hog")[i]
                            cv2.rectangle(img_elon, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 255), 2)
                            face_loc_test = face_recognition.face_locations(img_test)[a]
                            encode_elon_test = face_recognition.face_encodings(img_test,model="hog")[a]

                            # print(encode_elon_test)
                            cv2.rectangle(img_test, (face_loc_test[3], face_loc_test[0]), (face_loc_test[1], face_loc_test[2]), (255, 0, 255), 2)

                            # ２つの画像が同一人物かの判定
                            results = face_recognition.compare_faces([encode_elon], encode_elon_test)
                            # 値が小さい程マッチしている
                            face_dis = face_recognition.face_distance([encode_elon], encode_elon_test)
                            print(f"[hog] {results, face_dis}")
                            p = 1 - face_dis[0]
                            probability = p*100
                            print(f"[hog] {probability}%")
                            if results == [False]:
                                res = "No match."
                            elif results == [True]:
                                if probability < 60:
                                    res = "little match"
                                elif probability > 60:
                                    res = "Match found."
                            text = f"{res}:{probability}%"
                            print(f"[hog]{text}")
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
                            com = f"video_picture/{v}.jpg"
                            back_im = im1.copy()
                            back_im.paste(im2, (590, 530))
                            back_im.save(completion, quality=95)
                            back_im.save(com, quality=95)
                            img = cv2.imread(f'Analysis_result_hog/Analysis_result{i}{a}{se}.jpg')
                            video.write(img)
                    except Exception as e:
                        v = v-1
                        print("[hog] error" + str(e))
    finally:
        v = v+1

video.release()

cv2.destroyAllWindows()
