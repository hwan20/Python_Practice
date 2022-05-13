#SVM으로 XOR 분류 처리

x_data = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm, metrics

x_df = pd.DataFrame(x_data)
feature = np.array(x_df.iloc[:, 0:2])
label = np.array(x_df.iloc[:, 2])
print(feature)
print(label)

#model = LogisticRegression()
model = svm.SVC()
model.fit(feature, label) #fit은 학습된 feature, label의 값이 최소가 될 수 있도록 함
pred = model.predict(feature)
print('예측값 : ', pred) 
print('정확도 : ', metrics.accuracy_score(label, pred)) 

#LogisticRegression()일 때는 and, or gate는 75%의 정확도를 갖지만
#xor gate에서는 50%만 정확도를 갖음 - 선형
#svm.SVC() 를 사용하면 and, or, xor gate에서 100%의 정확도를 갖는다 - 비선형
#deeplearning 나오기 전에는 이미지 분류에 많이 쓰임 80%의 정확도. 그렇지만 deeplearning에 밀림










