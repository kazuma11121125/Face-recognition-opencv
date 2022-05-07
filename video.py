import cv2
import face_recognition
from PIL import Image, ImageFont, ImageDraw
from moviepy.editor import *
import threading
ok = False

PATHS = [
    "vtest.mp4",#ビデオデータ
    "movie_resied.mp4",  # 解像度変更したビデオデータ
    "image/elon_test.jpg"  # 対象人物指定画像

]
global XML_PATH
XML_PATH = "haarcascade_frontalface_default.xml"

cascade = cv2.CascadeClassifier(XML_PATH)
img1 = cv2.imread(PATHS[2])
rects1 = cascade.detectMultiScale(img1, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
print('[hog] 検出された対象人物人数: {}'.format(len(rects1)))

cap9 = cv2.VideoCapture(PATHS[0])                  # 動画を読み込む
video_frame_count = cap9.get(cv2.CAP_PROP_FRAME_COUNT) # フレーム数を取得する
video_fps = cap9.get(cv2.CAP_PROP_FPS)                 # フレームレートを取得する
video_len_sec = video_frame_count / video_fps         # 長さ（秒）を計算する
print(video_len_sec)

DURATION = video_len_sec / 4

print(DURATION)

file_path = PATHS[0]

def one():
    start = 0    # 切り出し開始時刻。秒で表現
    end = DURATION    # 切り出し終了時刻。同じく秒で表現
    save_path = "movie_set/cat_vtest_1.mp4"    # 編集後のファイル保存先のパス
    video = VideoFileClip(file_path).subclip(start, end)    # ビデオのカット開始
    video.write_videofile(save_path,fps=10)
    cap = cv2.VideoCapture(save_path)
    # 動画のプロパティを取得
    fps = 10
    saizu = (720,480)
    # 書き出し設定
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    writer = cv2.VideoWriter("movie_set/cat_vtest_1_set.mp4",fourcc, fps, saizu)
    # 画質変換
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame,saizu)
        writer.write(frame)

    writer.release()
    cap.release()

def two():
    start = DURATION    # 切り出し開始時刻。秒で表現
    end = DURATION*2    # 切り出し終了時刻。同じく秒で表現
    save_path = "movie_set/cat_vtest_2.mp4"    # 編集後のファイル保存先のパス
    video = VideoFileClip(file_path).subclip(start, end)    # ビデオのカット開始
    video.write_videofile(save_path,fps=10)
    cap = cv2.VideoCapture(save_path)
    # 動画のプロパティを取得
    fps = 10
    saizu = (720,480)
    # 書き出し設定
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    writer = cv2.VideoWriter("movie_set/cat_vtest_2_set.mp4",fourcc, fps, saizu)
    # 画質変換
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame,saizu)
        writer.write(frame)

    writer.release()
    cap.release()

def three():
    start = DURATION*2    # 切り出し開始時刻。秒で表現
    end = DURATION*3    # 切り出し終了時刻。同じく秒で表現
    save_path = "movie_set/cat_vtest_3.mp4"    # 編集後のファイル保存先のパス
    video = VideoFileClip(file_path).subclip(start, end)    # ビデオのカット開始
    video.write_videofile(save_path,fps=10)
    cap = cv2.VideoCapture(save_path)
    # 動画のプロパティを取得
    fps = 10
    saizu = (720,480)
    # 書き出し設定
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    writer = cv2.VideoWriter("movie_set/cat_vtest_3_set.mp4",fourcc, fps, saizu)
    # 画質変換
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame,saizu)
        writer.write(frame)

    writer.release()
    cap.release()
