"""
[ANOVA 예제 1]
빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.

kind quantity
1       64
2       72
3       68
4       77
2       56
1       NaN
3       95
4       78
2       55
1       91
2       63
3       49
4       70
1       80
2       90
1       33
1       44
3       55
4       66
2       77
"""

#귀무 : 빵을 튀길 때 기름의 종류에 따라 빵이 흡수하는 기름의 평균에 차이가 없다
#대립 : 빵을 튀길 때 기름의 종류에 따라 빵이 흡수하는 기름의 평균에 차이가 있다



import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols 
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd

#데이터 뽑기

kind = [1, 2, 3, 4, 2, 1, 3, 4, 2, 1, 2, 3, 4, 1, 2, 1, 1, 3, 4, 2]
quantity = [64, 72, 68, 77, 56, np.nan, 95, 78, 55, 91, 63, 49, 70, 80, 90, 33, 44, 55, 66, 77]
#print(len(kind), len(quantity))

data = pd.DataFrame({'kind':kind, 'quantity':quantity})
data = data.fillna(data.mean())
#print(data, type(data))

k1 = data[data['kind']==1]
k2 = data[data['kind']==2]
k3 = data[data['kind']==3]
k4 = data[data['kind']==4]

#print(k1)
q1 = k1['quantity']
q2 = k2['quantity']
q3 = k3['quantity']
q4 = k4['quantity']


#정규성
print(stats.shapiro(q1).pvalue) #0.86804
print(stats.shapiro(q2).pvalue) #0.59239
print(stats.shapiro(q3).pvalue) #0.48601
print(stats.shapiro(q4).pvalue) #0.41621



#등분산성
print('등분산성 확인 : ', stats.levene(q1, q2, q3, q4).pvalue)
#등분산성 확인 :  0.3268969935062273
#p-value가 0.05보다 크므로 등분산성을 만족한다


#일원분산분석
lmodel = ols('quantity ~ C(kind)', data=data).fit()
print(anova_lm(lmodel, type=1))
#            df       sum_sq     mean_sq         F    PR(>F)
#C(kind)    3.0   231.304247   77.101416  0.266935  0.848244
#Residual  16.0  4621.432595  288.839537       NaN       NaN
#p값은 0.848244로 0.05보다 크므로 귀무 채택 대립 기각
#빵을 튀길 때 기름의 종류에 따라 빵이 흡수하는 기름의 평균에 차이가 없다


#사후검정
turkey_result = pairwise_tukeyhsd(endog = data.quantity, groups = data.kind)
print(turkey_result)


#시각화
turkey_result.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()








