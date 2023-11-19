# KT AIVLE School AI 개발자 3기 3차 미니 프로젝트

## 1. About

차량 공우 업체의 차량 파손 여부 분류 모델 제작

## 2. Attendees

팀 프로젝트 진행 (7명), 각자 개인적으로 EDA 및 모델 제작 후 결과 공유, 개선

## 3. Info

1. 차량 일부 사진 데이터를 인식 및 흠집을 찾는 Keras 기반 AI 모델 생성
2. Data Argumentation 및 Transfer Learning(VGG16) 적용
   - 이미지 변형 등을 통해 모델 성능 개선
3. 저시력자를 위한 이미지 기반 화폐 분류 모델 제작 및 튜닝 

### 코드

#### 사용 라이브러리

```python
import zipfile
import random, shutil
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report, confusion_matrix
```

#### 모델링
```python
# ## Sequential API
# 1. sesion clear
keras.backend.clear_session()


# 2. model structure
model = keras.models.Sequential()


# 3. model assembly
model.add(keras.layers.Input(shape=(280, 280, 3)))
#     # 1. 인풋 레이어
model.add(keras.layers.Conv2D(filters=32, kernel_size=(2, 2)))
#     # 2. Convolution : 필터수 32개, 사이즈(2, 2), same padding
model.add(keras.layers.Conv2D(filters=32,            # 새롭게 제작할 feature map의 수
                              kernel_size=(2, 2),    # 훑는 필터의 가로세로 사이즈
                              padding='same',        # 필터가 훑기 이전 사이즈를 유지하는 기법
                              strides=(1, 1),        # 기본적으로 한 칸씩 이동하며 훑음
                              activation='relu'))    # 주의!
#     # 3. BatchNormalization
model.add(keras.layers.BatchNormalization())
#     # 4. Convolution : 필터수 32개, 사이즈(2, 2), same padding
model.add(keras.layers.Conv2D(filters=32,            # 새롭게 제작할 feature map의 수
                              kernel_size=(2, 2),    # 훑는 필터의 가로세로 사이즈
                              padding='same',        # 필터가 훑기 이전 사이즈를 유지하는 기법
                              strides=(1, 1),        # 기본적으로 한 칸씩 이동하며 훑음
                              activation='relu'))    # 주의!
#     # 5. BatchNormalization
model.add(keras.layers.BatchNormalization())
#     # 6. MaxPooling : 사이즈(2,2) 스트라이드(2,2)
model.add(keras.layers.MaxPool2D(pool_size=(2,2), # pooling filter의 가로세로 사이즈
                                 strides=(2,2)))  # pooling filter가 어떻게 이동할 것인지
#     # 7. DropOut : 25% 비활성화
model.add(keras.layers.Dropout(0.25))
#     # 8. Convolution : 필터수 64개, 사이즈(2, 2), same padding
model.add(keras.layers.Conv2D(filters=64,            # 새롭게 제작할 feature map의 수
                              kernel_size=(2, 2),    # 훑는 필터의 가로세로 사이즈
                              padding='same',        # 필터가 훑기 이전 사이즈를 유지하는 기법
                              strides=(1, 1),        # 기본적으로 한 칸씩 이동하며 훑음
                              activation='relu'))    # 주의!
#     # 9. BatchNormalization
model.add(keras.layers.BatchNormalization())
#     # 10. Convolution : 필터수 64개, 사이즈(2, 2), same padding
model.add(keras.layers.Conv2D(filters=64,            # 새롭게 제작할 feature map의 수
                              kernel_size=(2, 2),    # 훑는 필터의 가로세로 사이즈
                              padding='same',        # 필터가 훑기 이전 사이즈를 유지하는 기법
                              strides=(1, 1),        # 기본적으로 한 칸씩 이동하며 훑음
                              activation='relu'))    # 주의!
#     # 11. BatchNormalization
model.add(keras.layers.BatchNormalization())
#     # 12. MaxPooling : 사이즈(2,2) 스트라이드(2,2)
model.add(keras.layers.MaxPool2D(pool_size=(2,2), strides=(2,2)))
#     # 13. DropOut : 25% 비활성화
model.add(keras.layers.Dropout(0.25))
#     # 14. Flatten
model.add(keras.layers.Flatten())
#     # 15. Fully Connected Layer : 노드 512개
model.add(keras.layers.Dense(1024, activation='relu'))
#     # 16. BatchNormalization
model.add(keras.layers.BatchNormalization())
#     # 17. 아웃풋 레이어
model.add(keras.layers.Dense(2, activation='softmax'))

# compile
model.compile(loss='binary_crossentropy', metrics=['accuracy'], optimizer='adam')

# summary
model.summary()
```

자세한 내용은 폴더 내 ipynb 파일에 있습니다.
