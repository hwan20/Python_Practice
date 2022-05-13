#[XGBoost 문제] 
#kaggle.com이 제공하는 'glass datasets'
#유리 식별 데이터베이스로 여러 가지 특징들에 의해 7가지의 label(Type)로 분리된다.
#RI    Na    Mg    Al    Si    K    Ca    Ba    Fe    
#glass.csv 파일을 읽어 분류 작업을 수행하시오.

from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import numpy as np
from xgboost import plot_importance
import xgboost as xgb
import matplotlib.pyplot as plt

data = pd.read_csv('../testdata/glass.csv')

#print(xgb.__version__) #1.6.1
print(data.head(10), data.shape) #(214, 10)

print(data.keys()) #['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']
print(data.isnull().any()) #null값 없음

data_x = data.drop(['Type'], axis=1) #Type 칼럼을 제외한 나머지 칼럼 독립변수로 사용
data_y = data.Type

print(data_y.unique()) #[1 2 3 5 6 7]
print(data_x.columns) #['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']



from sklearn.preprocessing import LabelEncoder
lab = LabelEncoder()
data_y = pd.Series(lab.fit_transform(data_y))
print(data_y.head(), type(data_y)) #dtype: int64 <class 'pandas.core.series.Series'>
print(set(data_y)) #{0, 1, 2, 3, 4, 5}

#ValueError: Invalid classes inferred from unique values of `y`.  Expected: [0 1 2 3 4 5], got [1 2 3 5 6 7]
#unique값이 중간에 4가 빠지면서 순차적으로 되지가 않아 오류가 남. 
#방법은 2가지
#1) xgboost의 버전을 내리기 - 버전을 낮추면 다른 것과 연동이 안 맞을 수가 있어서 추천X
#2) unique값을 더미로 시스템이 원하는 순차적인 값으로 바꿔주기 [1 2 3 5 6 7] -> [0 1 2 3 4 5]
#방법 2번을 사용하기 위해 LabelEncoder를 사용해서 [1 2 3 5 6 7]을 [0 1 2 3 4 5]로 바꿔줌

x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size = 0.3, random_state = 12) #독립변수, 종속변수 순
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(149, 9) (65, 9) (149,) (65,)

model = xgb.XGBClassifier(booster='gbtree', max_depth = 6, n_estimators = 500).fit(x_train, y_train)
model.fit(x_train, y_train)
pred = model.predict(x_test)

print('예측값 : ', pred[:10]) #[1 1 4 0 5 1 2 5 0 0]
print('실제값 : ', np.array(y_test[:10])) #[1 1 4 0 5 4 2 5 0 0]
print('분류 정확도 : ', metrics.accuracy_score(y_test, pred)) #0.8
print('분류 보고서 : ', metrics.classification_report(y_test, pred))

from xgboost import plot_importance
plot_importance(model)
plt.show()
