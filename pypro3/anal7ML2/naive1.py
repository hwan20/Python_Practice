#나이브베이즈 모델 : 베이지 정리를 이용
from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder

x = np.array([1, 2, 3, 4, 5])
x = x[:, np.newaxis]
print(x)

y = np.array([1, 3, 5, 7, 9])

model = GaussianNB().fit(x, y)
print(model)
pred = model.predict(x)
print(pred)
print('acc : ', metrics.accuracy_score(y, pred)) #acc :  1.0

#새로운 값으로 분류
new_x = np.array([[0.5], [2], [7], [12], [0.1]])
new_pred = model.predict(new_x)
print('new_pred : ', new_pred) #new_pred :  [1 3 9 9 1]
#가공울 해야함 원핫처리(원핫인코딩) - 대다수의 값은 0으로 주고 해당 데이터의 위치가 있는 데이터만 1로 주는 것
#ex 1 2 3 4 5 가 있을 때
#   0 0 0 1 0 이런식으로 원핫처리 1을 주는 것 
print('============================================')


#가우시안은 분류에서 잘 쓰임 특히 이메일 분류에서 잘 쓰인다
#One Hot encoding
#1. np.eye()
x = '1, 2, 3, 4, 5'
x = x.split(',')
x = np.eye(len(x))
print(x)


#2. OneHotEncoder 사용
x = '1, 2, 3, 4, 5'
x = x.split(',')
x = np.array(x)
x = x[:, np.newaxis]
one_hot = OneHotEncoder(categories = 'auto')
x2 = one_hot.fit_transform(x).toarray()
print(x2)
y = np.array([1, 3, 5, 7, 9])


model2 = GaussianNB().fit(x2, y)
print(model2)
pred2 = model2.predict(x)
print(pred2)






