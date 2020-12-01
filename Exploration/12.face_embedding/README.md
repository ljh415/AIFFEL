# 얼굴 임베딩 벡터를 활용해서 닮은 연예인 얼굴 찾기



## 구성

- e12.py 

  - 함수가 선언되어 있음

- face_embedding.ipynb

  - main

- face_embedding_gui.ipynb

  - ```tkinter```활용 gui구현

  

## 기능

1. 입력 사진 및 연예인 사진에서 ```dlib```을 활용해서 얼굴을 인식, 따로 인식한 얼굴만 새로 저장한다.
2. 1번에서 수정한 얼굴사진만 가지고 와서 임베딩 벡터를 생성
   - 내 얼굴(입력 사진) 임베딩 벡터 생성
   - 연예인들의 얼굴 임베딩 벡터를 딕셔너리로 생성
   - 임베딕 벡터 딕셔러니에 처음에 만든 내 얼굴 임베딩 벡터 추가
3. 연예인들의 얼굴 임베딩 벡터와 비교, L2 Norm Distance를 활용
4. 상위 5명의 닮은 꼴을 출력, 가장 닮은 연예인의 얼굴과 내 얼굴을 ```matplotlib```을 사용해서 시각화
5. ```tkinter```를 활용, GUI환경 구현

   - 입력사진 선택

     ![image](https://user-images.githubusercontent.com/48716219/92770348-d4fa2100-f3d4-11ea-9c98-913b367fded6.png)

   - 출력화면

     ![Screenshot from 2020-09-11 02-15-13](https://user-images.githubusercontent.com/48716219/92770435-e8a58780-f3d4-11ea-931e-7db8e8167291.png)