#iris data로 시각화
import matplotlib.pyplot as plt
import pandas as pd
from numpy import diagonal

iris_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/iris.csv")
print(iris_data.info())
print('-------------')
print(iris_data.head(3))

plt.scatter(iris_data['Sepal.Width'], iris_data['Petal.Width'])
plt.show()

#pandas의 시각화
from pandas.plotting import scatter_matrix
iris_col = iris_data.loc[:, 'Sepal.Width':'Petal.Width'] #모든 행에 대한 
scatter_matrix(iris_col, diagonal='kde') #diagonal='kde' 밀도 분포
plt.show() 


#seaborn
import seaborn as sns
sns.pairplot(iris_data, hue='Species', height=1)
plt.show()







