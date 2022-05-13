#kaggle.com이 제공하는 'Red Wine quality' 분류 ( 0 - 10)
#dataset은 winequality-red.csv 
#https://www.kaggle.com/sh6147782/winequalityred?select=winequality-red.csv

#Input variables (based on physicochemical tests):
# 1 - fixed acidity
# 2 - volatile acidity
# 3 - citric acid
# 4 - residual sugar
# 5 - chlorides
# 6 - free sulfur dioxide
# 7 - total sulfur dioxide
# 8 - density
# 9 - pH
# 10 - sulphates
# 11 - alcohol
# Output variable (based on sensory data):
# 12 - quality (score between 0 and 10)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import model_selection

df = pd.read_csv("../testdata/winequality-red.csv")
print(df.head(3), df.shape) 
print(df.isnull().any())

df_x = df.drop(['quality'], axis=1)  # 독립변수로 사용. quality를 제외한 나머지 칼람
df_y = df['quality']  # 종속변수로 사용

print(df_y.unique()) # [5 6 7 4 8 3]
print(df_x.columns)  # ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', ...

train_x, test_x, train_y, test_y = train_test_split(df_x, df_y)
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)

model = RandomForestClassifier(criterion='entropy', n_estimators=500)  
model.fit(train_x, train_y)
pred = model.predict(test_x)

from sklearn.metrics import accuracy_score
print('acc: ', accuracy_score(test_y, pred))  # acc:  0.7075

# 독립변수 중 중요 변수 확인
print()
import matplotlib.pyplot as plt
import numpy as np

print('특성(변수) 중요도: {}'.format(model.feature_importances_))

def plot_importance_func(model):
    n_features = df_x.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), df_x.columns)
    plt.xlabel("attr importance")
    plt.ylabel("attr")
    plt.show()

plot_importance_func(model)




