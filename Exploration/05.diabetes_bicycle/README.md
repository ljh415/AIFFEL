# Exploration 5 (Regression)



## Regression 문제

1. 당뇨병 예측
    - ```Learning Rate``` : ```0.1```
    - ```loss``` : ```MSE```
    - ```iteration``` **2851회** 부터 loss값은 3000이하로 떨어짐
    - **test데이터에 대한 성능 : 2870.6623956787585**
    - 예측 데이터 시각화
        ![image](https://user-images.githubusercontent.com/48716219/89889035-fb794080-dc0b-11ea-9a72-8f8cdbb48c78.png)  
    <br>  
    <br>
    
2. 자전거 타기

    https://www.kaggle.com/c/bike-sharing-demand

    - 학습 데이터 별 RMSE값
        1. 요일, hour, weather
            - ```RMSE``` : 155.2688 
        2. 요일, hour, weather, tmp
            - ```RMSE``` : 155.2688 
        3. 요일, hour, weather, humidity
            - ```RMSE``` : 163.2827 
        4. 요일, hour, weather, humidity, temp
            - ```RMSE``` : 151.4418 
        5. 요일, hour, weather, humidity, temp, atemp, season
            - ```RMSE``` : **149.6252**  
    <br>
    - 5번째 학습데이터에 대한 예측 결과 데이터 시각화
        1. x축 : X 데이터 중 temp데이터 / y축 : count
            ![image](https://user-images.githubusercontent.com/48716219/89889645-f4066700-dc0c-11ea-92f9-5c284e440400.png)
        
        2. x축 : X 데이터 중 humidity데이터 / y축 : count
            ![image](https://user-images.githubusercontent.com/48716219/89889666-fe286580-dc0c-11ea-8d70-6895d73fd91a.png)