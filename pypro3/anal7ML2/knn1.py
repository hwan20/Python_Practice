#KNN : 데이터로부터 거리가 가까운 k개의 다른 데이터의 레이블을 참조하여 분류를 진행

train = [
    [5, 3, 2], #데이터가 줄어듦
    [1, 3, 5], #데이터가 늘어남
    [4, 5, 7]
]

label = [0, 1, 1]

import matplotlib.pyplot as plt

#plt.plot(train, 'o')
#plt.xlim([-1, 3])
#plt.ylim([0, 10])
#plt.show()

from sklearn.neighbors import KNeighborsClassifier
kmodel = KNeighborsClassifier(n_neighbors = 3, weights = 'distance')
kmodel.fit(train, label)
pred = kmodel.predict(train)
print('pred : ', pred)
#[0 1 1] 로 레이블 데이터에 맞게 잘 분류함

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

plt.rc('font', family='malgun gothic')

cancer = load_breast_cancer()

#데이터가 많으니 잘름
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target,
                                                    stratify = cancer.target, random_state = 66)
#straify = cancer.target은 한 쪽으로 치우침을 방지
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(426, 30) (143, 30) (426,) (143,)

train_acc = []
test_acc = []
neighbors_set = range(1, 11)

for n_nei in neighbors_set:
    clf = KNeighborsClassifier(n_neighbors = n_nei)
    clf.fit(x_train, y_train)
    train_acc.append(clf.score(x_train, y_train))
    test_acc.append(clf.score(x_test, y_test))

import numpy as np
print(train_acc)
print(test_acc)
print('train 분류 평균 정확도 : ', np.mean(train_acc)) #0.954225
print('test 분류 평균 정확도 : ', np.mean(test_acc)) #0.91888
#오버피팅을 확인하기 위해 train과 test를 확인함. 이정도의 차이는 괜찮음


plt.plot(neighbors_set, train_acc, label = '훈련 정확도')
plt.plot(neighbors_set, test_acc, label = '검증 정확도')
plt.xlabel('k값')
plt.ylabel('정확도')
plt.legend()
plt.show()






