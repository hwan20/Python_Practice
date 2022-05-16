#weather dataset으로 비 유무 처리용 나이브베이즈 분류 모델

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import metrics
from nltk.chunk.util import accuracy

df = pd.read_csv('../testdata/weather.csv')
print(df.head())
print(df.info()) #366행 12열짜리
#RangeIndex: 366 entries, 0 to 365
#Data columns (total 12 columns):

#데이터 전처리
x = df[['MinTemp', 'MaxTemp', 'Rainfall']] #최저기온과 최대기온, 강수량을 독립변수로 뽑음
label = df['RainTomorrow'].map({'Yes':1, 'No':0}) #obj타입이니 더미 변수로 변환
print(x[:3])
print(label[:3])

#train / test 데이터 나누기
train_x, test_x, train_y, test_y = train_test_split(x, label, random_state = 0)

#모델 학습
gmodel = GaussianNB()
gmodel.fit(train_x, train_y)

pred = gmodel.predict(test_x) #값을 얻음
print('예측 값 : ', pred[:10]) #[0 0 0 0 0 0 0 0 0 0]
print('실제 값 : ', test_y[:10].values) #[0 0 1 0 1 1 1 0 0 0]

print('acc(정확도) : ', accuracy_score(test_y, pred)) #0.72826   변수의 갯수를 늘려주면 더 좋아질 수도 있다
print('report : \n', metrics.classification_report(test_y, pred))










