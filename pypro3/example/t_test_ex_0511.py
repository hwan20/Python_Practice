#다음 데이터는 동일한 상품의 포장지 색상에 따른 매출액에 대한 자료이다.

#포장지 색상에 따른 제품의 매출액에 차이가 존재하는지 two-sample t-검정을 하시오.
#blue : 70 68 82 78 72 68 67 68 88 60 80
#red : 60 65 55 58 67 59 61 68 77 66 66

#귀무가설 : 포장지 색상에 따른 제품의 매출액에는 차이가 없다
#대립가설 : 포장지 색상에 따른 제품의 매출액에는 차이가 있다

import numpy as np
from scipy import stats
import pandas as pd

blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]


# 정규성 검증
print(stats.shapiro(blue).pvalue) # 0.5102 < 0.05 만족
print(stats.shapiro(red).pvalue) #0.5347 < 0.05 만족

# 등분산성 검증
print(stats.levene(blue, red).pvalue) # 0.4391 > 0.05 만족

#정규성을 만족하지 못한 경우 
#stats.mannwhitneyu(sco1, sco2) #표본의 크기가 다를 때
#stats.wilcoxon(sco1, sco2) #표본의 크기가 같을 때
#sample = stats.mannwhitneyu(blue, red)
#print(sample) #pvalue=0.0041 < 0.05 귀무가설 기각, 대립가설 채택
#포장지 색상에 따른 제품의 매출액에는 차이가 있다
print('-----')

#정규성과 등분산성을 만족하는 경우
sample = stats.ttest_ind(blue, red, equal_var=True)
#print('검정통계량 t : %.5f, p-value : %.5f'%sample)
print(sample) #pvalue=0.0083 < 0.05 귀무가설 기각, 대립가설 채택

