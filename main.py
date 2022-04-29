import cv2
import face_recognition
import os
from PIL import Image, ImageFont, ImageDraw ,ImageFilter
from concurrent.futures import ThreadPoolExecutor
import threading
import sys

def cnn():
    XML_PATH = "haarcascade_frontalface_default.xml"
    INPUT_IMG_PATH = "image/elon.jpg"
    OUTPUT_IMG_PATH = "image/elon1.jpg"
    
    cascade = cv2.CascadeClassifier(XML_PATH)
    
    img = cv2.imread(INPUT_IMG_PATH)
    color = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    targets = cascade.detectMultiScale(color)
    
    for x, y, w, h in targets:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    cv2.imwrite(OUTPUT_IMG_PATH, img)
    im = Image.open(OUTPUT_IMG_PATH)
    im.show()

    img1 = cv2.imread('image/elon_test.jpg')
    color1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    
    targets = cascade.detectMultiScale(color1)
    
    for x, y, w, h in targets:
        cv2.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    cv2.imwrite('image/elon_test1.jpg', img1)
    im = Image.open('image/elon_test1.jpg')
    im.show()

    rects = cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
    rects1 = cascade.detectMultiScale(img1, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
    print('[cnn] 検出された人数\n: {}'.format(len(rects)))
    print('[cnn] 検出された対象人物人数\n: {}'.format(len(rects1)))

    h = len(rects)
    print(f"[cnn] {h}")
    y = len(rects1)
    print(f"[cnn] {y}")
    for i in range(h):
        print(f"[cnn] {i}")
        try:
            for a in range(y):
                # step1 画像読み込みとコンバート
                img_elon = face_recognition.load_image_file('image/elon.jpg')
                img_elon = cv2.cvtColor(img_elon, cv2.COLOR_BGR2RGB)
                img_test = face_recognition.load_image_file('image/elon_test.jpg')
                img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)
                img = cv2.imread('image/elon.jpg')

                # step2 顔認証
                face_loc = face_recognition.face_locations(img_elon,model="cnn")[i]
                # 128次元の顔エンコーディングのリスト
                encode_elon = face_recognition.face_encodings(img_elon)[i]
                cv2.rectangle(img_elon, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 255), 2)
                print(f"[cnn] {a}\n")
                face_loc_test = face_recognition.face_locations(img_test, model="cnn")[a]
                encode_elon_test = face_recognition.face_encodings(img_test)[a]

                # print(encode_elon_test)
                cv2.rectangle(img_test, (face_loc_test[3], face_loc_test[0]), (face_loc_test[1], face_loc_test[2]), (255, 0, 255), 2)

                # ２つの画像が同一人物かの判定
                results = face_recognition.compare_faces([encode_elon], encode_elon_test)
                # 値が小さい程マッチしている
                face_dis = face_recognition.face_distance([encode_elon], encode_elon_test)
                print(f"[cnn] {results, face_dis}\n")
                p = 1-face_dis[0]
                probability = p*100
                print(f"[cnn] {probability}\n")
                if results == [False]:
                    res = "No match."
                elif results == [True]:
                    if probability < 60:
                        res = "little match"
                    elif probability > 60:
                        res = "Match found."
                text = f"{res}:{probability}%"
                cv2.imwrite(f'result/{i}{a}.jpg', img_elon)
                cv2.imwrite(f'result/{i}{a}_tm.jpg', img_test)
                pic = Image.open(f'result/{i}{a}.jpg')
                pic1 = Image.open(f'result/{i}{a}_tm.jpg')
                img_resize = pic.resize((1000, 800))
                img_resize1 = pic1.resize((400, 300))
                img_resize.save(f'result/{i}{a}_ts.jpg')
                img_resize1.save(f'result/{i}{a}_tm_ts.jpg')

                fnt = ImageFont.truetype("arial.ttf", 60)
                # 画像ファイルを開く
                photo_img = Image.open(f'result/{i}{a}_ts.jpg')
                
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
                photo_img.save(f'result/Analysis_result{i}{a}.jpg')
                im1 = Image.open(f'result/Analysis_result{i}{a}.jpg')
                im2 = Image.open(f'result/{i}{a}_tm_ts.jpg')

                back_im = im1.copy()
                back_im.paste(im2, (590, 530))
                back_im.save(f'Analysis_result/Analysis_result{i}{a}.jpg', quality=95)
                
                if results == [True]:
                    if probability >60:
                        im = Image.open(f'Analysis_result/Analysis_result{i}{a}.jpg')
                        im.show()

        except Exception as e:
            print("[cnn] error" + str(e))

