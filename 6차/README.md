# KT AIVLE School AI 개발자 3기 6차 미니 프로젝트

### 1. About

Aivle School 지원 질문 분류 및 그에 해당하는 챗봇 만들기

### 2. Attendees

팀 프로젝트 진행 (7명), 각자 개인적으로 EDA 및 모델 제작 후 결과 공유, 개선

### 3. Info

#### 전처리 

1. 데이터 탐색
   
  - intent별 질문 개수 분포 확인하기
  - 질문별 무장길이의 분포 확인하기
  - 대화 유형(type)별 문장길이 분포 비교하기
  - 그 외 필요하다고 판단되는 부분에 대해 데이터를 탐색하고 분석하기
    
2. 전처리
  - 기본 전처리: 데이터를 불러온 후 다음의 전처리를 먼저 수행
    - 한글 컬럼 이름을 영어이름으로 변경
    - 두 데이터셋을 하나로 통합
    - intent 번호를 통합된 번호로 만들기
    - 일상대화와 Q&A 대화를 구분하는 한글자 컬럼 추가
  - 학습을 위한 전처리: 자연어 처리를 위한 전처리 수행
      - 형태소 분석기를 활용해 문장 어절들에 대해 형태소로 변환
    - 전처리 결과 저장
   
  환경 설정
  ```python
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

!pip install gensim==3.8.3
```

사용 라이브러리
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os
import matplotlib.font_manager as fm
import random
from sklearn.model_selection import train_test_split
```

자세한 내용은 1번 ipynb 파일에 있습니다.

#### 모델링


챗봇1. Word2Vec 임베딩 벡터 기반 머신러닝 분류 모델링

  - Word2Vec 모델을 만들고 임베딩 벡터를 생성합니다.
  - 임베딩 벡터를 이용하여 intent를 분류하는 모델링을 수행합니다.
  - 이때, LightGBM을 추천하지만, 다른 알고리즘을 이용할수 있습니다.
  - 예측된 intent의 답변 중 임의의 하나를 선정하여 출력합니다.
  
챗봇2. 단계별 모델링1

  1단계 : type(일상대화 0, 에이블스쿨Q&A 1) 분류 모델 만들기
  
    - Embedding + LSTM 모델링
  
  2단계 : 사전학습된 Word2Vec 모델을 로딩하여 train의 임베딩벡터 저장
  
    - 코사인 유사도로 intent 찾아 답변 출력
  
    - 새로운 문장의 임베딩벡터와 train의 임베딩 벡터간의 코사인 유사도 계산
  
    - 가장 유사도가 높은 질문의 intent를 찾아 답변 출력하기
  
챗봇3. 단계별 모델링2

  1단계 : 챗봇2의 1단계 모델을 그대로 활용
  
  2단계 : FastText 모델 생성하여 train의 임베딩벡터 저장
    
    - 코사인 유사도로 intent 찾아 답변 출력
    
    - 새로운 문장의 임베딩벡터와 train의 임베딩 벡터간의 코사인 유사도 계산
    
    - 가장 유사도가 높은 질문의 intent를 찾아 답변 출력하기
    
    - 챗봇3개에 대해서 몇가지 질문을 입력하고 각각의 답변을 비교해 봅시다.

#### 모델 예시

```python
import random

question = input("type your question here: ")

# 토큰화된 데이터로 word2vec 학습
question = [tokenize(get_tokenizer('mecab'), question)]

# 학습된 word2vec 모델로 데이터셋 구성
inputquestion = get_dataset(question, pre_wv_model, 200)

predicted_intent = model.predict(inputquestion)

# 예측된 intent에 해당하는 답변들의 리스트 가져오기
response_options = train[train['intent'] == predicted_intent[0]]['A'].tolist()

# 답변들 중에서 랜덤하게 하나 선택
response = random.choice(response_options)

print('답변: ', response)
# print(response_options)
```

```
type your question here: 예비군 훈련 참석시 불참으로 처리되나요?
답변:  단위기간(훈련시작일로부터 1개월) 내 80% 이상 출석해야 훈련수강 유지가 가능합니다. 
예를 들어, 훈련시작일로부터 1개월을 기준으로 1개월간의 훈련일수가 20일이라고 가정할 경우 16일 이상 출석하셔야 훈련수강을 계속 유지할 수 있습니다. 
결석 기준은 1. 당일 소정훈련시간의 50퍼센트 미만을 수강한 경우, 2. 지각, 조퇴 3회 누적 시, 결석 처리 됩니다. 
훈련 수준 유지를 위해 100% 출석을 권고 드립니다. 

K-Digital Training (K-DT) 규정상 월 1회 휴가 사용이 가능합니다.
```

자세한 내용은 2번 ipynb 파일에 있습니다.
