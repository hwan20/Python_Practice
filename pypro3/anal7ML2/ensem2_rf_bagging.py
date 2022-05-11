#Bagging은 Bootstrap Aggregation의 약자
#배깅은 샘플을 여러 번 뽑아(Bootstrap) 각 모델을 학습시켜 결과물을 집계(Aggregration)하는 방법
#RandomForestClassifier

#데이터로부터 부트스트랩을 하고 (복원 랜덤 샘플링) 부트스트랩한 데이터로 모델을 학습시킴
#그리고 학습된 모델의 결과를 집계하여 최종 결과 값을 구함 - 평균 값으로 구함

#Survived: 생존 여부 => 0 = No, 1 = Yes
#pclass: 티켓 등급 => 1 = 1st, 2 = 2nd, 3 = 3rd
#Sex: 성별
#Age: 나이
#Sibsp: 함께 탑승한 형제자매, 배우자의 수
#Parch: 함께 탑승한 부모, 자식의 수
#Ticket: 티켓 번호
#Fare: 운임
#Cabin: 객실 번호
#Embarked: 탑승 항구 => C = Cherbourg, Q = Queenstown, S = Southampton

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import pandas as pd
from sklearn.preprocessing.tests.test_data import n_features

df = pd.read_csv('../testdata/titanic_data.csv')
print(df.keys())
print(df.head(), df.shape) #(891, 12)
print(df.isnull().any()) #null인 칼럼을 알기 위해? 21분

df = df.dropna(subset=['Pclass', 'Age', 'Sex']) #3개의 칼럼을 사용할 것이니 3개의 칼럼에서 nan이 있는 값을 날림
print(df.shape) #(714, 12)

df_x = df[['Pclass', 'Age', 'Sex']] #3개의 행을 가지고 matrix를 만듦
print(df_x.head())

#Sex columns의 male, female을 0과 1로 가공하기
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np

#방법 1
df_x.loc[:, 'Sex'] = LabelEncoder().fit_transform(df_x['Sex'])
#남자는 1 여자는 0 이유는 LabelEncoder는 사전 순으로 처리해줌

#방법 2
#df_x['Sex'] = df_x['Sex'].apply(lambda x: 1 if x == 'male' else 0)
#만약 x가 male이면 x를 1로 바꿔줌
print(df_x.Sex.head())
#male, female로 되어있는 Sex columns를 0, 1로 바꿔주는 두 가지 방법

"""
#OneHotEncoder를 사용하면 분류 모델에서 성능이 더 좋게 나올 수 있다
#pcalss를 나눈 것 LabelEncoder가 나온 김에 설명함
df_x2 = pd.DataFrame(OneHotEncoder().fit_transform(df_x['Pclass'].values[:, np.newaxis]).toarray(),
                                                   columns = ['f_class', 's_class', 't_class'],
                                                   index = df_x.index)
print(df_x2.head())

df_x = pd.concat([df_x, df_x2], axis = 1)
print(df_x.head())
"""

df_y = df['Survived']
train_x, test_x, train_y, test_y = train_test_split(df_x, df_y)
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape) #(535, 3) (179, 3) (535,) (179,)
#랜덤 포레스팅으로 배깅을 사용하고 있음 병렬처리, 성능은 부스팅에 비해서 조금 떨어짐

#model : RandomForestClassifier - 여러 개의 DecisionTree를 배깅방식으로 처리해 최적화된 앙상블 모델을 구현
#앙상블은 여러 개의 모델을 사용해 투표하여 최적화된 모델을 정함 - 병렬 방식
model = RandomForestClassifier(criterion='entropy', n_estimators=500)
#https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
#n_estimators=100, *, criterion='gini' 가 기본 값
#criterion{“gini”, “entropy”}, default=”gini”
#gini를 사용하던 entropy를 사용하던 상관은 없지만 gini는 4분


model = model.fit(train_x, train_y)

pred = model.predict(test_x)
print('예측 값 : ', pred[:10])
print('실제 값 : ', np.array(test_y[:10]))
print('accuracy : ', sum(test_y == pred) / len(test_y))

from sklearn.metrics import accuracy_score
print('accuracy : ', accuracy_score(test_y, pred))

#교차검증(cross validation - K-fold)
cross_vali = cross_val_score(model, train_x, train_y, cv = 5)
print(cross_vali)
print(np.round(np.mean(cross_vali), 3)) #5겹 교차 검증 처리 모델 평균 정확도
#train한 부분으로 하니까 조금 더 떨어짐, overfitting 방지하기 위해 더 깐깐하니까

#train / test 하기 전 값으로 구함
cross_vali2 = cross_val_score(model, df_x, df_y, cv = 5) #를 사용할 수도 있다
print(cross_vali2)
print(np.round(np.mean(cross_vali2), 3))
print('----------------')


#모델의 중요 변수 확인
#중요 변수를 확인하고 필요 없는 변수는 빼서 확률을 더 높일 수 있다
import matplotlib.pyplot as plt

print('특성(변수)의 중요도 : \n {}'.format(model.feature_importances_))

def plot_feature_importances_func(model):
    n_features = df_x.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align = 'center')
    plt.yticks(np.arange(n_features), df_x.columns) #눈금 대신에 columns를 대입
    plt.xlabel('attr importances') #attr은 변수를 얘기함
    plt.ylabel('attr')
    plt.show()

plot_feature_importances_func(model)

#Age, Sex, Pclass 순으로 중요도가 있다












