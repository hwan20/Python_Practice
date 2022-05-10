#sklearn 모듈(라이브러리) 이 지원하는 과적합 방지 함수(메소드)의 이해
#iris dataset 사용

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
print(iris.keys())
train_data = iris.data
train_label = iris.target
print(train_data[:3])
print(train_label[:3])

#분류 모델
dt_clf = DecisionTreeClassifier() #sklearn의 다른 분류모델을 써도 됨
dt_clf.fit(train_data, train_label)#나누지 않고 모든 데이터를 학습에 참여시킴
pred = dt_clf.predict(train_data)
print('예측값 : ', pred)
#자기가 학습하고 자기가 예측함 합리적이지 못함?

print('실제값 : ', train_label)
print('분류 정확도 : ', accuracy_score(train_label, pred)) #accuracy_score(실제값, 예측값) 순으로 넣어야 함

#분류 정확도 :  1.0 로 분류 정확도가 100%로 과적합 문제 발생
#분류할 필요가 없는 문제
#모델의 포용성을 위해 과적합 문제를 해결하는 방안

#과적합 방지를 목적으로 처리하기 1
#train / test split을 함   보통 7:3, 8:2 비율로 처리를 함
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                    test_size = 0.3, random_state = 121)

print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
#(105, 4) (45, 4) (105,) (45,)
dt_clf.fit(x_train, y_train) #모델 학습은 train data
pred2 = dt_clf.predict(x_test) #모델 평가는 test data
print('예측값 : ', pred2)
print('실제값 : ', y_test)
print('분류 정확도 : ', accuracy_score(y_test, pred2)) #0.95555 과적합이 일어나지 않는 좋은 모델


#과적합 방지를 목적으로 처리하기 2
#본 고사를 치르기 전에 모의고사를 여러 번 보는 것
#모델 학습 시 데이터의 편중을 방지하고자 학습 데이터를 쪼개 학습과 평가를 병행
#교차검증 중 가장 보편적인 방법으로는 k-fold가 있다
from sklearn.model_selection import KFold
import numpy as np
features = iris.data
label = iris.target
dt_clf = DecisionTreeClassifier(criterion = 'entropy', random_state = 123) #criterion, random_state 파라미터 값
kfold = KFold(n_splits = 5) #n_splits은 알아서 적당히 주면 된다
cv_acc = []
print('iris shape : ', features.shape) #(150, 4)  
#150개를 5개(n_splits)로 나눈 후 첫 번째를 검증. 나머지 train
#전체 행 수가 150, 학습데이터 : 4/5(120개), 검증데이터 : 1/5(30)개로 분할해 가며 학습을 진행
#그 다음 120개 중에 90개 학습 30개 검증 이런 식으로 나씩 차례차례 진행

n_iter = 0
for train_index, test_index in kfold.split(features):
    """
    print('n_iter : ', n_iter)
    print('train_index : ', len(train_index))
    print('test_index : ', len(test_index))
    n_iter +=1
    """
    xtrain, xtest = features[train_index], features[test_index]
    ytrain, ytest = label[train_index], label[test_index]
    
    dt_clf.fit(xtrain, ytrain)
    pred = dt_clf.predict(xtest)
    n_iter +=1
    
    #반복할 때마다 정확도 측정
    acc = np.round(accuracy_score(ytest, pred), 3)
    train_size = xtrain.shape[0]
    test_size = xtest.shape[0]
    print('반복 수 : {}, 교차검증 정확도 : {}, 학습데이터 크기 : {}, 학습데이터 크기 : {}'.format(n_iter, acc, train_size, test_size))

    #print('반복 수 : {}, validation data index : {}'.format(n_iter, test_index))
    #30개씩 나눠서 하는 것을 볼 수가 있다
    cv_acc.append(acc)

print('평균 검증 정확도 : ', np.mean(cv_acc)) #0.91999
print('-----------------------------------------------')


