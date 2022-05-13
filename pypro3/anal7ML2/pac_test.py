#주성분 분석(PCA) : 데이터 차원 축소
#원래 데이터 분산을 최대한 보존하는 새로운 축을 찾고, 그 축에 데이터를 사영(projection) 시키는 방법(직교) 사용

#iris data를 사용해서 차원 축소

from sklearn.decomposition import PCA
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
from sklearn.datasets import load_iris

iris = load_iris()
print(iris.data[:2]) #Sepal.Length    Sepal.Width    Petal.Length    Petal.Width
n=10 #관찰값
x=iris.data[:n, :2] #0열과 1열만 가져옴
print('차원 축소 전 : ', x, x.shape, type(x))
print(x.T)

"""
#시각화
plt.plot(x.T, 'o:')
plt.xticks(range(2), ['꽃받침 길이', '꽃받침 폭'])
plt.xlabel('특성의 종류')
plt.ylabel('특성 값')
plt.title('붓꽃 크기 특성')
plt.legend(['표본{}'.format(i+1) for i in range(n)])
plt.show()
#시각화 하여 보니 두 변수간에는 관계가 있어보임 그래서 산점도를 볼 필요가 있음
"""

"""
#x축에는 꽃받침의 길이, y축에는 꽃받침의 폭
df = pd.DataFrame(x)
ax = sns.scatterplot(df[0], df[1], data=df, marker='s', s=100, color=['b'])
for i in range(n):
    ax.text(x[i, 0]-0.05, x[i, 1]+0.03, '표본 : {}'.format(i+1)) #글씨의 위치와 표본 : 1.. 표본 : 10 까지 표시
plt.xlabel('꽃받침 길이')
plt.ylabel('꽃받침 폭')
plt.title('붓꽃 크기 특성(2차원)')
plt.axis('equal')
plt.show()
#우상향 하는 산점도 
"""

#두 개의 열의 값 패턴이 매우 유사함을 알 수 있다.
#그러므로 차원 축소 가능하다 -> PCA
pca1 = PCA(n_components = 1) #변환하는 차원의 수 2개를 하나로 합칠 거니까 1을 준다
x_low = pca1.fit_transform(x) #지도 학습이 아닌 비지도 학습이라 하나만 주어짐(target은 지정하지 않음)
#특징 행렬을 낮은 차원의 근사행렬로 변환
print(x, ' ', x.shape) #(10, 2)
print('x_low : ', x_low, ' ', x_low.shape) #(10, 1)
#[[5.1 3.5]                                 [[ 0.30270263]
# [4.9 3. ] 이러한 두 변수를 주성분 분석으로 하여     [-0.1990931 ] 하나의 열로 바뀜
#두 열에 관해서 분산을 가장 잘 설명하는 하나의 열로 축소됨

#축소된 차원 원복화
x2 = pca1.inverse_transform(x_low) 
print('원복 값 : ', x2, ' ', x2.shape)
#제 1 주성분 값으로 하여 원래의 값과 완전 똑같지 않다. 근사값으로 됨
#[[5.06676112 3.53108532]    [[5.1 3.5]
# [4.7240094  3.1645881 ]     [4.9 3. ]
print('원래 값 : ', x[0,:]) # [5.1 3.5]
print('주성분 값 : ', x_low[0]) #[0.30270263]
print('원복 값 :', x2[0, :]) #[5.06676112 3.53108532]

"""
#x축에는 꽃받침의 길이, y축에는 꽃받침의 폭
df = pd.DataFrame(x)
ax = sns.scatterplot(df[0], df[1], data=df, marker='s', s=100, color=['b'])
for i in range(n):
    ax.text(x[i, 0]-0.05, x[i, 1]+0.03, '표본 : {}'.format(i+1)) #글씨의 위치와 표본 : 1.. 표본 : 10 까지 표시
    plt.plot([x[i, 0], x2[i, 0]], [x[i, 1], x2[i, 1]], 'k--')
plt.plot(x2[:,0], x2[:,1], 'o-', color='y', markersize=10)
plt.plot(x[:,0].mean(), x[:,1].mean(), 'D', color='r', markersize=10)
plt.xlabel('꽃받침 길이')
plt.ylabel('꽃받침 폭')
plt.title('붓꽃 크기 특성(2차원)')
plt.axis('equal')
plt.show()
"""

#iris 4개의 열을 2개로 축소
x = iris.data
print(x[:2])
pca2 = PCA(n_components = 2)
x_low2 = pca2.fit_transform(x)
print('x_low2 : ', x_low2, ' ', x_low2.shape)
print(pca2.explained_variance_ratio_) #변동성 비율을 보여줌 [0.92461872 0.05306648] 제 1 주성분, 제 2 주성분
x_trans = pca2.inverse_transform(x_low2)
print('원래 값 : ', x[0,:]) # [5.1 3.5 1.4 0.2]
print('주성분 값 : ', x_low2[0]) # [-2.68412563  0.31939725] 근사 행렬로 변환했을 때 원본 값의 0.92461 설명함
#원래값을 주성분값으로 만들 때 0.9246 만큼 설명한다는 뜻
print('원복 값 : ', x_trans[0, :])
#원래 값 :  [5.1 3.5 1.4 0.2]
#원복 값 :  [5.08303897 3.51741393 1.40321372 0.21353169]
#92.461%의 확률로 설명하기 때문에 근사값에 차이가 있음
print('======================================')

#원래값
iris1 = pd.DataFrame(x, columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
print(iris1.head(5))

iris2 = pd.DataFrame(x_low2, columns = ['var1', 'var2'])
print(iris2.head(5))

#분류 작업을 원래 데이터로 해도 되고 주성분 값으로 해도 된다
#iris칼럼 4개를 2개로 비율 값으로 나눈 것





