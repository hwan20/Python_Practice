#상관관계 문제)
#https://github.com/pykwon/python 에 있는 Advertising.csv 파일을 읽어 tv,radio,newspaper 간의 상관관계를 파악하시오. 
#그리고 이들의 관계를 heatmap 그래프로 표현하시오. 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("../testdata/Advertising.csv")
#print(data)

#numpy로 상관계수 보기
#print(np.corrcoef(data.tv, data.radio)) #[[1.         0.05480866]
#print(np.corrcoef(data.tv, data.newspaper)) #[[1.         0.05664787]


data=data.drop(['no', 'sales'], axis=1)

print(data.corr())
#                 tv     radio  newspaper
#tv         1.000000  0.054809   0.056648
#radio      0.054809  1.000000   0.354104
#newspaper  0.056648  0.354104   1.000000


#heatmap 그래프로 표시
import seaborn as sns
sns.heatmap(data.corr()) #heat는 상관계수에 따라 색을 입혀줌
plt.show() 


