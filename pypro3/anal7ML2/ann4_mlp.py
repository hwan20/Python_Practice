#퍼셉트론은 단층 신경망으로 다중으로 사용하려면 노드의 갯수를 늘려야 한다
#MLP : 다층신경망 노드의 갯수를 복수로 준다 - 선형 / 비선형 분류가 가능하다

import numpy as np
#from sklearn.linear_model import Perceptron #단층 신경망
from sklearn.neural_network import MLPClassifier #다층 신경망
from sklearn.metrics import accuracy_score

feature = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
print(feature)
#label = np.array([0, 0, 0, 1]) #and게이트
#label = np.array([0, 1, 1, 1]) #or게이트
label = np.array([0, 1, 1, 0]) #xor게이트

#입력 데이터가 들어올 때 노드의 갯수를 늘린다.
#노드의 갯수가 하나면 단층 신경망.
#입력되는 부분 - 입력층    
#출력되는 부분 - 출력층
#Layer - 은닝충 여러 개를 가질 수가 있다 갯수가 늘어나면 출력이 좋지만 너무 많으면 안 좋음 - 정해져있지 않음. 분석가의 판단

#ml = MLPClassifier(hidden_layer_sizes=30, activation='relu', solver = 'adam', 
#                   learning_rate_init = 0.01).fit(feature, label) 
#지금은 learning_rate_init을 쓰지만 텐서플로에서는 안 쓰임
#learning_rate_init = 0.01 은 0.01씩 이동한다

ml = MLPClassifier(hidden_layer_sizes=(10, 10, 10), activation='relu', solver = 'adam', 
                   learning_rate_init = 0.01).fit(feature, label) 
#hidden_layer_sizes=(10, 10, 10) 이렇게 줘도 잘 나옴 이유는? 레이어 3개에 노드를 10개씩 줌
#노드 수를 늘릴 건가, 사이즈 수를 늘릴 건지를 선택해야 됨
#레이어와 노드 수가 늘어나면서 연산 양이 엄청나게 늘어나게 됨 -> GPU가 필요(병렬 연산)


print(ml)
pred = ml.predict(feature)
print('pred : ', pred) 
print('acc : ', accuracy_score(label, pred)) 
#hidden_layer_sizes의 노드수를 늘리면 xor이 학습되지 않던 문제를 해결할 수가 있다













