# 결과
---
## 1. LR=0.0005, 0.2999
![image](https://user-images.githubusercontent.com/48716219/99338556-c2660180-28c7-11eb-8d33-54b1e4d8d6c8.png)

## 2. LR=0.0001, 0.2988
![image](https://user-images.githubusercontent.com/48716219/99338666-fa6d4480-28c7-11eb-89b7-62aeac9fcef6.png)

## 3. LR=0.0001, 0.3099
![image](https://user-images.githubusercontent.com/48716219/99363377-ff49ec80-28f7-11eb-8edc-c496ce459796.png)
```python
config = Config({"d_model": 256, "n_head": 4, "d_head": 64, "dropout": 0.2, "d_ff": 1024, "layernorm_epsilon": 0.001, "n_layer": 5, "n_seq": 384, "n_vocab": 0, "i_pad": 0})
config.n_vocab = len(vocab)
config.i_pad = vocab.pad_id()
config
```