def four():
    start = DURATION*3    # 切り出し開始時刻。秒で表現
    end = DURATION*4    # 切り出し終了時刻。同じく秒で表現
    save_path = "movie_set/cat_vtest_4.mp4"    # 編集後のファイル保存先のパス
    video = VideoFileClip(file_path).subclip(start, end)    # ビデオのカット開始
    video.write_videofile(save_path,fps=10)
    cap = cv2.VideoCapture(save_path)
    # 動画のプロパティを取得
    fps = 10
    saizu = (720,480)
    # 書き出し設定
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    writer = cv2.VideoWriter("movie_set/cat_vtest_4_set.mp4",fourcc, fps, saizu)
    # 画質変換
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame,saizu)
        writer.write(frame)

    writer.release()
    cap.release()

t1 = threading.Thread(target=one)
t2 = threading.Thread(target=two)
t3 = threading.Thread(target=three)
t4 = threading.Thread(target=four)

t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

cap1 = cv2.VideoCapture("movie_set/cat_vtest_1_set.mp4")  # ビデオ読み込み
if not cap1.isOpened():  
    print("1 正常に読み込めませんでした。")
    exit()

cap2 = cv2.VideoCapture("movie_set/cat_vtest_2_set.mp4")  # ビデオ読み込み
if not cap2.isOpened():  
    print("2 正常に読み込めませんでした。")
    exit()

cap3 = cv2.VideoCapture("movie_set/cat_vtest_3_set.mp4")  # ビデオ読み込み
if not cap3.isOpened():  
    print("3 正常に読み込めませんでした。")
    exit()

cap4 = cv2.VideoCapture("movie_set/cat_vtest_4_set.mp4")  # ビデオ読み込み
if not cap4.isOpened():  
    print("4 正常に読み込めませんでした。")
    exit()


global img_array,img_array_1,img_array_2,img_array_3,img_array_4
img_array = []
img_array_1 = []
img_array_2 = []
img_array_3 = []
img_array_4 = []

def one_set():
    se,noe = 0,0
    cascade = cv2.CascadeClassifier(XML_PATH)

    while (cap1.isOpened()):
        se = se+1
        ret1, frame = cap1.read()
        if ret1 == False:break
        face = cascade.detectMultiScale(frame)
        for x, y, w, h in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
        rects = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
        print('[hog:1]検出された人数: {}'.format(len(rects)))
        ho = len(rects)
        if ho ==0:
            cv2.imwrite(f"Analysis_result_hog/none/Analysis_result{se}{noe}_1.jpg",frame)
            img = cv2.imread(f"Analysis_result_hog/none/Analysis_result{se}{noe}_1.jpg")
            noe = noe+1
            img_array_1.append(img)
        if ho > 0:
            cascade = cv2.CascadeClassifier(XML_PATH)
            img1 = cv2.imread(PATHS[2])
            rects1 = cascade.detectMultiScale(img1, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
            y = len(rects1)
            if y == 0:
                print("[hog:1] 対象人物が検出されませんでした")
                break
            if y >0:
                print(f"[hog:1] 対象人物 {y}人")
                for i in range(ho):
                    print(f"[hog:1] 検出された {i+1}人目")
                    try:
                        for a in range(y):
                            print(f"[hog:1] 対象人物 {y}人目")
                            # step1 画像読み込みとコンバート
                            img_elon = frame
                            img_test = face_recognition.load_image_file(PATHS[2])
                            img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)
                            # step2 顔認証
                            face_loc = face_recognition.face_locations(img_elon)[i]
                            # 128次元の顔エンコーディングのリスト
                            encode_elon = face_recognition.face_encodings(img_elon)[i]
                            cv2.rectangle(img_elon, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 255), 2)
                            face_loc_test = face_recognition.face_locations(img_test)[a]
                            encode_elon_test = face_recognition.face_encodings(img_test)[a]

                            # print(encode_elon_test)
                            cv2.rectangle(img_test, (face_loc_test[3], face_loc_test[0]), (face_loc_test[1], face_loc_test[2]), (255, 0, 255), 2)

                            # ２つの画像が同一人物かの判定
                            results = face_recognition.compare_faces([encode_elon], encode_elon_test)
                            # 値が小さい程マッチしている
                            face_dis = face_recognition.face_distance([encode_elon], encode_elon_test)
                            print(f"[hog:1] {results, face_dis}")
                            p = 1 - face_dis[0]
                            probability = p*100
                            print(f"[hog:1] {probability}%")
                            if results == [False]:
                                res = "No match."
                            elif results == [True]:
                                if probability < 60:
                                    res = "little match"
                                elif probability > 60:
                                    res = "Match found."
                            text = f"{res}:{probability}%"
                            print(f"[hog:1]{text}")
                            resu = f'result_hog/{i}{a}{se}_1.jpg'
                            resu1 = f'result_hog/{i}{a}{se}_tm_1.jpg'
                            cv2.imwrite(resu, img_elon)
                            cv2.imwrite(resu1, img_test)
                            pic = Image.open(resu)
                            pic1 = Image.open(resu1)
                            img_resize = pic.resize((1000, 800))
                            img_resize1 = pic1.resize((400, 300))
                            reze = f'result_hog/{i}{a}{se}_ts_1.jpg'
                            reze1 = f'result_hog/{i}{a}{se}_tm_ts_1.jpg'
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
                            graw = f'result_hog/Analysis_result{i}{a}{se}_1.jpg'
                            photo_img.save(graw)
                            im1 = Image.open(graw)
                            im2 = Image.open(reze1)
                            completion = f'Analysis_result_hog/Analysis_result{i}{a}{se}_1.jpg'
                            back_im = im1.copy()
                            back_im.paste(im2, (590, 530))
                            back_im.save(completion, quality=95)

                            img = cv2.imread(f'Analysis_result_hog/Analysis_result{i}{a}{se}_1.jpg')
                            img_array_1.append(img)
                    except Exception as e:
                        try:
                            cv2.imwrite(f"Analysis_result_hog/none/Analysis_result{i}{a}{se}{noe}_1.jpg",frame)
                            img = cv2.imread(f"Analysis_result_hog/none/Analysis_result{i}{a}{se}{noe}_1.jpg")
                            img_array_1.append(img)
                            noe = noe+1
                        except:
                            print("[hog:1] error" + str(e))
                        print("[hog:1] error" + str(e))

