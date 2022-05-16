#군집분석(Clustering) : 비지도 학습
#계층적 군집분석 : 특정 알고리즘에 의해 데이터들을 연결하여 계층적으로 군집(클러스터)을 형성
#응집형 : 자료 하나를 군집으로 간주하고 가까운 군집끼리 연결해가는 방법(상향식) - 보콩 많이 사용됨
#분리형 : 전체 자료를 하나의 큰 군집으로 간주하고, 유의한 부분을 분리해가는 방법(하향식)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')

np.random.seed(123)
var = ['X', 'Y']
labels = ['점0', '점1', '점2', '점3', '점4']
x = np.random.random_sample([5, 2]) * 10
df = pd.DataFrame(x, columns = var, index = labels)
print(df)

#콘솔창에 출력되어 있는 데이터만 봐서는 어떻게 분포되어 있는지 모른다 이럴 때 시각화하여 데이터의 분포를 확인
#plt.scatter(x[:, 0], x[:, 1], s=50, c='blue', marker='o')
#plt.grid(True) #보기 편하게 궤도를 그림
#plt.show()

from scipy.spatial.distance import pdist, squareform #pdist로 거리를 잼. 백터로 보니 보기가 힘듦 그래서 squareform을 사용
dist_vec = pdist(df, metric = 'euclidean', out=None) #거리를 계산할 때는 euclidean방법이 기본
print(dist_vec) #[5.3931329  1.38884785 4.89671004 2.40182631 5.09027885 7.6564396 2.99834352 3.69830057 2.40541571 5.79234641]

#거리가 벡터로 나와있어 보기가 어려우니 사각형 형식으로 출력
row_dist = pd.DataFrame(squareform(dist_vec), columns = labels, index = labels)
print(row_dist)
#        점0        점1        점2        점3        점4
#점0  0.000000  5.393133  1.388848  4.896710  2.401826
#점1  5.393133  0.000000  5.090279  7.656440  2.998344
#점2  1.388848  5.090279  0.000000  3.698301  2.405416
#점3  4.896710  7.656440  3.698301  0.000000  5.792346
#점4  2.401826  2.998344  2.405416  5.792346  0.000000

#계층적 군집분석
from scipy.cluster.hierarchy import linkage
row_cluster = linkage(dist_vec, method = 'ward') #single, average, ward .... 등의 연결법이 있다

df = pd.DataFrame(row_cluster, columns = ['클러스터id_1', '클러스터id_2', '거리', '클러스터 멤버수']) 
print(df)

from scipy.cluster.hierarchy import dendrogram
row_dend = dendrogram(row_cluster, labels = labels)
plt.tight_layout()
plt.ylabel('유클리드 거리')
plt.show()




















