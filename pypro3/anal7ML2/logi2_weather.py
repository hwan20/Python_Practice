#로지스틱 회귀분석(Logistic linear regression)
#날씨 데이터로 비가 올 확률을 예측하여 분류 모델을 작성하기

import pandas as pd
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np

data = pd.read_csv("../testdata/weather.csv")
print(data.head(), data.shape) #366, 12

#필요 없는 칼럼을 삭제
data2 = pd.DataFrame()
data2 = data.drop(['Date', 'RainToday'], axis=1) #열을 삭제할 거기 때문에 axis=1
#RainTomorrow의 Yes와 No를 0과 1로 바꾸기
data2['RainTomorrow'] = data2['RainTomorrow'].map({'Yes':1, 'No':0}) #더미 변수로 바꿈
print(data2.head())
print(data2.RainTomorrow.unique()) #[1 0] RainTomorrow 칼럼의 데이터 정보를 보여줌 0 아니면 1이다


#train(모델 학습)/test(모델 평가)분리 : 하는 이유는 과적합 방지(overfitting 방지)를 위해
#보통 7:3, 8:2 비율로 나눈다

train, test = train_test_split(data2, test_size = 0.3, random_state = 42)
print(train[:3], train.shape) # 256, 10
print(test[:3], test.shape) # 110, 10


#model
#formula = 'RainTomorrow ~ MinTemp+MaxTemp ...'
clo_select ="+".join(train.columns.difference(['RainTomorrow']))
print(clo_select)
formula='RainTomorrow ~ ' + clo_select

model = smf.glm(formula = formula, data = train, family = sm.families.Binomial()).fit()
#model = smf.logit(formula = formula, data = train).fit()
print(model.summary())

print('예측값 : ', np.rint(model.predict(test)[:5].values))
print('실제값 : ', test['RainTomorrow'][:5].values)

#conf_mat = model.pred_table() #glm에서는 해당 명렁어 지원 안 함
#print(conf_mat)

from sklearn.metrics import accuracy_score
pred = model.predict(test)
print('분류 정확도 : ', accuracy_score(test['RainTomorrow'], np.rint(pred)))  #0.8727272727272727
#정확도를 더 높일 수가 있다 



