

# Super Resolution



## 프로젝트 1 : 직접 고른 이미지로 SRGAN 실험

### 프로젝트 1-1

1. 적당한 해상도의 이미지를 불러온다
2. 이미지의 사이즈를 임의로 1/4로 줄인다.
3. 1/4로 줄인 이미지를 각각 Bicubic방식, SRGAN을 적용하여서 원본이미지와 함께 비교를 해본다.

- 사용한 Image의 Shape : (651, 500, 3)

  ![image](https://user-images.githubusercontent.com/48716219/96692680-4a3c1700-13c1-11eb-8375-173268764d55.png)

- 결과

  ![image](https://user-images.githubusercontent.com/48716219/96692459-03e6b800-13c1-11eb-94a0-6925c4a7b4b8.png)

### 프로젝트 1-2

1. 낮은 해상도의 이미지를 사용
2. 해당 이미지를 각각 Bicubic 방식, SRGAN을 적용한 결과물을 비교

- 사용한 Image의 Shape : (48, 48, 3)

  ![image](https://user-images.githubusercontent.com/48716219/96693043-bb7bca00-13c1-11eb-9c4b-8a6acbd5767e.png)

- 결과

  ![image](https://user-images.githubusercontent.com/48716219/96693098-cafb1300-13c1-11eb-8ec8-fa83c2a02866.png)

---

## 프로젝트 2 : GIF에 Super Resolution적용시키기

- [결과물 링크](https://drive.google.com/drive/folders/1cviZZTw1QC_4n3yzlOtVu3xOK8yST2mA?usp=sharing)
- '고해상도.gif'의 경우 ```ratio```값을 ```0.8```로 주어서 전체 길이의 80퍼센트는 SRGAN을 적용, 나머지 뒷부분은 bicubic 방법으로 보간하여서 ```resize```만 수행했다.
- '저해상도.gif'의 경우 처음부터 끝까지 SRGAN을 사용하지 않고 ```resize```만 적용하였다.
---
- SRGAN을 적용 시켰을 경우

    ![image](https://user-images.githubusercontent.com/48716219/96689798-d77d6c80-13bd-11eb-912b-e63314f7f01d.png)

- bicubic방식으로 resize만 적용했을 경우

    ![image](https://user-images.githubusercontent.com/48716219/96689888-f54ad180-13bd-11eb-8845-d0e51c1eb0c8.png)

- 위 두장의 사진처럼 SRGAN을 적용시켰을 경우 글자가 더 또렷하게 보이는 것을 확인 할 수 있다.