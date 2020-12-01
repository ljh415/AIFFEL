# pix2pix
---
1. Augmentation적용
    1. 두 이미지가 채널 축으로 연결
    2. 1의 결과에 50% 확률로 Reflection padding, constant padding이 30픽셀의 pad width만큼 적용
    3. 2의 결과에서 (256, 256, 6) 크기를 가진 이미지를 임의로 잘라낸다
    4. 3의 결과물을 50%의 확률로 가로 반전
    - 세로반전과 회전은 수행하지 않는다.
        
        - 일반적으로 도로사진은 그런 사진이 없기 때문에
    - 의문점
        - 이미지를 concat시키지 않고 짤릴 경우 기존에 이미지는 하얀색 배경이라서 하얀색이 있는게 문제가 되지 않지만, 도로 이미지의 경우 기존에 segmap에는 색칠이 다 되어 있기 때문에 흰색이 오히려 학습에 도움이 되지 않을 것 같다.

          ![image](https://user-images.githubusercontent.com/48716219/98461359-d5edda00-21ee-11eb-8c6c-6cd0876cd2e1.png)   

<br>  
        
2. U-Net generator, discriminator 사용
    - Generator부분에서 Encoder와 Decoder 사이를 skip connection으로 연결시켜주고 있다.
    - Concatenate layer를 활용, 기존 Encoder의 Output을 Decoder에 연결시키기 위해 역순으로 사용한다.
    - Encoder의 마지막 output은 따로 skip connection을 사용하지 않아도 Decoder에 연결되기 때문에 제외
    ```python
    def call(self, x):
        features = []
        for block in self.encode_blocks:
            x = block(x)
            features.append(x)
        
        features = features[:-1]
                    
        for block, feat in zip(self.decode_blocks, features[::-1]):
            x = block(x)
            x = layers.Concatenate()([x, feat])
        
        x = self.last_conv(x)
        return x
    ```

<br>  

3. 50 epoch 학습
    - 10 epoch에 비해서는 훨씬 좋아졌지만 여전히 조금 아쉬운 결과물이다.

      ![image](https://user-images.githubusercontent.com/48716219/98472478-af539180-2236-11eb-9b0b-1db9a7c06299.png)