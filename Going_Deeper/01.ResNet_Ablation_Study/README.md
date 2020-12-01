# 결과 정리

- 이미지를 (224, 224)로 resize를 해주었지만 메모리 용량이 부족했다. 다음과 같은 방법으로 해결했다.

  1. `BATCH_SIZE`를 줄여준다 : 16까지 줄여준다.

  2. ```ds = ds.prefetch(tf.data.experimental.AUTOTUNE)``` 사용을 안한다.

     - prefetch를 하면 에폭이 끝나기 전에 메모리에 미리 데이터를 올려놓고 다음 에폭을 시작할 때 빠르게 진행하도록 해주는 것으로 알고 있다.
     - 이 기능을 사용하지 않고 커널이 죽는 현상을 막을 수 있었다.

  3. 중간중간에 `del`을 사용해서 메모리를 계속해서 정리해준다.

     

------

- `ResNet34` **vs** `PlainNet34` : Loss 값 변화  

  ​	![image](https://user-images.githubusercontent.com/48716219/96059954-23b24380-0eca-11eb-8b61-afc2e2bc7cb5.png)

  - PlainNet34의 경우 Loss 값의 변화를 보면 학습이 진행되지 않은 것을 볼 수 있다.

  - 그에 반해 ResNet34는 Loss가 안정적으로 감소하고 있는 그래프를 보여주고 있고, 학습이 진행되고 있음을 알 수 있다.

    

- `ResNet50` **vs** `PlainNet50` : Loss 값 변화  

  ​	![image](https://user-images.githubusercontent.com/48716219/96060594-e64eb580-0ecb-11eb-9080-667a93c20556.png)

  - `PlainNet50`의 그래프는 이전에 `PlainNet34`와 비교했을 때도 볼 수 있듯이 이전보다 그래프의 변동폭이 매우 작고 학습이 전혀 진행되지 않는 모습을 볼 수 있다.

  - `ResNet50`도 마찬가지로 `PlainNet50`과 비교를 하면 Loss가 감소하면서 안정적으로 학습이 진행됨을 확인 할 수 있다.

    

- `ResNet34` vs `ResNet50` : Validation Accurcay

  - 각각 `0.6927`과 `0.7194`의 score를 기록하였다.
  - 에폭이 10번밖에 수행밖에 안해서 그런지 크게 차이는 나지 않았다. 하지만 마지막 수치만 보았을 때는 `ResNet50`의 값이 더 높았고, 층을 더 깊게 쌓은 `ResNet50`의 경우에 Validation Accuracy가 안정적으로 증가하는 그림을 확인할 수 있었다.