def two_set():
    cascade = cv2.CascadeClassifier(XML_PATH)
    se,noe = 0,0
    while (cap2.isOpened()):
        se = se+1
        ret1, frame = cap2.read()
        if ret1 == False:break
        face = cascade.detectMultiScale(frame)
        for x, y, w, h in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
        rects = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
        print('[hog:2]検出された人数: {}'.format(len(rects)))
        ho = len(rects)
        if ho ==0:
            cv2.imwrite(f"Analysis_result_hog/none/Analysis_result{se}{noe}_2.jpg",frame)
            img = cv2.imread(f"Analysis_result_hog/none/Analysis_result{se}{noe}_2.jpg")
            noe = noe+1
            img_array_2.append(img)
        if ho > 0:
            cascade = cv2.CascadeClassifier(XML_PATH)
            img1 = cv2.imread(PATHS[2])
            rects1 = cascade.detectMultiScale(img1, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
            y = len(rects1)
            if y == 0:
                print("[hog:2] 対象人物が検出されませんでした")
                break
            if y >0:
                print(f"[hog:2] 対象人物 {y}人")
                for i in range(ho):
                    print(f"[hog:2] 検出された {i+1}人目")
                    try:
                        for a in range(y):
                            print(f"[hog:2] 対象人物 {y}人目")
                            # step1 画像読み込みとコンバート
                            img_elon = frame
                            img_test = face_recognition.load_image_file(PATHS[2])
                            img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)
                            # step2 顔認証
                            face_loc = face_recognition.face_locations(img_elon)[i]
                            # 128次元の顔エンコーディングのリスト
                            encode_elon = face_recognition.face_encodings(img_elon)[i]
                            cv2.rectangle(img_elon, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 255), 2)
                            face_loc_test = face_recognition.face_locations(img_test)[a]
                            encode_elon_test = face_recognition.face_encodings(img_test)[a]

                            # print(encode_elon_test)
                            cv2.rectangle(img_test, (face_loc_test[3], face_loc_test[0]), (face_loc_test[1], face_loc_test[2]), (255, 0, 255), 2)

                            # ２つの画像が同一人物かの判定
                            results = face_recognition.compare_faces([encode_elon], encode_elon_test)
                            # 値が小さい程マッチしている
                            face_dis = face_recognition.face_distance([encode_elon], encode_elon_test)
                            print(f"[hog:2] {results, face_dis}")
                            p = 1 - face_dis[0]
                            probability = p*100
                            print(f"[hog:2] {probability}%")
                            if results == [False]:
                                res = "No match."
                            elif results == [True]:
                                if probability < 60:
                                    res = "little match"
                                elif probability > 60:
                                    res = "Match found."
                            text = f"{res}:{probability}%"
                            print(f"[hog:2]{text}")
                            resu = f'result_hog/{i}{a}{se}_2.jpg'
                            resu1 = f'result_hog/{i}{a}{se}_tm_2.jpg'
                            cv2.imwrite(resu, img_elon)
                            cv2.imwrite(resu1, img_test)
                            pic = Image.open(resu)
                            pic1 = Image.open(resu1)
                            img_resize = pic.resize((1000, 800))
                            img_resize1 = pic1.resize((400, 300))
                            reze = f'result_hog/{i}{a}{se}_ts_2.jpg'
                            reze1 = f'result_hog/{i}{a}{se}_tm_ts_2.jpg'
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
                            graw = f'result_hog/Analysis_result{i}{a}{se}_2.jpg'
                            photo_img.save(graw)
                            im1 = Image.open(graw)
                            im2 = Image.open(reze1)
                            completion = f'Analysis_result_hog/Analysis_result{i}{a}{se}_2.jpg'
                            back_im = im1.copy()
                            back_im.paste(im2, (590, 530))
                            back_im.save(completion, quality=95)

                            img = cv2.imread(f'Analysis_result_hog/Analysis_result{i}{a}{se}_2.jpg')
                            img_array_2.append(img)
                    except Exception as e:
                        try:
                            cv2.imwrite(f"Analysis_result_hog/none/Analysis_result{i}{a}{se}{noe}_2.jpg",frame)
                            img = cv2.imread(f"Analysis_result_hog/none/Analysis_result{i}{a}{se}{noe}_2.jpg")
                            img_array_2.append(img)
                            noe = noe+1
                        except:
                            print("[hog] error" + str(e))
                        print("[hog] error" + str(e))
    
