# kaggle_kakr_housing

---

- XGBoost사용

  ```python
  model = xgb.XGBRegressor(max_depth=10, n_estimators=1300, learning_rate=0.01, booster='dart', subsample=0.8, colsample_bytree=0.6, random_state=random_state)
  ```

  ---

- 08.21 / 22:36 제출
  
- score
  
  - private score : 110944.67572
  - public score : 107264.13139

---

- XGBoost사용

  ```python
  model = xgb.XGBRegressor(max_depth=9, n_estimators=2000, learning_rate=0.01, booster='dart', subsample=0.8, colsample_bytree=0.6, random_state=random_state)
  ```

  

- 08.24 / 12:30 제출

## 정리
- score
  - private score : 109886.29276
  - public score : 104244.58567

- Feature는 많이 건드리지 않고 거의 그대로 사용
- 4가지의 모델을 활용
    1. LightGBM
    2. GradientBoost
    3. XGBoost
    4. RandomForest
- 앙상블 시도 => 하지만 score는 낮아져서 제출물에는 사용하지 않음
- 다양한 하이퍼 파라미터를 사용
    - 모델 별로 수십번 돌아가면서 feature에서 모자른 부분을 하이퍼 파라미터 튜닝 시도
    - Grid Search 활용
    - 모델마다 요구하는 파라미터가 다 다르다.
        - ```max_depth```, ```learning_rate```, ```n_estimators```, ```num_leaves```, ```boosting_type``` 외에도 다양하게 존재
        
----
## 개선점
1. **Feature Engineering**
    - 캐글 뿐만 아니라 다양한 Competition에서 결국에는 결과물이 중요하다고는 하지만 꼼꼼한 EDA를 통한 데이터이해, EDA를 바탕으로한 Feature Engineering이 전체 결과물의 아마 반이상을 차지할 것이다.
    - 캐글에 공유되어 있는 고수님들의 코드를 따라치면서 공부를 해보는 방향으로 해본다.  
      
      
2. **앙상블 기법 활용**
    - Feature Engineering이 선행된다면 위에서 처럼 앙상블 기법을 해도 점수가 좀더 좋아지지 않을까 예상해본다.  
      
      
3. **Random Search 활용**
    - 일반적으로 Grid Search를 사용하면 최적의 파라미터를 한 번에 못 찾는다고 한다. 하지만 위에서 실습할 때 Grid Search를 수행하면서 게속 범위를 좁혀 나가면서 그러한 단점을 최소화시키려고 시도하였다.
    - 이러한 부분에서 시간을 많이 소비하게 되었는데 Random Search를 통해서 시간을 단축시킬 수 있는지, 정말로 Grid Search에서는 못찾았던 최적의 하이퍼파라미터를 찾을 수 있는지 확인해야 할 것이다.