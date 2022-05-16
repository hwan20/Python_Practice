#인공신경망 : 단층 신경망(뉴런 또는 노드가 1개) - Perceptron
#입력 데이터값의 가중치 합에 대해서 임계값에 대해서 0또는 1 또는 소프트 맥스를 이용해서 다양한 범주형 데이터로 분류
#input data * 가중치의 합에 대해 (+b는 생량) 임계값(활성 함수, 시그모이드 등)을 이항 분류가 가능

import numpy as np
from sklearn.linear_model import Perceptron #linear모델에 들어있다
from sklearn.metrics import accuracy_score

feature = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
print(feature)
#label = np.array([0, 0, 0, 1]) #and게이트
#label = np.array([0, 1, 1, 1]) #or게이트
label = np.array([0, 1, 1, 0]) #xor게이트는 단층 신경망으로는 학습이 불가능함 정확도 0.5밖에 안 됨


ml = Perceptron(max_iter = 10, eta0 = 0.1).fit(feature, label) #max_iter 최대 학습수, eta 학습율
#x1, x2값이 각 노드로 들어옴 x1 * w1 + b의 형식으로 두 값이 들어와 이항 분류가 됨
print(ml)
pred = ml.predict(feature)
print('pred : ', pred) 
print('acc : ', accuracy_score(label, pred)) 

#학습수 max_iter이 1일 떄 
#[0 0 0 0]
#0.75

#학습수 max_iter이 10일 떄
#[0 0 0 1]
#1.0

#학습 시 차이가 크니 다시 학습을 시작 -> 10번을 하니 학습율이 높아져서 정확도가 올라감
#객체 형식 OOP라서 사람의 학습 방식과 비슷함






