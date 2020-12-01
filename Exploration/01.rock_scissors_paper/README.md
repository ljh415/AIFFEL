# 가위바위보 판별기

- 데이터 통합

  ```merge_data``` 를 활용해서 팀원들의 데이터 종합

- Dropout, 정규화을 사용하여서 오버피팅을 억제

- 기존의 MNIST 예제의 모델을 그대로 사용

  - 변경한 것
    - epoch : 10 -> 20
    - Dense : 32 -> 128
    - Dropout추가
    - 무작위로 5개의 데이터를 읽어들여서 predict 후 결과 시각화

  - test는 두가지 방식으로 확인

  1. 기존의 데이터셋을 8:1:1의 비율로 train, valid, test set으로 분류
  2. 새롭게 촬영한 데이터 각각 100장씩, 총 300장을 새롭게 test set 으로 생성

## 결과

1. accuracy : 0.9333 

2. accuracy : 0.6367



## 08.01 _ 추가

```review_rcp.ipynb``` 추가

- 복습하면서 slack에서 공유된 데이터를 사용해서 재학습 및 재평가

- 모델, 학습률(0.0005)은 그대로 사용

- 모델 summary

  ![image](https://user-images.githubusercontent.com/48716219/89104610-86607b00-d455-11ea-873d-8e890dd8a3bd.png)