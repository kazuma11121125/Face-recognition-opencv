import cv2
import glob

def makevido():
    img_array = []
    for filename in sorted(glob.glob("Analysis_result_hog/*.jpg")):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    name = 'Face recognition.mp4'
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter(name,fourcc,10,size)

    for i in range(len(img_array)):
        video.write(img_array[i])
    video.release
    global ok
    ok = True

makevido()