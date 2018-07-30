import cv2
import numpy as np

def nothing(x):
    pass


face_cascade_path = 'haarcascade_frontalface_alt2.xml'
eye_cascade_path = 'haarcascade_eye2.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,800)

cv2.namedWindow('image')
cv2.createTrackbar('value','image',1,2,nothing)

a=0

# 漫画化フィルタ
def manga_filter(gray, screen, th1=60, th2=150):

    # グレースケール変換
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    # スクリーントーン画像を入力画像と同じ大きさにリサイズ
    screen = cv2.resize(screen,(gray.shape[1],gray.shape[0]))

    # Cannyアルゴリズムで輪郭検出し、色反転
    edge = 255 - cv2.Canny(gray, 80, 120)

    # 三値化
    gray[gray <= th1] = 0
    gray[gray >= th2] = 255
    gray[ np.where((gray > th1) & (gray < th2)) ] = screen[ np.where((gray > th1)&(gray < th2)) ]

    # 三値画像と輪郭画像を合成
    return cv2.bitwise_and(gray, edge)

while True:
    ret, img = cap.read()

    screen = cv2.imread("screen.jpg")
    three_img = cv2.imread("images.jpg")
    images=cv2.imread("images2.jpg")


    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threegray_img = cv2.cvtColor(three_img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for x, y, w, h in faces:
        face = img[y: y + h, x: x + w]
        face_gray = gray[y: y + h, x: x + w]
    for x ,y, w, h in faces:
        eyes = eye_cascade.detectMultiScale(face_gray)
        for (ex, ey, ew, eh) in eyes:
            a=cv2.getTrackbarPos('value','image')
            
            if(a==0):
                gray[y+ey: y + ey + eh, x+ex: x + ex + ew] = cv2.resize(threegray_img,(ew,eh), interpolation = cv2.INTER_AREA)

            if(a==2):
                t = 0.5
                images1 = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
                images1=images1/255
                ret, images2 = cv2.threshold(images1, t, 1, cv2.THRESH_BINARY)
                images2=images2.astype('uint8')
                gray[y: y + h, x: x + w] *= cv2.resize(images2,(w,h), interpolation = cv2.INTER_AREA)  
                
            # 画像の漫画化
            manga = manga_filter(gray, screen, 60, 150)


            cv2.imshow('image', manga)
    key = cv2.waitKey(10)
    if key == 27:  # ESCキーで終了
        break

cap.release()
cv2.destroyAllWindows()
