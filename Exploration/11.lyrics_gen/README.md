# LSTM을 활용한 가사 생성

- 가사 데이터를 학습
- (LSTM - BatchNormalization) X 2
###  목표 Loss (2.2 이하, epoch = 10 고정)

---

1. 20.09.09 : **2.2278**

   - 하이퍼 파라미터

     ```python
     num_words = 17000
     BATCH_SIZE = 256
     embedding_size = 2400
     hidden_size = 3000
     learning_rate = 0.0001
     ```

   - 파라미터수 (2억 2천8백만...)

     ![image](https://user-images.githubusercontent.com/48716219/92634317-11fbe000-f30f-11ea-9b96-a23c43369498.png)

   - 학습 진행

     ![image](https://user-images.githubusercontent.com/48716219/92634558-70c15980-f30f-11ea-814b-398f2cdbec93.png)