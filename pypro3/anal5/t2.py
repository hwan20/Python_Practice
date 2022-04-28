#두 집단 평균 또는 비율 차이 검정
#두 집단의 가설검정 – 실습 시 분산을 알지 못하는 것으로 한정하겠다.
#선행조건 : 정규성, 등분산성을 확인해야 한다

#* 서로 독립인 두 집단의 평균 차이 검정(independent samples t-test)
#남녀의 성적, A반과 B반의 키, 경기도와 충청도의 소득 따위의
#서로 독립인 두 집단에서 얻은 표본을 독립표본(two sample)이라고 한다.

#실습1) 남녀 두 집단 간 파이썬 시험의 평균 차이 검정

#귀무 : 남녀 간의 파이썬 시험 평균에 차이가 없다.
#대립 : 남녀 간의 파이썬 시험 평균에 차이가 있다.

import pandas as pd
from numpy import average
from scipy import stats


male = [75, 85, 100, 72.5, 86.5]
female = [63.2, 76, 52, 100, 70]

print(average(male), ' ', average(female)) #83.8   72.24
#평균은 average로도 쓸 수가 있다

#정규성과 등분산성은 생략 

#onesample 검정이 아닌 31분
two_sample = stats.ttest_ind(male, female) #두 개의 표본에 대해 독립표본 t검정
print(two_sample)
#statistic(t값)=1.233193127514512, pvalue=0.2525076844853278  p값이 좀 크니 t값이 작다
#해석 : pvalue값이 유의수준 0.05보다 크므로 귀무가설이 채택된다


print('---------------------------------')
#실습2) 두 가지 교육방법에 따른 평균시험 점수에 대한 검정 수행 two_sample.csv

#귀무 : 두 가지 교육 방법에 따른 평균 시험 점수는 차이가 없다.
#대립 : 두 가지 교육 방법에 따른 평균 시험 점수는 차이가 있다.

data = pd.read_csv('../testdata/two_sample.csv')
print(data.head())

ms = data[['method','score']]
print(ms.head(), ms.tail(), len(ms))

m1 = ms[ms['method']==1]  #방법 1
m2 = ms[ms['method']==2]  #방법 2

#score1 = ms[ms['score']==1]
#Empty DataFrame
#Columns: [method, score]
#Index: []


score1 = m1['score']
score2 = m2['score']
#print('---------------------------------')
#print(score1)
#print('---------------------------------')
#print(score2)

#데이터프레임이름.isnull().sum() #널 확인

#sco1 = score1.fillna(0) #Nan값 0으로 채우기
#sco2 = score2.fillna(0)
sco1 = score1.fillna(score1.mean()) #Nan값 평균으로 채우기
sco2 = score2.fillna(score2.mean())


#정규성 확인
#하나씩 확인할 수도 있다
print(stats.shapiro(sco1)) #0.36799
print(stats.shapiro(sco2)) #0.67141

#정규성 시각화
#import seaborn as sns
#import matplotlib.pyplot as plt
#sns.histplot(sco1, kde=True)
#sns.histplot(sco2, kde=True)
#plt.show()


#등분산성 확인 : 0.05보다 크면 만족
#모수 검정일 떄
print(stats.levene(sco1,sco2)) #0.45684    제일 많이 사용
print(stats.fligner(sco1, sco2).pvalue) #0.44323   pvalue만 확인 가능
#비모수 검정일 때
print(stats.bartlett(sco1, sco2)) #0.26789


#정규성과 등분산성을 만족하니
result = stats.ttest_ind(sco1, sco2, equal_var=True) #등분산성 만족 O
#result = stats.ttest_ind(sco1, sco2, equal_var=False) #등분산성 만족 X
print('검정통계량 t : %.5f, p-value : %.5f'%result) #검정통계량 t : -0.19649, p-value : 0.84505
#해석 : p-value는 0.05보다 크므로 귀무 채택된다  
#두 가지 교육 방법에 따른 평균 시험 점수에 차이는 없다

#two 샘플일 때
#참고로 정규성을 만족하지 못한 경우 
#stats.mannwhitneyu(sco1, sco2) #표본의 크기가 다를 때
#stats.wilcoxon(sco1, sco2) #표본의 크기가 같을 때






