#[로지스틱 분류분석 문제2] 
#게임, TV 시청 데이터로 안경 착용 유무를 분류하시오.
#안경 : 값0(착용X), 값1(착용O)
#예제 파일 : https://github.com/pykwon  ==>  bodycheck.csv
#새로운 데이터(키보드로 입력)로 분류 확인. 스케일링X

from sklearn.model_selection import train_test_split
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

url = "https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/bodycheck.csv"

df = pd.read_csv(url)
#print(df)
df = df[['게임', 'TV시청', '안경유무']]
print(df)

arr = df.values
#print(arr)
x = arr[:, 0:2] #matrix
print(x[:3], x.shape)
#print(x)

y = arr[:, 2] #vector
print(y[:3], y.shape)
print()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)





model1 = LogisticRegression(C = 1, random_state = 0)
model1.fit(x_train, y_train)
y_pred1 = model1.predict(x_test)
print('예측값 : ', model1.predict(x_test))
print('실제값 : ', y_test)
print('분류 정확도 1 : %.5f' %accuracy_score(y_test, y_pred1))



print('--------------------------------')


model2 = LogisticRegression(C = 0.01, random_state = 0)
model2.fit(x_train, y_train)
y_pred2 = model2.predict(x_test)
print('예측 값 : ', y_pred2)
print('실제 값 : ', y_test)
print('정확도 : %.5f'%accuracy_score(y_test, y_pred2))




