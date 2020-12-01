# 정리
---
1. KITTI 데이터셋 확인
    - ```semantic``` 디렉토리에 있는 segmentation 마스킹 이미지를 뜯어보면 다음과 같이 다양한 클래스를 확인할 수 있다.
    - 클래스 7의 경우 도로에 대한 정보를 담고 있는 것을 확인할 수 있다.  
        ![image](https://user-images.githubusercontent.com/48716219/98630838-5a5f6a80-235f-11eb-943d-2b2e90066916.png)  
        

<br>  

2. Augmentation 적용
    - albumentation 라이브러리 활용  
        ![image](https://user-images.githubusercontent.com/48716219/98632834-998fba80-2363-11eb-847a-acd1466f990f.png)  
    - augmentation 후, 원본 데이터와 segmentation 마스킹 이미지 시각화  
        ![image](https://user-images.githubusercontent.com/48716219/98636009-50426980-2369-11eb-9d50-6c92c993484f.png)

<br>  

3. U-Net++ 모델 구현
    - 기존의 U-Net 모델의 skip connectio이  DesnseNet의 Dense connectivity를 적용  
        ![image](https://user-images.githubusercontent.com/48716219/98207024-59ed5b00-1f7e-11eb-8bee-9daec27ddb62.png)
    -  ```build_UNet```, ```build_Unet_Plus``` 함수 선언, 각각 UNet과 UNet++모델을 반환  
    

<br>  

4. 결과 비교
    - U-Net : IoU = 0.777  
        ![image](https://user-images.githubusercontent.com/48716219/98636812-e4610080-236a-11eb-8553-a53abd117b67.png)
    - U-Net++ : IoU = 0.912  
        ![image](https://user-images.githubusercontent.com/48716219/98636993-2db15000-236b-11eb-8cc8-31fa08955a9a.png)
    - U-Net의 경우 생각보다 잘 찾은 것 같지만 인도 영역까지 segmentation을 했다. 그에 반해 U-Net++는 인도를 제외한 도로의 영역만 찾아냈고 실제로 IoU수치도 약 0.14정도 U-Net++의 성능이 더 좋게 나왔다.