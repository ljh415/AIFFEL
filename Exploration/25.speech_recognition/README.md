# 정리

1. Spectrogram 시각화

   ​    \- 1차원의 waveform 데이터를 2차원의 Spectrogram으로 변환시켰다.  

   ​        ![image](https://user-images.githubusercontent.com/48716219/98951535-b849a900-253d-11eb-8f67-bd838a5a1b45.png)



2. 두 가지 모델로 학습을 시켰다.

   ​    - Skip Connection이 없는 모델

   ​    - Skip Connection이 있는 모델

   ​    - 두 모델의 accuracy는 각각 ```0.9667```, ```0.9716```으로 Skip Connection을 사용한 모델이 ```0.005```정도 더 정확하게 나왔다.



3. 학습 진행

   ​    - Skip Connection 사용 X  

   ​        ![image](https://user-images.githubusercontent.com/48716219/98952526-e8457c00-253e-11eb-8142-6db4176147de.png)

   ​    - Skip Connection 사용  

   ​        ![image](https://user-images.githubusercontent.com/48716219/98952636-06ab7780-253f-11eb-8b0e-9b17703612b9.png)

   

   ​    - 기존의 1차원의 waveform을 학습시키던 모델의 Conv1D layer들을 Conv2D layer로 변경을 해주었다.

   ​    - 모델에 데이터를 넣기 위해서 채널을 추가해주었다.

   ​        ```python

   ​        a.shape

   ​        \>>> (130, 126)

   ​        a = a[:,:,np.newaxis]

   ​        a.shape

   ​        \>>> (130, 126, 1)

   ​        a = a.squeeze()

   ​        a.shape

   ​        \>>> (130, 126)

   ​        ```

   > 인위적으로 추가한 채널의 경우 ```np.squeeze```를 수행하여 채널의 차원을 없애고 ```Conv1D```로 학습해도 학습은 정상적으로 진행되었다.