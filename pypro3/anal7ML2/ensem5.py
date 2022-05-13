#titanic dataset으로 LogisticRegression, DecisionTreeClassifier, RandomForestClassifier 처리

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv')

print(df.head(), df.shape) #(891, 12)
#사망이랑 필요없는 칼럼 지움
df.drop(columns=['PassengerId', 'Name', 'Ticket'], inplace = True)
print(df.info())
#count를 보면 숫자가 다른 것이 있음 - Non이 있다
#데이터 타입을 보면 obj가 있다 - 데이터 타입을 맞춰줘야 함

print(df.isnull().sum())
#Age         177
#Cabin       687
#Embarked      2
#Null을 어떻게 해야할지 생각을 해야한다
#Null처리 : 0또는 평균 또는 제거 또는 임의의 값으로 대체(앞이나 뒤의 숫자로)
df['Age'].fillna(df['Age'].mean(), inplace = True) #Age를 평균으로 채움
df['Cabin'].fillna('N', inplace = True) #나머지 값들을 N값으로 채움
df['Embarked'].fillna('N', inplace = True)
print(df.isnull().sum())
print(df.head(), df.shape) #(891, 9)

#object type : Sex, Cabin, Embarked 열들의 상태를 별도 확인
print('Sex : ', df['Sex'].value_counts())
print('Cabin : ', df['Cabin'].value_counts())
df['Cabin'] = df['Cabin'].str[:1] #Cabin의 종류가 너무 많으니 앞글자만 따옴
#print(df.Cabin.head(5))
print('Cabin : ', df['Cabin'].value_counts())
print('Embarked : ', df['Embarked'].value_counts())
print(df.head())
#각 데이터의 칼럼 정보를 수집해야 함
#어떤 데이터가 어떤 결과에 영향이 있는가를 생각해 봐야 함


#성별이 생존 확률에 어떤 영향이 있는가?
print(df.groupby(['Sex', 'Survived'])['Survived'].count()) #성별이 생존 확률에 어떤 영향이 있는지 숫자로 표현해줌
#       Sex     Survived
#female  0            81
#        1           233
#male    0           468
#        1           109

#남자의 사망 비율이 여자보다 높아보임 - 데이터를 이용하여 분석하는데 유의미함
#승객은 남자가 많지만 생존자는 여자가 많음을 알 수 있다
print('여자의 생존율 : ', 233/(81+233)) #0.742
print('남자의 생존율 : ', 109/(468+109)) #0.188
#성별 이외에 노인과 아이, 직원과 승객, 부자와 거지 등등의 기준이 있을 수도 있다

#시각화 : 성별 생존확률
#sns.barplot(x = 'Sex', y = 'Survived', data = df, ci = 95) #ci=95 신뢰구간 95%
#plt.show()

#시각화 : 성별, Pclass별 생존확률
#sns.barplot(x = 'Pclass', y = 'Survived', hue = 'Sex', data = df, ci = 95) #성별과 Pclass에 대해서 성별 생존 확률
#plt.show()
#1등급에 탈 수록 생존 확률이 높았다


#나이별 생존 확률
def age_category_func(age):
    msg = '' #데이터 값이 들어갈 변수를 만들어줌
    if age <= -1:msg = 'unknown' #나이가 없으면 unknow가 나옴
    elif age <= 5:msg = 'baby' #나이가 5살까지는 아이
    elif age <= 18:msg = 'teenager' #나이가 6살부터 18살까지는 10대
    elif age <= 65:msg = 'adult' #나이가 18살부터 65살까지는 성인
    else:msg = 'elder' #그 외에는 노인
    return msg #함수 실행이 끝나면 msg를 함수를 호출한 곳으로 보내줌

df['Age_category'] = df['Age'].apply(lambda a:age_category_func(a))
print(df.head(10))


#시각화 : 나이별 생존확률
sns.barplot(x = 'Age_category', y='Survived', hue = 'Sex', data = df,
            order = ['unknow', 'baby', 'teenager', 'adult', 'elder']) #순서는 unknow부터 elder순으로
#plt.show()

del df['Age_category'] #시각화 하기 위해 만든 칼럼이니 시각화 확인하고 삭제함


#Dummy변수 : 문자열 -> 숫자(범주형)
#Cabin, Sex, Embarked 등
from sklearn import preprocessing

def label_encode_func(datas):
    cols = ['Cabin', 'Sex', 'Embarked']
    for c in cols:
        la = preprocessing.LabelEncoder().fit(datas[c])
        datas[c] = la.transform(datas[c])
    
    return datas

df = label_encode_func(df)
#label함수에 df를 입력시키면 'Cabin', 'Sex', 'Embarked' 만 작업한 후에 리턴시켜줌