def three_set():
    cascade = cv2.CascadeClassifier(XML_PATH)
    se,noe = 0,0
    while (cap3.isOpened()):
        se = se+1
        ret1, frame = cap3.read()
        if ret1 == False:break
        face = cascade.detectMultiScale(frame)
        for x, y, w, h in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
        rects = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
        print('[hog:3]検出された人数: {}'.format(len(rects)))
        ho = len(rects)
        if ho ==0:
            cv2.imwrite(f"Analysis_result_hog/none/Analysis_result{se}{noe}_3.jpg",frame)
            img = cv2.imread(f"Analysis_result_hog/none/Analysis_result{se}{noe}_3.jpg")
            noe = noe+1
            img_array_3.append(img)
        if ho > 0:
            cascade = cv2.CascadeClassifier(XML_PATH)
            img1 = cv2.imread(PATHS[2])
            rects1 = cascade.detectMultiScale(img1, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
            y = len(rects1)
            if y == 0:
                print("[hog:3] 対象人物が検出されませんでした")
                break
            if y >0:
                print(f"[hog:3] 対象人物 {y}人")
                for i in range(ho):
                    print(f"[hog:3] 検出された {i+1}人目")
                    try:
                        for a in range(y):
                            print(f"[hog:3] 対象人物 {y}人目")
                            # step1 画像読み込みとコンバート
                            img_elon = frame
                            img_test = face_recognition.load_image_file(PATHS[2])
                            img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)
                            # step2 顔認証
                            face_loc = face_recognition.face_locations(img_elon)[i]
                            # 128次元の顔エンコーディングのリスト
                            encode_elon = face_recognition.face_encodings(img_elon)[i]
                            cv2.rectangle(img_elon, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 255), 2)
                            face_loc_test = face_recognition.face_locations(img_test)[a]
                            encode_elon_test = face_recognition.face_encodings(img_test)[a]

                            # print(encode_elon_test)
                            cv2.rectangle(img_test, (face_loc_test[3], face_loc_test[0]), (face_loc_test[1], face_loc_test[2]), (255, 0, 255), 2)

                            # ２つの画像が同一人物かの判定
                            results = face_recognition.compare_faces([encode_elon], encode_elon_test)
                            # 値が小さい程マッチしている
                            face_dis = face_recognition.face_distance([encode_elon], encode_elon_test)
                            print(f"[hog:3] {results, face_dis}")
                            p = 1 - face_dis[0]
                            probability = p*100
                            print(f"[hog:3] {probability}%")
                            if results == [False]:
                                res = "No match."
                            elif results == [True]:
                                if probability < 60:
                                    res = "little match"
                                elif probability > 60:
                                    res = "Match found."
                            text = f"{res}:{probability}%"
                            print(f"[hog:3]{text}")
                            resu = f'result_hog/{i}{a}{se}_3.jpg'
                            resu1 = f'result_hog/{i}{a}{se}_tm_3.jpg'
                            cv2.imwrite(resu, img_elon)
                            cv2.imwrite(resu1, img_test)
                            pic = Image.open(resu)
                            pic1 = Image.open(resu1)
                            img_resize = pic.resize((1000, 800))
                            img_resize1 = pic1.resize((400, 300))
                            reze = f'result_hog/{i}{a}{se}_ts_3.jpg'
                            reze1 = f'result_hog/{i}{a}{se}_tm_ts_3.jpg'
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
                            graw = f'result_hog/Analysis_result{i}{a}{se}_3.jpg'
                            photo_img.save(graw)
                            im1 = Image.open(graw)
                            im2 = Image.open(reze1)
                            completion = f'Analysis_result_hog/Analysis_result{i}{a}{se}_3.jpg'
                            back_im = im1.copy()
                            back_im.paste(im2, (590, 530))
                            back_im.save(completion, quality=95)

                            img = cv2.imread(f'Analysis_result_hog/Analysis_result{i}{a}{se}_3.jpg')
                            img_array_3.append(img)
                    except Exception as e:
                        try:
                            cv2.imwrite(f"Analysis_result_hog/none/Analysis_result{i}{a}{se}{noe}_3.jpg",frame)
                            img = cv2.imread(f"Analysis_result_hog/none/Analysis_result{i}{a}{se}{noe}_3.jpg")
                            img_array_3.append(img)
                            noe = noe+1
                        except:
                            print("[hog:3] error" + str(e))
                        print("[hog:3] error" + str(e))

