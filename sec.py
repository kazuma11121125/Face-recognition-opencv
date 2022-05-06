import cv2
from moviepy.editor import *
import threading
PATHS = [
    "vtest.mp4",#ビデオデータ
    "movie_resied.mp4",  # 解像度変更したビデオデータ
    "image/elon_test.jpg"  # 対象人物指定画像

]
cap9 = cv2.VideoCapture(PATHS[1])                  # 動画を読み込む
video_frame_count = cap9.get(cv2.CAP_PROP_FRAME_COUNT) # フレーム数を取得する
video_fps = cap9.get(cv2.CAP_PROP_FPS)                 # フレームレートを取得する
video_len_sec = video_frame_count / video_fps         # 長さ（秒）を計算する
print(video_len_sec)

DURATION = video_len_sec / 4

print(DURATION)

file_path = PATHS[1]

def one():
    start = 0    # 切り出し開始時刻。秒で表現
    end = DURATION    # 切り出し終了時刻。同じく秒で表現
    save_path = "cat_vtest_1.mp4"    # 編集後のファイル保存先のパス
    video = VideoFileClip(file_path).subclip(start, end)    # ビデオのカット開始
    video.write_videofile(save_path,fps=10) 

def two():
    start = DURATION    # 切り出し開始時刻。秒で表現
    end = DURATION*2    # 切り出し終了時刻。同じく秒で表現
    save_path = "cat_vtest_2.mp4"    # 編集後のファイル保存先のパス
    video = VideoFileClip(file_path).subclip(start, end)    # ビデオのカット開始
    video.write_videofile(save_path,fps=10)

def three():
    start = DURATION*2    # 切り出し開始時刻。秒で表現
    end = DURATION*3    # 切り出し終了時刻。同じく秒で表現
    save_path = "cat_vtest_3.mp4"    # 編集後のファイル保存先のパス
    video = VideoFileClip(file_path).subclip(start, end)    # ビデオのカット開始
    video.write_videofile(save_path,fps=10)

def four():
    start = DURATION*3    # 切り出し開始時刻。秒で表現
    end = DURATION*4    # 切り出し終了時刻。同じく秒で表現
    save_path = "cat_vtest_4.mp4"    # 編集後のファイル保存先のパス
    video = VideoFileClip(file_path).subclip(start, end)    # ビデオのカット開始
    video.write_videofile(save_path,fps=10)

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
