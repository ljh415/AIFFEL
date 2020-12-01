# Simple Segmentation


## Semantic Segmentation다루기
- DeepLab이라는 Segmentation 모델을 만들고 모델에 이미지를 입력
- 다음과 같은 클래스들이 있다.
    ```python
    LABEL_NAMES = [
    'background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus',
    'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike',
    'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tv'
    ]
    ```
- 이 중에서 강아지와 사람을 사용

## 배경변경
- 귀여운 강아지 사진
    ![03_doong](https://user-images.githubusercontent.com/48716219/93452193-188fe600-f913-11ea-8fde-4a2dd9755c03.jpg)  
      
<br>  
<br>  
- 1
    ![back](https://user-images.githubusercontent.com/48716219/93469002-ce1a6380-f92a-11ea-8c43-d726953444ae.jpeg)  
    
    ![image](https://user-images.githubusercontent.com/48716219/100718746-08aa7d00-33ff-11eb-92b4-81b9f446aab5.png)
- 2
    ![image](https://user-images.githubusercontent.com/48716219/100718861-2aa3ff80-33ff-11eb-8a4e-b64c0308ca7e.png)  

    ![back2](https://user-images.githubusercontent.com/48716219/93469015-d5da0800-f92a-11ea-9ddd-97b420d10b62.jpg)
