#iris dataset으로 분류 모델을 작성 : 지도학습(K-NN), 비지도학습(K-Mean)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import numpy as np

iris = load_iris()
train_x, test_x, train_y, test_y = train_test_split(iris['data'], iris['target'], 
                                                    test_size = 0.25, random_state = 42)
print(train_x[:2])
print(train_y[:2])
print('------------------')

#지도학습 : K최근접 이웃 알고리즘
knnModel = KNeighborsClassifier(n_neighbors = 3)
knnModel.fit(train_x, train_y) #feature, label을 주니 지도학습

predict_label = knnModel.predict(test_x)
print(predict_label[:3]) #[1 0 2]
print('acc : ', metrics.accuracy_score(test_y, predict_label)) #1.0 의 정확도를 가짐. 낮추려면 패널티를 주면 됨
print('------------------')

#비지도학습 : K평균 군집 알고리즘
from sklearn.cluster import KMeans

kmeansModel = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
kmeansModel.fit(train_x) #label이 없으니 비지도학습
print(kmeansModel.labels_)
print('0 cluster : ', train_y[kmeansModel.labels_ == 0])
print('1 cluster : ', train_y[kmeansModel.labels_ == 1])
print('2 cluster : ', train_y[kmeansModel.labels_ == 2])
print('------------------')

new_input = np.array([[6.1, 2.3, 4.5, 1.5]])
clu_pred = kmeansModel.predict(new_input)
print(clu_pred)