#과적합 방지를 목적으로 처리하기 2-1
#정확도가 한 쪽으로 치우쳐저 있으면 k-fold가 안 먹음
#이럴때는 27분 어쩌고 저쩌고
#대출 사기 데이터인 경우 정상과 사기 데이터가 비율적으로 편향된 경우가 많은데
#이럴 때는 k-fold대신 StratifiedKFold를 사용한다
#참고로 iris데이터는 StratifiedKFold와 맞지 않는 데이터이다. - 편향되지 않았기 때문
#스팸 데이터, 강우 여부 이런 경우만 사용 가능

from sklearn.model_selection import StratifiedKFold
skfold = StratifiedKFold(n_splits = 5)
cv_acc = []
n_iter = 0

for train_index, test_index in skfold.split(features, label):
    
    xtrain, xtest = features[train_index], features[test_index]
    ytrain, ytest = label[train_index], label[test_index]   
    
    dt_clf.fit(xtrain, ytrain)
    pred = dt_clf.predict(xtest)
    n_iter +=1
    
    #반복할 때마다 정확도 측정
    acc = np.round(accuracy_score(ytest, pred), 3)
    train_size = xtrain.shape[0]
    test_size = xtest.shape[0]
    print('반복 수 : {}, 교차검증 정확도 : {}, 학습데이터 크기 : {}, 학습데이터 크기 : {}'.format(n_iter, acc, train_size, test_size))

    #print('반복 수 : {}, validation data index : {}'.format(n_iter, test_index))
    #30개씩 나눠서 하는 것을 볼 수가 있다
    cv_acc.append(acc)
    
print('평균 검증 정확도 : ', np.mean(cv_acc)) #0.9534  
print('-----------------------------------------------')



#과적합 방지를 목적으로 처리하기 2-2
#k-fold를 사용해도 되지만 복잡하기 때문에
#cross_val_score를 사용하면 교차검증을 쉽게 할 수 있다

from sklearn.model_selection import cross_val_score

data = iris.data
label = iris.target

score = cross_val_score(dt_clf, data, label, scoring='accuracy', cv = 5)
#이렇게만 하면 KFold의 과정을 거친 것이다
#내부적으로 KFold의 수식이 들어가 있음

print('교차 검증별 정확도 : ', np.round(score, 3))
print('평균 검증 정확도 : ', np.round(np.mean(score), 3))






#과적합 방지를 목적으로 처리하기3
#GridSearchCV : 교차검증과 최적의 속성(하이퍼 파라미터)을 위한 튜닝을 한 번에 처리

from sklearn.model_selection import GridSearchCV

#예를 드는 것. 파라미터 값은 나중에 응용해서 사용
#여러 개의 속성(parameters)값 중 max_depth, min_samples_split에 대해서 최적의 값 찾기
parameters = {'max_depth' : [1, 2, 3], 'min_samples_split' : [2, 3]}
#parameters 속성을 어떻게 주느냐에 따라 값이 달라진다

grid_tree = GridSearchCV(dt_clf, param_grid = parameters, cv = 3, refit = True)
#cv = 3 split의 갯수
#refit = True 최적의 학습값을 가질 때까지 계속 학습
grid_tree.fit(x_train, y_train)


import pandas as pd
scores_df = pd.DataFrame(grid_tree.cv_results_)
pd.set_option('max_columns', None)
#print(scores_df) #칼럼들을 볼 수가 있다

print('GridSearchCV 최적 파라미터 : ', grid_tree.best_params_) 
#최적의 값은 'max_depth': 3, 'min_samples_split': 2 을 넣으면 된다
print('GridSearchCV 최고 정확도 : ', grid_tree.best_score_)
#dt_clf = DecisionTreeClassifier(..., max_depth = 3, min_samples_split = 2, ...)
#GridSearchCV을 사용하면 최적의 모델에 사용 할 parameter값을 구할 수가 있다

#GridSearchCV가 제공하는 최적의 파라미터로 모델(DecisionTreeClassifier) 생성
estimator = grid_tree.best_estimator_ #최적의 파라미터를 가진 모델을 찾아줌
print(estimator) 
#DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=123)
#GridSearchCV에 입력한 속성 값으로 찾은 최적의 모델

pred = estimator.predict(x_test)
print(pred)
print('모델 성능(정확도) : ', accuracy_score(y_test, pred))


#과적합 방지 모델을 생성하는데 있어서 GridSearchCV 중요하다


