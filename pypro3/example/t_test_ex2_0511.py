#단일표본 검정(one-sample t-test)에 대한 문제다.

#남아 신생아 몸무게의 평균 검정을 수행하려고 한다.
#파일명 : babyboom.csv (testdata 폴더에 있음) # 1:여아, 2:남아 (배점:10)
#남아 신생아의 몸무게는 평균이 3000(g)으로 알려져 왔으나 이것이 틀렸다는 주장이 나왔다.
#표본으로 남아를 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정하시오.

# 귀무 : 남아 신생아의 몸무게는 평균이 3000(g) 이다.
# 대립 : 남아 신생아의 몸무게는 평균이 3000(g)이 아니다.

import pandas as pd
import scipy.stats as stats

data = pd.read_csv('../testdata/babyboom.csv')
print(data.head())
data = data[data['gender'] == 2]
print(data)

#정규성 확인
print(stats.shapiro(data.weight)) #pvalue=0.2022 > 0.05 만족

print(stats.ttest_1samp(data.weight, popmean=3000)) 
#pvalue=0.0001 < 0.05 이므로 귀무가설을 기각하고 대립가설을 채택한다

