#PCA(주성분 분석) : 원본 데이터의 feature갯수에 비해 작은 주성분으로
#원본 데이터의 총 변동성(variance)을 대부분 설명할 수 있는 분석기법
#비지도 학습 차원 축소가 해당됨

import numpy as np
import pandas as pd

x1 = [95, 91, 66, 94, 68]
x2 = [56, 27, 25, 1, 9]
x3 = [57, 34, 9, 79, 4]
x = np.stack((x1, x2, x3), axis = 0)
print(x)
print('----------------------')

#표준화
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_std = scaler.fit_transform(x)
print(x_std)
print(scaler.inverse_transform(x_std))
print('----------------------')

#PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
print(pca.fit_transform(x_std))
print(pca.inverse_transform(pca.fit_transform(x_std)))
print('----------------------')

print(scaler.inverse_transform(pca.inverse_transform(pca.fit_transform(x_std))))
print('----------------------')

#wine dataset으로 분류 모델(Randomforest)
from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics
from sklearn.model_selection import train_test_split
import pandas as pd

datas = pd.read_csv('../testdata/wine.csv', header = None)
print(datas.head(3))
x = np.array(datas.iloc[:, 0:12])
y = np.array(datas.iloc[:, 12])
print(x[:2])
print(y[:2], set(y))
#레드와인은 1 화이트와인은 0
print('----------------------')

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size = 0.25, random_state = 1)
model = RandomForestClassifier(n_estimators = 100, criterion = 'entropy').fit(train_x, train_y)
pred = model.predict(test_x)
print('acc : ', sklearn.metrics.accuracy_score(test_y, pred))
print('----------------------')

#주성분 분석 후 feature의 수를 줄여 Randomforest 진행
pca = PCA(n_components = 3)
print(x[:2])
print('----------------------')
print(pca.fit_transform(x)[:3])
print('----------------------')

x_pca = pca.fit_transform(x)
train_x, test_x, train_y, test_y = train_test_split(x_pca, y, test_size=0.25, random_state = 1)
model2 = RandomForestClassifier(n_estimators = 100, criterion = 'entropy').fit(train_x, train_y)
pred2 = model2.predict(test_x)
print('acc2 : ', sklearn.metrics.accuracy_score(test_y, pred2))


#열의 갯수가 많을 때는 주성분 분석을 해서 열의 갯수를 줄여서 작업을 실행








