#분산 분석
#강남구에 있는 GS편의점 3개 지역 알바생의 급여에 대한 평균 차이를 검정하기

#그룹별 월급의 통계를 낸 후 차이를 확인

#귀무 : GS편의점 3개 지역 알바생의 급여에 대한 평균에 차이가 없다
#대립 : GS편의점 3개 지역 알바생의 급여에 대한 평균에 차이가 있다

import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt


#data = pd.read_csv("../testdata/group3.txt", header = None)
#print(data, type(data)) #<class 'pandas.core.frame.DataFrame'>
#print(data.describe())
#pandas가 아닌 numpy로도 데이터를 읽어올 수 있다


data = np.genfromtxt("../testdata/group3.txt", delimiter=",")
print(data[:3], type(data))  #<class 'numpy.ndarray'>
print(data.shape)  #(22, 2)  22행 2열

#세 개 집단의 평균 급여
gr1 = data[data[:, 1]==1, 0]  #data의 모든 행, 1열을 1열이 1인 데이터를 저장
gr2 = data[data[:, 1]==2, 0]
gr3 = data[data[:, 1]==3, 0]
print(gr1, ' ', np.mean(gr1)) #316.625
print(gr2, ' ', np.mean(gr2)) #256.44444444444446
print(gr3, ' ', np.mean(gr3)) #278.0
print("-----------------------")

#정규성
print(stats.shapiro(gr1).pvalue) #0.3336853086948395
print(stats.shapiro(gr2).pvalue) #0.6561065912246704
print(stats.shapiro(gr3).pvalue) #0.832481324672699
print("-----------------------")

#등분산성
print(stats.levene(gr1, gr2, gr3).pvalue) #0.045846812634186246
#데이터가 작으니(표본의 수가 적으니) levene(모수)보다 bartlett(비모수)를 사용
print(stats.bartlett(gr1, gr2, gr3).pvalue) #0.3508032640105389
print("-----------------------")

#데이터 분포 시각화
#plt.boxplot([gr1, gr2, gr3])
#plt.show()

#일원분산분석 방법1 : anova_lm   statsmodels 모듈이 제공
df = pd.DataFrame(data, columns = ['pay', 'group'])
print(df.head())
print("-----------------------")

lmodel = ols('pay ~ C(group)', data = df).fit()
print(anova_lm(lmodel, type=1))
print("-----------------------")
#            df        sum_sq      mean_sq         F    PR(>F)
#C(group)   2.0  15515.766414  7757.883207  3.711336  0.043589
#Residual  19.0  39716.097222  2090.320906       NaN       NaN

#p밸류인 PR(>F) 0.043589로 0.05보다 작으므로 귀무 기각, 대립 채택
#GS편의점 3개 지역 알바생의 급여에 대한 평균에 차이가 있다


#일원분산분석 방법1 : f_oneway scipy 모듈이 제공      f_twoway는 없다
f_statistic, pvalue = stats.f_oneway(gr1, gr2, gr3)
print('f_statistic : ', f_statistic)
print('pvalue : ', pvalue)

#f_statistic :  3.7113359882669763
#pvalue :  0.043589334959178244

#어떤 방식으로 해도 값은 똑같다


#사후검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
turkey_result = pairwise_tukeyhsd(endog = df.pay, groups = df.group)
print(turkey_result)

turkey_result.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()











