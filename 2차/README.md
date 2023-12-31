# KT AIVLE School AI 개발자 3기 2차 미니 프로젝트

## 1. About

서울시 생활정보를 기반으로 한 대중교통 수요분석 EDA

## 2. Attendees

팀 프로젝트 진행 (7명), 각자 개인적으로 EDA 진행 후 결과 공유

## 3. Info

1. 데이터 불러오기
2. 기본정보 확인 및 결측치, 이상치 제거
3. 각 변수별로 시각화 및 데이터 분포 확인 (Seaborn, Matplotlib 활용)
4. 분석 내용
   - 서울시 미세먼지 데이터 분석
   - 분석 및 정제한 데이터로 LinearRegression, RandomForest, GradientBoosting 이용해 특정 기간의 미세먼지 예측 후 모델 최적화 진행

### 사용한 라이브러리

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

### 데이터 형

| 지점 | 지점명 | 일시                | 기온(°C) | 기온 QC플래그 | 강수량(mm) | 강수량 QC플래그 | 풍속(m/s) | 풍속 QC플래그 | 풍향(16방위) | ... | 최저운고(100m) | 시정(10m) | 지면상태(지면상태코드) | 현상번호(국내식) | 지면온도(°C) | 지면온도 QC플래그 | 5cm 지중온도(°C) | 10cm 지중온도(°C) | 20cm 지중온도(°C) | 30cm 지중온도(°C) |
|------|--------|---------------------|----------|--------------|------------|--------------|------------|--------------|--------------|-----|----------------|-----------|---------------------|----------------|--------------|----------------|------------------|------------------|------------------|------------------|
| 108  | 서울   | 2021-01-01 01:00    | -8.7     | NaN          | NaN        | NaN          | 2.4        | NaN          | 270.0        | ... | NaN            | 2000      | NaN                 | NaN            | -6.9         | NaN            | -1.0             | -0.8             | 0.3              | 1.6              |
| 108  | 서울   | 2021-01-01 02:00    | -9.1     | NaN          | NaN        | NaN          | 1.6        | NaN          | 270.0        | ... | NaN            | 2000      | NaN                 | NaN            | -7.1         | NaN            | -1.1             | -0.8             | 0.3              | 1.6              |
| 108  | 서울   | 2021-01-01 03:00    | -9.3     | NaN          | NaN        | NaN          | 1.1        | NaN          | 250.0        | ... | NaN            | 2000      | NaN                 | NaN            | -7.3         | NaN            | -1.2             | -0.9             | 0.3              | 1.6              |
| 108  | 서울   | 2021-01-01 04:00    | -9.3     | NaN          | NaN        | NaN          | 0.3        | NaN          | 0.0          | ... | NaN            | 2000      | NaN                 | NaN            | -7.5         | NaN            | -1.3             | -1.0             | 0.2              | 1.5              |
| 108  | 서울   | 2021-01-01 05:00    | -9.7     | NaN          | NaN        | NaN          | 1.9        | NaN          | 20.0         | ... | NaN            | 2000      | NaN                 | NaN            | -7.6         | NaN            | -1.3             | -1.0             | 0.2              | 1.5              |

### 시각화

```python
air_21[['PM10','PM25']].plot.line(figsize=(20,8))

```

<img src="https://raw.githubusercontent.com/PhoneticsBug/ktAivle/main/2%EC%B0%A8/img1.png">

#### 상세한 내용 및 코드는 디렉토리 내 ipynb 파일에 있습니다.
