# KT AIVLE School AI 개발자 3기 5차 미니 프로젝트

## 1. About

VOC 제기 고객 해지 여부 예측 모델 제작 및 튜닝

## 2. Attendees

팀 프로젝트 진행 (7명), 각자 개인적으로 EDA 및 모델 제작 후 결과 공유, 개선

## 3. Info

통신사 VOC(Voice of Customer) 제기 고객이 해지할 것인지 여부를 예측하는 AI 모델 제작 및 튜닝 


사용한 라이브러리

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import *
from tensorflow.keras.backend import clear_session
from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Input, Dense, Concatenate, Dropout
from tensorflow.keras.activations import relu, softmax

from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.optimizers import Adam

from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import plot_model
# 후략
```

### 전처리 작업

#### 데이터 결측치 처리

1. 결측치가 절반 이상인 데이터 컬럼 제거

  ```python
  to_delete = []
for i in list(df1):
        if (df1.loc[df[i] == '_'].value_counts().sum())/len(df1[i])*100 > 50:
            to_delete.append(i)
to_delete

for col in to_delete:
    df1.drop(col, axis=1, inplace=True)
df1.head()

```

2. '_'로 설정되어 있는 값을 Null로 변경 후 최빈값/중앙값 둥으로 변경

```python
df1.replace('_', None, inplace=True)

most = df1['cust_clas_itg_cd'].value_counts().idxmax()
most


# # cust_clas_itg_cd 컬럼에 대한 값 분포 확인
df1['cust_clas_itg_cd'] = df1['cust_clas_itg_cd'].fillna(most)
print(df1['cust_clas_itg_cd'].value_counts())
```

```python
# 중앙값(median) 확인
med = df1['age_itg_cd'].median()
df1['age_itg_cd'] = df1['age_itg_cd'].fillna(med)

df1['cont_sttus_itg_cd'] = df1['cont_sttus_itg_cd'].fillna(df1['cont_sttus_itg_cd'].mode())
df1['cont_sttus_itg_cd'].value_counts()

df1['cust_dtl_ctg_itg_cd'] = df1['cust_dtl_ctg_itg_cd'].fillna(df1['cust_dtl_ctg_itg_cd'].mode())

df1['cust_dtl_ctg_itg_cd'].value_counts()
```

3. 라벨 인코딩 및 원핫 인코딩

```python
#cust_clas_itg_cd 컬럼에 대해 LabelEncoder를 적용
# LabelEncoder 임포트
from sklearn.preprocessing import LabelEncoder
# LabelEncoder

encoder = LabelEncoder()
for i in obj_list:
    df1[i] = encoder.fit_transform(df1[i].values)

df1
```

```python
# df1의 나머지 object 컬럼에 대해서 One-Hot-Encoding될수 있도록 Pandas의 get_dummies 함수를 적용
df1 = pd.get_dummies(df1)
df1.columns

df1 = pd.get_dummies(data=df1, columns=['cont_sttus_itg_cd', 'cust_dtl_ctg_itg_cd', 'trm_yn'], drop_first=True)
df1.head()
```

4. x, y 데이터 분리, 표준화 후 모델 생성 

```python
clear_session()

model = Sequential()

model.add(Input(shape=(x_train_s.shape[1])))

model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(32, activation='relu'))
model.add(Dense(2, activation='sigmoid'))

model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

model.summary()
```

이후 자세한 내용은 AI 5차 미니프로젝트_VOC.ipynb 파일에 있습니다.
