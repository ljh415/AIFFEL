# Seq2Seq를 활용한 번역기

1. 텍스트 전처리
    ```python
    sentence = re.sub(r"([?.!,¿])", r" \1 ", sentence)   # 1
    sentence = re.sub(r"[^a-zA-Z!.?]+", r" ", sentence)  # 2
    sentence = re.sub(r"\s+", r" ", sentence)            # 3
    
    sentence = sentence.lower()                          # 4
    ```
    - 1 : 구분자 앞뒤로 공백을 추가
    - 2 : 소문자, 대문자 알파벳, 구분자를 제외한 문자 공백으로 치환
    - 3 : 여러 공백문자들을 하나의 공백으로 치환
    - 4 : 문장을 소문자로 바꿔준다
    
2. 학습 진행
    ```
    Epoch 1/50
235/235 [==============================] - 9s 38ms/step - loss: 3.8890 - acc: 0.6101 - val_loss: 2.1206 - val_acc: 0.6128
Epoch 2/50
235/235 [==============================] - 7s 32ms/step - loss: 1.8707 - acc: 0.6770 - val_loss: 1.7175 - val_acc: 0.7273
    .
    .
    .
    Epoch 49/50
235/235 [==============================] - 8s 33ms/step - loss: 0.7837 - acc: 0.8629 - val_loss: 0.9349 - val_acc: 0.8434
Epoch 50/50
235/235 [==============================] - 8s 33ms/step - loss: 0.7795 - acc: 0.8639 - val_loss: 0.9354 - val_acc: 0.8445
    ```
    validation loss가 안정적으로 떨어지면서 0.9354까지 떨어지면서 학습 중간에 오르기 시작하는 현상(Overfitting)은 관찰되지 않았다.
    
3. 테스트용 디코더의 경우 input을 2개로 받아오면서 이전에 학습할때 사용한 디코더와는 구조가 다르다.
    - 원래 들어오는 input + input의 상태
    - 이전 시점에서 나오는 outputs과 그 상태