def foure_set():
    se,noe = 0,0
    cascade = cv2.CascadeClassifier(XML_PATH)
    while (cap4.isOpened()):
        se = se+1
        ret1, frame = cap4.read()
        if ret1 == False:break
        face = cascade.detectMultiScale(frame)
        for x, y, w, h in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
        rects = cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
        print('[hog:4]検出された人数: {}'.format(len(rects)))
        ho = len(rects)
        if ho ==0:
            cv2.imwrite(f"Analysis_result_hog/none/Analysis_result{se}{noe}_4.jpg",frame)
            img = cv2.imread(f"Analysis_result_hog/none/Analysis_result{se}{noe}_4.jpg")
            noe = noe+1
            img_array_4.append(img)
        if ho > 0:
            cascade = cv2.CascadeClassifier(XML_PATH)
            img1 = cv2.imread(PATHS[2])
            rects1 = cascade.detectMultiScale(img1, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
            y = len(rects1)
            if y == 0:
                print("[hog:4] 対象人物が検出されませんでした")
                break
            if y >0:
                print(f"[hog:4] 対象人物 {y}人")
                for i in range(ho):
                    print(f"[hog:4] 検出された {i+1}人目")
                    try:
                        for a in range(y):
                            print(f"[hog:4] 対象人物 {y}人目")
                            # step1 画像読み込みとコンバート
                            img_elon = frame
                            img_test = face_recognition.load_image_file(PATHS[2])
                            img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)
                            # step2 顔認証
                            face_loc = face_recognition.face_locations(img_elon)[i]
                            # 128次元の顔エンコーディングのリスト
                            encode_elon = face_recognition.face_encodings(img_elon)[i]
                            cv2.rectangle(img_elon, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255, 0, 255), 2)
                            face_loc_test = face_recognition.face_locations(img_test)[a]
                            encode_elon_test = face_recognition.face_encodings(img_test)[a]

                            # print(encode_elon_test)
                            cv2.rectangle(img_test, (face_loc_test[3], face_loc_test[0]), (face_loc_test[1], face_loc_test[2]), (255, 0, 255), 2)

                            # ２つの画像が同一人物かの判定
                            results = face_recognition.compare_faces([encode_elon], encode_elon_test)
                            # 値が小さい程マッチしている
                            face_dis = face_recognition.face_distance([encode_elon], encode_elon_test)
                            print(f"[hog:4] {results, face_dis}")
                            p = 1 - face_dis[0]
                            probability = p*100
                            print(f"[hog:4] {probability}%")
                            if results == [False]:
                                res = "No match."
                            elif results == [True]:
                                if probability < 60:
                                    res = "little match"
                                elif probability > 60:
                                    res = "Match found."
                            text = f"{res}:{probability}%"
                            print(text)
                            resu = f'result_hog/{i}{a}{se}_4.jpg'
                            resu1 = f'result_hog/{i}{a}{se}_tm_4.jpg'
                            cv2.imwrite(resu, img_elon)
                            cv2.imwrite(resu1, img_test)
                            pic = Image.open(resu)
                            pic1 = Image.open(resu1)
                            img_resize = pic.resize((1000, 800))
                            img_resize1 = pic1.resize((400, 300))
                            reze = f'result_hog/{i}{a}{se}_ts_4.jpg'
                            reze1 = f'result_hog/{i}{a}{se}_tm_ts_4.jpg'
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
                            graw = f'result_hog/Analysis_result{i}{a}{se}_4.jpg'
                            photo_img.save(graw)
                            im1 = Image.open(graw)
                            im2 = Image.open(reze1)
                            completion = f'Analysis_result_hog/Analysis_result{i}{a}{se}_4.jpg'
                            back_im = im1.copy()
                            back_im.paste(im2, (590, 530))
                            back_im.save(completion, quality=95)

                            img = cv2.imread(f'Analysis_result_hog/Analysis_result{i}{a}{se}_4.jpg')
                            img_array_4.append(img)
                    except Exception as e:
                        try:
                            cv2.imwrite(f"Analysis_result_hog/none/Analysis_result{i}{a}{se}{noe}_4.jpg",frame)
                            img = cv2.imread(f"Analysis_result_hog/none/Analysis_result{i}{a}{se}{noe}_4.jpg")
                            img_array_4.append(img)
                            noe = noe+1
                        except:
                            print("[hog:4] error" + str(e))
                        print("[hog:4] error" + str(e))

t1 = threading.Thread(target=one_set)
t2 = threading.Thread(target=two_set)
t3 = threading.Thread(target=three_set)
t4 = threading.Thread(target=foure_set)

t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

img_array.extend(img_array_1)
img_array.extend(img_array_2)
img_array.extend(img_array_3)
img_array.extend(img_array_4)


name = 'Face recognition hog.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter(name,fourcc,10,(1000, 800))

for i in range(len(img_array)):
    video.write(img_array[i])

video.release()

cv2.destroyAllWindows()
