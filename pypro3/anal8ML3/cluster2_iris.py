#군집화 - label(정답) 없음
#iris_dataset

import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
print(iris_df.head())

from scipy.spatial.distance import pdist, squareform
#dist_vec = pdist(iris_df.loc[0:4, ['sepal length (cm)', 'sepal width (cm)']], metric = 'euclidean')
dist_vec = pdist(iris_df.loc[:, ['sepal length (cm)', 'sepal width (cm)']], metric = 'euclidean')

print(dist_vec)
print('-------------------------------------------')
row_dist = pd.DataFrame(squareform(dist_vec))
print(row_dist)
print('-------------------------------------------')

from scipy.cluster.hierarchy import linkage, dendrogram
row_cluster = linkage(dist_vec, method = 'complete') #complete 완전 연결법
print('row_cluster : ', row_cluster)
print('-------------------------------------------')

df = pd.DataFrame(row_cluster, columns = ['id_1', 'id_2', 'dist', 'member']) 
print(df)

row_dend = dendrogram(row_cluster)
plt.tight_layout()
plt.ylabel('euclidean dist')
plt.show()







