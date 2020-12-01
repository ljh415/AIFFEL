# Object Detection

- Keras RetinaNet사용 ([github](https://github.com/fizyr/keras-retinanet))

> 주의!
>
> TensorFlow 버전 2.3이상, keras 버전 2.4이상에서 동작한다.

## 정리

---
### 1. KITTI데이터셋 분석
- [KITTI](http://www.cvlibs.net/datasets/kitti/) 데이터셋은 자율주행을 위한 데이터셋이다.
- 2D object detection 뿐만 아니라 깊이까지 포함한 3D object detection 라벨 등을 제공한다
    - 다음은 제공하는 라벨 정보이다
    ![image](https://user-images.githubusercontent.com/48716219/97407066-7dd8ed00-193d-11eb-9518-0d69ff24892a.png)
- 여기서는 ```tensorflow_dataset```을 활용해서 데이터를 가져온다.
    - 처음 설치할 경우 11GB가 넘어가는 대용량의 데이터셋이기 때문에 매우 오래걸린다.
- ```tensorflow_dataset```에서 ```ds_train.take(1)```데이터를 가져오고 확인해보면 xml형식(key:value)의 ```annotation``` 정보를 확인할 수 있다.
    - 다양한 ```annotation```정보 중에서 여기선 bbox에 대한 정보를 사용할 것이고 4개의 값이 담겨 있다. ( ```left```, ```top```, ```right```, ```bottom``` 의 pixel 정보)이다.

<br>  

### 2. 결과 시각화
- 다음의 두가지 조건으로 Go, Stop을 정한다.
    1. 사람이 한 명 이상 있는 경우
    2. 차량의 크기(width or height)가 300px이상인 경우
- ```model.predict_on_batch```로 학습시킨 모델을 사용해서 입력 이미지에서 detection을 수행하고 물체를 탐지하면 ```boxes```, ```scores```, ```labels```의 3가지 변수를 반환하게 된다.
    - ```self_drive_assist``` 함수 : ```result```의 default값을 ```'Go'```로 하여서 이미지에서 물체가 탐지되지 않으면 장애물이 없다는 것으로 인식하고 그대로 ```'Go'```를 반환하도록 한다.
- ```boxes``` 변수에는 총 4개의 수가 담기게 된다. 이를 활용해서 ```width```와 ```height```를 구한다.
    - ```width = boxes[2] - boxes[0]```
    - ```height = boxes[3] - boxes[1]```
- ```labels```변수에 담기는 정보 중에서 1이 담겨 있을 경우, 객체 인식에서 '사람'을 인식한 것으로 알 수 있다.

<br>  

### 3. 수행결과
- 총 10개의 사진 중에서 9개의 사진에 대해서 맞추었고 90퍼센트의 정확도를 보여주었다.
