# Face2Emoji


## 요약

1. 표정 데이터로 ```MobileNet``` 학습 : ```face2emoji.ipynb```

    - 데이터 받기 : [Facial Expression](https://www.kaggle.com/ahmedmoorsy/facial-expression)
    - 정규화하기 + Train, Validation 나누기 (train : 32298, eval :3589)
    - ```MobileNetV2```로 활용
    - ModelCheckpoint사용, val_categorical_accuracy가 가장 좋을 때를 기준으로 모델을 저장
        - 최고 socre : 50.571점
2. 학습된 모델을 TensorFlow.js 형식으로 변환
    - 위에서 저장한 가장 좋은 스코어의 모델로 TensorFlow.js를 활용
        ```bash
        $ pip install tensorflowjs
        $ cd '모델이 저장되어 있는 경로'
        $ tensorflowjs_converter --input_format=keras model.h5 model
        ```
3. 카메라에서 영상 가져오기 : ```index.html```
    - 웹캠에서 영상 가져오기
    - 캡쳐후 버튼 옆에 작게 사진을 표시
4. MobileNet 추론 결과 표시
    - ```<span>``` 태그를 활용, 추론 결과를 표시
    - 7가지 감정 표시
        - 🤬 : angry, 🤢 : disgust, 😱 : fear, 😄 : happy, 😲 : surprise, 😢 : sad, 😐 : neutral
5. github page에 HTML과 MobileNet 모델 배포하기
    
    - [https://ljh415.github.io/tfjs_mobile](https://ljh415.github.io/tfjs_mobile)

---

## 개선사항

1. 얼굴인식
    - 기존에 사용했던 얼굴인식 방법은 **```dlib```**, **```face_recognition```** 과 같은 라이브러리를 사용했다. 이미지에서부터 **'얼굴'을 찾아서** 랜드마크를 찾아서 스티커 이미지를 붙이거나 임베딩 벡터를 생성해서 닮은 꼴을 찾았다. 여기서 중요한 것은 사진에서부터 **얼굴**을 찾는 것이지만 여기서는 특별히 얼굴을 찾는 부분은 없다. 
    - 실제로 벽을 찍거나 <u>얼굴이 없는 사진</u>으로도 학습시킨 모델을 사용해서 이모지를 결과로 보여주지만 실제로 정답 score자체는 낮게 나올것이다. 하지만 사람의 얼굴을 인식해야 하는 것이기 때문에 위에서 언급한 방법을 사용하는 것이 더 좋을 것이라고 생각한다.
2. 모델 훈련 방식
    - ```weights='None'```으로 사용했지만 Classification을 수행하는 윗부분을 그대로 사용하고 있다.
    - **```include_top=False```**를 사용해서 Feature_extraction하는 모델의 구조만 가져오고 **Classification층을 새로 구성**해보는 것도 괜찮을 것 같다.
    - 하지만 기존의 데이터셋이 얼굴 사진으로부터 감정을 학습시키지 않았기 때문에 가중치는 ```ImageNet```으로 쓰기 보다는 ```None```으로 주는 것이 더 맞는 것 같다.
3. 뭐가 있을까...

---