print(df.head(), type(df))
print(df['Cabin'].unique()) # 7 2 4 6 3 0 1 5 8  9가지의 종류
print(df['Sex'].unique()) # 1 0  2가지의 종류
print(df['Embarked'].unique()) # 3 0 2 1  4가지의 종류
print('-------------------------------------------------')

#등등 데이터 가공에는 다양하게 작업할 것들이 많다
from sklearn.model_selection import train_test_split
feature_df = df.drop(['Survived'], axis = 'columns') #독립변수 Survived는 종속변수로 사용할 것이니 데이터 목록에서 제거
label_df = df['Survived'] #종속변수

print(feature_df.head())
print(label_df.head())

x_train, x_test, y_train, y_test = train_test_split(feature_df, label_df, test_size = 0.2, random_state = 1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(712, 8) (179, 8) (712,) (179,)

from sklearn.linear_model import LogisticRegression 
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#학습을 시킴
logmodel = LogisticRegression(solver = 'lbfgs', max_iter = 500).fit(x_train, y_train) 
demodel = DecisionTreeClassifier().fit(x_train, y_train)
rfmodel = RandomForestClassifier().fit(x_train, y_train)

#train으로 학습을 시키고 test로 검증하기
logpredict = logmodel.predict(x_test)
print('LogisticRegression accuracy : {0:.5f}'.format(accuracy_score(y_test, logpredict)))
depredict = demodel.predict(x_test)
print('DecisionTreeClassifier accuracy : {0:.5f}'.format(accuracy_score(y_test, depredict)))
rfpredict = rfmodel.predict(x_test)
print('RandomForestClassifier accuracy : {0:.5f}'.format(accuracy_score(y_test, rfpredict)))

#LogisticRegression accuracy : 0.79888
#DecisionTreeClassifier accuracy : 0.74302
#RandomForestClassifier accuracy : 0.75419
#일반적으로는 RandomForest가 성능이 좋지만 데이터에 따라 최적의 모델이 다르다


#GridSearchCV
from sklearn.model_selection import GridSearchCV

#몇 가지의 파라미터가 있다
#min_samples_split : 노드 분할 최소 샘플 수는? - 몇 개가 좋을까?
#min_samples_leaf : leaf노드의 최소 샘플 수는?
#max_depth
#- 트리의 최대 깊이, default = None
#완벽하게 클래스 값이 결정될 때 까지 분할
#또는 데이터 개수가 min_samples_split보다 작아질 때까지 분할 - 깊이가 깊어지면 과적합될 수 있으므로 적절히 제어 필요
#....등 여러 가지 파라미터가 있다

params = {'max_depth' : [2, 3, 5, 10, 15], 'min_samples_split' : [2, 3, 5], 'min_samples_leaf' : [1, 5, 8]}
#원래는 하나하나 다 넣어서 accuracy_score를 확인해야 하는데 힘드니 GridSearchCV를 사용

#DecisionTreeClassifier
grid_clf = GridSearchCV(demodel, param_grid = params, scoring = 'accuracy', cv = 5)
#학습을 하면서 편향되지 않게 train을 5번 접음
grid_clf.fit(x_train, y_train)
print('best_params_', grid_clf.best_params_) #학습된 데이터 중에 가장 좋은 params를 출력
#{'max_depth': 3, 'min_samples_leaf': 5, 'min_samples_split': 2}
print('best_score_', grid_clf.best_score_) #학습된 데이터 중에 가장 좋은 score를 출력
#0.83430513148823

best_clf = grid_clf.best_estimator_ #최적의 모델 얻기
bestPredict = best_clf.predict(x_test)
print('DecisionTreeClassifier accuracy : {0:.5f}'.format(accuracy_score(y_test, bestPredict)))
#0.80447
print('===================================================')

#RandomForestClassifier
grid_clf2 = GridSearchCV(rfmodel, param_grid = params, scoring = 'accuracy', cv = 5)
#학습을 하면서 편향되지 않게 train을 5번 접음
grid_clf2.fit(x_train, y_train)
print('best_params_', grid_clf2.best_params_) #학습된 데이터 중에 가장 좋은 params를 출력
#{'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 5}
print('best_score_', grid_clf2.best_score_) #학습된 데이터 중에 가장 좋은 score를 출력
#0.8441741357234316

best_clf2 = grid_clf2.best_estimator_ #최적의 모델 얻기
bestPredict2 = best_clf2.predict(x_test)
print('RandomForestClassifier accuracy : {0:.5f}'.format(accuracy_score(y_test, bestPredict2)))


#DecisionTreeClassifier : 0.80447
#RandomForestClassifier : 0.76536 Randomstate를 안 줘서 값이 매번 다르게 나옴

