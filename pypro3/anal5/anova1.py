#ANOVA(분산분석)

#세 개 이상의 모집단에 대한 가설검정 – 분산분석
#독립인 두 집단의 평균 비교를 반복하여 실시할 경우에 제1종 오류가 증가하게 되어 문제가 발생한다
#이를 해결하기 위해 Fisher가 개발한 분산분석(ANOVA, ANalysis Of Variance)을 이용하게 된다.

#세 집단 이상의 평균의 차이를 검정
#전제조건 : 독립성, 정규성, 불편성(편향이 없어야 한다. 등분산성)
#독립변수 : 범주형, 종속변수 : 연속형
#f-value = 그룹간분산 / 그룹내분산  f값이 크면 p값이 작은 것이니 귀무가설 기각
#집단 간 분산이 집단 내 분산보다 충분히 큰 것인가를 파악하는 것 
#종속변수의 변화(분산)폭이 독립변수에 의해 주로 기안하는지를 파악하는 것

 
#세 개 이상의 모집단에 대한 가설검정 – 분산분석
#‘분산분석’이라는 용어는 분산이 발생한 과정을 분석하여 요인에 의한 분산과 요인을 통해 나누어진 각 집단 내의 분산으로 나누고 요인
#에 의한 분산이 의미 있는 크기를 크기를 가지는지를 검정하는 것을 의미한다.
#세 집단 이상의 평균비교에서는 독립인 두 집단의 평균 비교를 반복하여 실시할 경우에 제1종 오류가 증가하게 되어 문제가 발생한다.
#이를 해결하기 위해 Fisher가 개발한 분산분석(ANOVA, ANalysis Of Variance)을 이용하게 된다.

#하나의 요인에 속한 집단이 복수 : 일원 분산 분석(one-way anova)

#* 서로 독립인 세 집단의 평균 차이 검정
#실습) 세 가지 교육방법을 적용하여 1개월 동안 교육받은 교육생 80명을 대상으로 실기시험을 실시. three_sample.csv'

#귀무 : 3가지 교육방법에 따른 교육생 80명의 실기시험 평균에 차이가 없다
#대립 : 3가지 교육방법에 따른 교육생 80명의 실기시험 평균에 차이가 있다

import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
import statsmodels.api as sm


data = pd.read_csv("../testdata/three_sample.csv")
print(data.head(3), len(data))
print(data.describe())

#boxplot으로 이상치를 확인
import matplotlib.pyplot as plt
#plt.boxplot(data.score)
#plt.hist(data.score)
#plt.show()
#100점이 만점인 score를 보는데 100점이 넘는 것들이 있어 그래프랑 점수가 이상

#100점이 넘거나는 score는 버림
data = data.query('score <= 100')
print(data.describe())

#plt.hist(data.score)
#plt.show()
#이제 알맞은 그래프가 나온다

#등분산성 확인 : 분산의 치우침 정도. 만족하면 anova, 만족하지 않으면 welch_anova를 사용
#등분산성을 만족하지 못 하는 경우 사용하기 전에 데이터를 가공할 수가 있다 - 표준화, 정규화, transformation(자연 로그를 씌운다)

result = data[['method', 'score']] #method칼럼과 score칼럼만 뽑아옴
#print(result)

m1 = result[result['method'] == 1] #method가 1인 행만 뽑아서 저장
m2 = result[result['method'] == 2]
m3 = result[result['method'] == 3]

score1 = m1['score'] #method가 1인 score 칼럼만 저장
score2 = m2['score']
score3 = m3['score']

#print(m1)
print(score1)

print('등분산성 확인 : ', stats.levene(score1, score2, score3).pvalue) #0.11322 > 0.05으로 등분산성 만족


#정규성 확인 #15분
#하나씩 보는 방법
print(stats.shapiro(score1))
print(stats.shapiro(score2))
print(stats.shapiro(score3))
print('----------------------')

#두 개를 같이 보는 방법
print(stats.ks_2samp(score1, score2))
print(stats.ks_2samp(score1, score3))
print(stats.ks_2samp(score2, score3))
print('----------------------')

#독립성 확인 : 상관관계 등으로 확인




#교육방법별 건수 : 교차표
data2 = pd.crosstab(index = data['method'], columns = 'count')
data2.index = ['방법1', '방법2', '방법3']
print(data2)
print('----------------------')


#교육방법별 만족여부 건수 : 교차표
data3 = pd.crosstab(data.method, data.survey)
data3.index = ['방법1', '방법2', '방법3']
data3.columns = ['만족', '불만족']
print(data3)

#f통계량을 얻기 위해 회귀분석 모델을 사용
#ANOVA 사용시에는 lm 필요
lm = ols('data["score"] ~ C(data["method"])', data = data).fit() #C(독립변수..) : 범주형임을 알림
#최소 제곱법으로 절편과 기울기를 알 수 있다
table = sm.stats.anova_lm(lm, typ=1)
print(table) #분산 분석표, 보고서 만들 때 반드시 필요

#                         자유도      처리 제곱합   sum_sp/df  F는 C의 mean_sq를 Residual의 mean나눈 값    
#                          df        sum_sq     mean_sq         F    PR(>F)
#C(data["method"]) (처리)   2.0     28.907967   14.453984  0.062312  0.939639    F와 P-value는 반비례 관계
#Residual          (오차)   75.0  17397.207418  231.962766       NaN       NaN

#p-value는 0.939639로 0.05보다 크므로 귀무가설 채택된다 
#3가지 교육방법에 따른 교육생 80명의 실기시험 평균에 차이가 없다

import numpy as np

print(np.mean(score1), np.mean(score2), np.mean(score3))
#집단 1, 2, 3의 차이가 있나 없나
#통계적으로는 차이가 없다



#사후 검정(Post Hoc Test)
#분산 분석은 세 개 이상의 집단에 평균의 차이 유무만을 알려줌
#세 개 이상의 집단 각각의 집단 간 평균의 차이를 알고 싶은 경우
#차이가 없어서 굳이 안 해도 되지만 한 번 확인을 해보는 것

from statsmodels.stats.multicomp import pairwise_tukeyhsd
turkey_result = pairwise_tukeyhsd(data.score, groups = data.method)

print(turkey_result)
#group1 group2 meandiff p-adj  lower   upper  reject
#---------------------------------------------------
#     1      2   0.9725   0.9  -8.946  10.891  False
#     1      3   1.4904   0.9 -8.8184 11.7992  False
#     2      3   0.5179   0.9 -9.6127 10.6484  False
#---------------------------------------------------

#시각화
turkey_result.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()