def hog():
    XML_PATH = "haarcascade_frontalface_default.xml"
    INPUT_IMG_PATH = "image/elon.jpg"
    
    cascade = cv2.CascadeClassifier(XML_PATH)
    
    img = cv2.imread(INPUT_IMG_PATH)

    img1 = cv2.imread('image/elon_test.jpg')

    rects = cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
    rects1 = cascade.detectMultiScale(img1, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
    print('[hog] 検出された人数: {}'.format(len(rects)))
    print('[hog] 検出された対象人物人数: {}'.format(len(rects1)))

    h = len(rects)
    print(f"[hog] {h}\n")
    y = len(rects1)
    print(f"[hog] {y}\n")
    for i in range(h):
        print(f"[hog] {i}\n")
        try:
            for a in range(y):
                # step1 画像読み込みとコンバート
                img_elon = face_recognition.load_image_file('image/elon.jpg')
                img_elon = cv2.cvtColor(img_elon, cv2.COLOR_BGR2RGB)
                img_test = face_recognition.load_image_file('image/elon_test.jpg')
                img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)
                img = cv2.imread('image/elon.jpg')

                # step2 顔認証
                face_loc = face_recognition.face_locations(img_elon)[i]
                # 128次元の顔エンコーディングのリスト
                encode_elon = face_recognition.face_encodings(img_elon)[i]
                cv2.rectangle(img_elon, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 255), 2)
                print(f"[hog] {a}\n")
                face_loc_test = face_recognition.face_locations(img_test)[a]
                encode_elon_test = face_recognition.face_encodings(img_test)[a]

                # print(encode_elon_test)
                cv2.rectangle(img_test, (face_loc_test[3], face_loc_test[0]), (face_loc_test[1], face_loc_test[2]), (255, 0, 255), 2)

                # ２つの画像が同一人物かの判定
                results = face_recognition.compare_faces([encode_elon], encode_elon_test)
                # 値が小さい程マッチしている
                face_dis = face_recognition.face_distance([encode_elon], encode_elon_test)
                print(f"[hog] {results, face_dis}\n")
                p = 1-face_dis[0]
                probability = p*100
                print(f"[hog] {probability}\n")
                if results == [False]:
                    res = "No match."
                elif results == [True]:
                    if probability < 60:
                        res = "little match"
                    elif probability > 60:
                        res = "Match found."
                text = f"{res}:{probability}%"
                cv2.imwrite(f'result_hog/{i}{a}.jpg', img_elon)
                cv2.imwrite(f'result_hog/{i}{a}_tm.jpg', img_test)
                pic = Image.open(f'result_hog/{i}{a}.jpg')
                pic1 = Image.open(f'result_hog/{i}{a}_tm.jpg')
                img_resize = pic.resize((1000, 800))
                img_resize1 = pic1.resize((400, 300))
                img_resize.save(f'result_hog/{i}{a}_ts.jpg')
                img_resize1.save(f'result_hog/{i}{a}_tm_ts.jpg')

                fnt = ImageFont.truetype("arial.ttf", 60)
                # 画像ファイルを開く
                photo_img = Image.open(f'result_hog/{i}{a}_ts.jpg')
                
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
                photo_img.save(f'result_hog/Analysis_result{i}{a}.jpg')
                im1 = Image.open(f'result_hog/Analysis_result{i}{a}.jpg')
                im2 = Image.open(f'result_hog/{i}{a}_tm_ts.jpg')

                back_im = im1.copy()
                back_im.paste(im2, (590, 530))
                back_im.save(f'Analysis_result_hog/Analysis_result{i}{a}.jpg', quality=95)
                
        except Exception as e:
            print("[hog] error" + str(e))
    
print("start.")

t1 = threading.Thread(target=cnn)
t2 = threading.Thread(target=hog)
t1.start()
t2.start()
t1.join()
t2.join()

print("end.")

sys.exit(0)
