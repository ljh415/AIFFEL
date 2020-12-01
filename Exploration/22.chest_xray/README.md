# Chest X-ray
---
1. 학습 결과 시각화 부분을 보면 Accuracy는 상승하고 Loss는 가끔 튀는 부분이 있지만 0에 수렴하는 모습을 볼 수 있다.
2. 성능향상을 위한 시도
    - Augmentation을 수행했을 때, 기존에 Augmentation을 적용하지 않았을 때보다 Accuracy가 10정도 줄어드는 것을 확인할 수 있었다.
    - 다음과 같은 방식으로 Accuracy를 **85**까지 올릴 수 있었다.
        - input층 이후이 있던 일반 Conv2D layer를 Separable Conv2D layer로 변경하였다.
        - 기존에 conv_block(32), conv_block(64), conv_block(128), <u>Dropout(0.2)</u>, conv_block(256), <u>Dropout(0.2)</u>
            - conv_block(32), conv_block(64), **conv_block(64)**, <u>Dropout(0.2)</u>, conv_block(128), <u>Dropout(0.2)</u>, **BatchNorm()**, conv_block(256), <u>Dropout(0.2)</u>, **BatchNorm()**
        - conv_block(64)를 하나 추가하였고 뒷단에 BatchNorm층을 추가해주었다.
3. 개선점
    - 기존의 augmentation을 수행했을 때 왜 정확도가 더 낮아질까 생각을 해보았다.
    - 원래 데이터는 정상 사진과 폐렴 사진에 대한 데이터 비가 1:3으로 정상 데이터가 많이 부족했다.
    - 하지만 이상태에서 Augmentation을 수행하게 될 경우 imbalance는 더 심해질 것으로 생각했고 그래서 정확도가 더 낮게 나온 것이 아닐까 생각을 했다.
    - 하지만 여기서 수행한 Augmentation은 이후에 class weight로 조정을 해주었지만 다른 방법으로 생각해 본것은 처음에 데이터셋을 train, valid 데이터셋을 만들기 전에 train데이터에 대해서만 좌우반전 Augmentation을 수행한다면 imbalance가 줄어들 것이고 그 상태로 train, valid로 나눠주는 것이 좋지 않을까 생각을 해보았다.