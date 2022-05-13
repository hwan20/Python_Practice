#https://cafe.daum.net/flowlife/SBU0/15
#데이터 분포의 치우침은 부스팅이 줄일 수 있고, 과적합 문제의 해결은 배깅만이 할 수 있다. 
#배깅은 병렬적으로 모델을 만들지만, 부스팅은 하나의 모델을 만들어 그 결과로 다른 모델을 만들어 나가는데 즉 순차적으로 모델을 완성시켜 나간다. 
#성능면에서는 부스팅이 우수하나, 과적합이 우려스럽다면 배깅을 사용하는 좋을 것 같다.

#배깅(Bagging): boostrap aggregating의 약어로 데이터를 가방(bag)에 쓸어 담아 복원 추출하여 여러 개의 표본을 만들어
#이를 기반으로 각각의 모델을 개발한 후에 결과를 하나로 합쳐 하나의 모델을 만들어 내는 것이다.
#배깅을 통해서 얻을 수 있는 효과는 '알고리즘의 안정성'이다. 
#대표적인 알고리즘에는 DecisionTree를 여러 개 나열시켜 사용하는 Random Forest 가 있다. 

#부스팅(Boosting):오분류 개체들에 가중치를 적용하여 새로운 분류 규칙 생성 반복 기반 최종 예측 모형 생성.
#Boosting이란 약한 분류기를 결합하여 강한 분류기를 만드는 과정이다. 
#분류기 A, B, C 가 있고, 각각의 0.3 정도의 accuracy를 보여준다고 하자. 
#A, B, C를 결합하여 더 높은 정확도, 예를 들어 0.7 정도의 accuracy를 얻는 게 앙상블 알고리즘의 기본 원리다. 
#Boosting은 이 과정을 순차적으로 실행한다.
#A 분류기를 만든 후, 그 정보를 바탕으로 B 분류기를 만들고, 다시 그 정보를 바탕으로 C 분류기를 만든다. 
#그리고 최종적으로 만들어진 분류기들을 모두 결합하여 최종 모델을 만드는 것이 Boosting의 원리다. 
#최근에는 XGBoost가 인기 있다


#XGBoost는 Gradient Boosting 알고리즘을 분산 환경에서도 실행할 수 있도록 구현해 놓은 라이브러리로
#Regression, Classification 문제를 모두 지원하며, 성능과 자원 효율이 좋아서 인기 있는 알고리즘이다.
#RandomForest와 마찬가지로 XGBoost는 여러 개의 Decision Tree를 조합해서 사용하는 Ensemble 알고리즘이다.

#XGBoost를 사용하기 위해서는 새로 깔아야함
#pip install xgboost
#pip install lightgbm


#brest_cancer dataset 사용

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer #sklearn에 기본적으로 깔려있는 테스트용 데이터
from sklearn.model_selection import train_test_split
from sklearn import metrics
import xgboost as xgb
from xgboost import plot_importance
from lightgbm import LGBMClassifier 
#XG부스트보다 연산량이 적음 데이터 양이 많아야됨 데이터 양이 적으면 성능이 떨어짐 - 데이터 양이 적으면 과적합이 발생함
import matplotlib.pyplot as plt

dataset = load_breast_cancer()
x_feature =dataset.data
#print(dataset.keys())
y_label = dataset.target
#print(dataset.feature_names)

cancer_df = pd.DataFrame(data = x_feature, columns = dataset.feature_names)
pd.set_option('max_columns', None)
print(cancer_df.head(2), cancer_df.shape) #(569, 30)
print(dataset.target_names) #['malignant' 'benign']
 
print(np.sum(y_label==0)) #malignant(악성) : 212 
print(np.sum(y_label==1)) #benign(양성) : 357

x_train, x_test, y_train, y_test = train_test_split(x_feature, y_label, test_size = 0.2, random_state = 12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(455, 30) (114, 30) (455,) (114,)

model = xgb.XGBClassifier(booster='gbtree', max_depth = 6, n_estimators = 500).fit(x_train, y_train)
#max_depth과적합 방지
#n_estimators = 500, tree를 500개 사용
#model = LGBMClassifier(booster='gbtree', max_depth = 6, n_estimators = 500).fit(x_train, y_train)
#좀 더 정확함
#XGBClassifier 대신에 LGBMClassifier 사용 가능
print(model)
pred = model.predict(x_test)
print('예측값 : ', pred[:10]) #[0 1 1 1 1 1 1 1 1 0]
print('실제값 : ', y_test[:10]) #[0 1 1 1 1 1 0 1 1 0]
print('분류 정확도 : ', metrics.accuracy_score(y_test, pred)) #0.9473
print('분류 보고서 : ', metrics.classification_report(y_test, pred))
#macro avg       0.95      0.94      
#weighted avg       0.95      0.95
#차이가 얼마 없어 좋은 결과이다

#시각화
fig, ax = plt.subplots(figsize = (10, 12))
plot_importance(model, ax = ax)
plt.show()

