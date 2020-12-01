# Transformer를 이용한 Chatbot

#### Transformer 논문 정리
[![Notion](https://img.shields.io/badge/Notion-white?style=flat-square&logo=Notion&logoColor=black&link=https://www.notion.so/c80299b18b934dfbabefab1227105370)](https://www.notion.so/Attention-is-All-You-Need-8d386fb5741f4d168f2e3703c15484e8)
---
1. 한국어 전처리
    - 기존의 영어와 구두점에 한글과 숫자도 추가했다.
    ```python
    # 전처리 함수
    def preprocess_sentence(sentence):
        sentence = sentence.lower().strip()

        # 단어와 구두점(punctuation) 사이의 거리를 만듭니다.
        # 예를 들어서 "I am a student." => "I am a student ."와 같이
        # student와 온점 사이에 거리를 만듭니다.
        sentence = re.sub(r"([?.!,])", r" \1 ", sentence)
        sentence = re.sub(r'[" "]+', " ", sentence)

        # 한글, 영어, 숫자, 4개의 구두점(? ! , .)을 제외한 모든 문자를 공백인 ' '로 대체
        sentence = re.sub(r"[^ㄱ-ㅣ가-힣a-zA-Z0-9?.!,]+", " ", sentence)
        sentence = sentence.strip()
        return sentence
    ```
    
 

2. 트랜스포머 모델의 하이퍼파라미터 변경

    - 원래 논문과 같이 ```NUM_LAYERS=2```, ```D_MODEL=512```로 사용
    - ```EPOCHS```도 기존에 20에서 50으로 늘려서 학습을 시켰다.
    - loss도 안정적으로 줄었고 accuracy도 꾸준히 증가하였다.  
    


3. 한국어 입력문장에 그럴듯한 답변을 리턴하였다.

    ![image](https://user-images.githubusercontent.com/48716219/97334479-221c4e80-18c0-11eb-8b94-3016a58b5bfe.png)
