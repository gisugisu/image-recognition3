# Opencvを用いて,漫画のキャラクターに近づける処理をする

## コードの説明
```python
if(a==0):
  gray[y+ey: y + ey + eh, x+ex: x + ex + ew] = cv2.resize(threegray_img,(ew,eh), interpolation = cv2.INTER_AREA)
```
ウインドウのトラックバーを０にした場合には,images.jpgを読み込み,グレースケール画像に変換したthree_imgを瞳認証で検出される範囲の大きさに画像をリサイズしてその範囲に貼り合わせる.このようにすることで,目の部分だけを３にすることが可能になる.  
ここで用いる3の画像では画像の境目が三値化処理をした時に周りの肌の色となじむように背景をグレーに,を黒にした画像を用いる.


```python
if(a==2):
  t = 0.5
  images1 = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
  images1=images1/255
  ret, images2 = cv2.threshold(images1, t, 1, cv2.THRESH_BINARY)
  images2=images2.astype('uint8')
  gray[y: y + h, x: x + w] *= cv2.resize(images2,(w,h), interpolation = cv2.INTER_AREA)
```
ウインドウのトラックバーを２にした場合には,眼鏡の画像images2.jpgを読み込みその画像をグレースケール化して,画像の画素値を255で割ることにより0~1に正規化する.そしてその画像を二値化する.このとき,眼鏡の画像は白か黒かなので適当にしきい値の値を0.5とした.  
0か1の二値化にすることで,掛け合わせた際に眼鏡の形の部分だけ黒になるので,上手く眼鏡がキャプチャー画像に貼り合わせられる.


## 実行結果
以下の動画はそれぞれ目を３にする動画と眼鏡をかける動画である.
- https://youtu.be/yXwdlBbQFIE  
- https://youtu.be/KvCsyPKursM


## 参考文献
-  Python, OpenCVで顔検出と瞳検出（顔認識、瞳認識)//https://note.nkmk.me/python-opencv-face-detection-haar-cascade/
- Github//https://github.com/opencv/opencv/tree/master/data/haarcascades
- 【Python/OpenCV】写真・画像を漫画風に加工//https://algorithm.joho.info/programming/python/opencv-manga-filter-py/
-  Python OpenCVの基礎 resieで画像サイズを変えてみる//http://peaceandhilightandpython.hatenablog.com/entry/2016/01/09/214333
