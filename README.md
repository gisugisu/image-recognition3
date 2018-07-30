# Opencvを用いて,漫画のキャラクターに近づける処理をする

## コードの説明
```python
if(a==0):
  gray[y+ey: y + ey + eh, x+ex: x + ex + ew] = cv2.resize(threegray_img,(ew,eh), interpolation = cv2.INTER_AREA)
```



```python
t = 0.5
images1 = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
images1=images1/255
ret, images2 = cv2.threshold(images1, t, 1, cv2.THRESH_BINARY)
images2=images2.astype('uint8')
gray[y: y + h, x: x + w] *= cv2.resize(images2,(w,h), interpolation = cv2.INTER_AREA)
```
## 実行結果
- 


## 参考文献
- https://note.nkmk.me/python-opencv-face-detection-haar-cascade/
- https://algorithm.joho.info/programming/python/opencv-manga-camera-py/
