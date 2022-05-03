#상관관계 분석
#두 개 이상의 확률변수(연속형)간에 어떤 관계가 있는지 분석하는 것
#공분산을 표준화한 것을 상관계수(r)라고 한다.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='malgun gothic') #그래프의 한글화 처리


df = pd.DataFrame({'id1':(1, 2, 3, 4, 5), 'id2':(2, 3, -1, 7, 9)})
print(df)
print(df.cov()) #공분산 방향을 알 수가 있다 2.5   4.5 데이터의 단위가 커지면 같이 커짐  이렇게 단위가 다 다르니 공분산을 표준화 한 것이 피어슨 상관 계수이다
print(df.corr()) #피어슨 상관계수 양의 상관 관계 0.711512 데이터의 단위가  커져도 값은 같다

#시각화
#분산도를 확인하기 위해서는 산점도가 좋다
#plt.scatter(df.id1, df.id2)
#plt.show()

#파일 자료를 읽어 상관 분석
data = pd.read_csv("../testdata/drinking_water.csv")
print(data.head(3), len(data))
print(data.info())
print(data.describe())
print("------------------------------")

#공분산
print(np.cov(data.친밀도, data.적절성)) #numpy로는 한 번에 두 가지 밖에 못봄
print(np.cov(data.친밀도, data.만족도))
print(data.cov()) #pandas의 dataframe으로 보면 한 번에 볼 수가 있다
print("--------------2----------------")

#공분산의 데이터 자료를 표준화 하여 볼 수가 있는 게 상관계수이다
print(np.corrcoef(data.친밀도, data.적절성))
print(np.corrcoef(data.친밀도, data.만족도))
print(data.corr()) #기본이 pearson상관 계수로 method를 안 써주면 아래와 같다
print(data.corr(method='pearson')) #좀 더 자세히 보고 싶으면 method='pearson' 정규성을 띄며, 연속형(등간, 비율 척도)이다
#print(data.corr(method='spearman')) #서열척도로 정규성을 띄지 않아 비선형이다
#print(data.corr(method='kendall')) #서열척도로 정규성을 띄지 않아 비선형인 kendall도 있다
print("------------------------------")

co_re = data.corr()
print(co_re['만족도']) #상관계수의 만족도 칼럼만 볼 수가 있다
print(co_re['만족도'].sort_values(ascending=False))
print("------------------------------")

#시각화
data.plot(kind='scatter', x='만족도', y='적절성')
#plt.show()

#색상 표현?
from pandas.plotting import scatter_matrix

#attr = ['친밀도', '적절성', '만족도']
#scatter_matrix(data(attr)) #scatter_matrix를 이용하면 히스토그램과 산점도 같이 볼 수 있다
#plt.show()

#heatmap
import seaborn as sns
#sns.heatmap(data.corr()) #heat는 상관계수에 따라 색을 입혀줌
#plt.show() #색이 밝을수록 상관계수가 높다


# heatmap에 텍스트 표시 추가사항 적용해 보기
corr = data.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)  # 상관계수값 표시
mask[np.triu_indices_from(mask)] = True
# Draw the heatmap with the mask and correct aspect ratio
vmax = np.abs(corr.values[~mask]).max()
fig, ax = plt.subplots()     # Set up the matplotlib figure

sns.heatmap(corr, mask=mask, vmin=-vmax, vmax=vmax, square=True, linecolor="lightgray", linewidths=1, ax=ax)

for i in range(len(corr)):
    ax.text(i + 0.5, len(corr) - (i + 0.5), corr.columns[i], ha="center", va="center", rotation=45)
    for j in range(i + 1, len(corr)):
        s = "{:.3f}".format(corr.values[i, j])
        ax.text(j + 0.5, len(corr) - (i + 0.5), s, ha="center", va="center")
ax.axis("off")
plt.show()


