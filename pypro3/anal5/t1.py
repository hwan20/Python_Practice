#두 집단 이하의 평균 또는 비율 차이 검정
#t분포는 표본평균을 이용해 정규분포의 평균을 해석할 때 사용한다
#독립변수 : 범주형
#종속변수 : 연속형

#단일 모집단의 평균에 대한 가설검정(one samples t-test)
#하나의 집단에 대한 표본평균이 예측된 평균(모집단의 평균)과 같은지를 검정

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#연습 1) 어느 남성 집단의 평균 키는 177이다. 남성 집단의 표본 데이터를 추출해 평균 차이 검정
#귀무 : 남성 집단의 평균 키는 177이다.
#대립 : 남성 집단의 평균 키는 177이 아니다. (양측검정)
#대립 : 남성 집단의 평균 키는 177보다 크다(또는 작다). (단측검정)


#one_sample = [177.0, 182.7, 169.6, 176.8, 180.0]
#print(np.array(one_sample).mean()) #177.21999999999997
one_sample2 = [167.0, 182.7, 169.6, 176.8, 185.0]
print(np.array(one_sample2).mean()) #176.21999999999997
#두 샘플 데이터의 평균에는 차이가 있는가?

#t분포는 데이터의 정규성을 확인할 필요가 있다
print(stats.shapiro(one_sample2)) #pvalue=0.540051 > 0.05이므로 만족

#검정 수행
result = stats.ttest_1samp(one_sample2, popmean=177)
#print(result)
print('값 : %.3f, p-value : %.3f'%result ) #값 : -0.221, p-value : 0.836
#해석 : p-value:0.836 > 0.05 이므로 귀무가설 채택

result = stats.ttest_1samp(one_sample2, popmean=165) #만약 모집단의 평균 키가 165이었다면 평균키 177과 차이가 있나?
print('값 : %.3f, p-value : %.3f'%result ) #값 : 3.185, p-value : 0.033
#해석 : p-value:0.033 < 0.05 이므로 귀무가설 기각


print('--------------------------')
#연습 2) A중학교 1학년 1반 학생들의 시험결과가 담긴 파일을 읽어 처리(국어 점수 평균 검정)
#A중학교 1학년 1반 학생들의 국어 시험결과는 늘 80이라고 알려져있다

#귀무 : A중학교 1학년 1반 학생들의 국어 시험 평균은 80이다.
#대립 : A중학교 1학년 1반 학생들의 국어 시험 평균은 80이 아니다. 

data = pd.read_csv("../testdata/student.csv")
print(data.head(3))
print(data['국어'].mean()) #국어 시험의 평균은 72.9로 80과 차이가 있는가? - 그냥 봐서는 통계적으로는 알 수가 없다
#print(data.describe())
print(stats.shapiro(data.국어)) #pvalue=0.0129 < 0.05 정규성을 만족하지 않다
#정규성을 만족하도록 데이터를 가공하거나 추가 수집해야함

print(stats.ttest_1samp(data.국어, popmean=80)) #국어 데이터의 평균과 표본 평균의 차이를 알기 위해
#statistic=-1.3321801667713213, pvalue=0.19856051824785262
#p-value > 0.05이므로 귀무 채택. 수집된 데이터는 우연히 발생된 자료이다.


print('--------------------------')
#연습 3) 여아 신생아 몸무게의 평균 검정 수행 babyboom.csv
#여아 신생아의 몸무게는 평균이 2800(g)으로 알려져 왔으나 이보다 더 크다는 주장이 나왔다. (관측검정)
#표본으로 여아 18명을 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정해 보자.

#귀무 : 여아 신생아 몸무게의 평균은 2800(g)이다.
#대립 : 여아 신생아 몸무게의 평균은 2800(g)보다 크다.

data = pd.read_csv("../testdata/babyboom.csv")
print(data.head(3), len(data)) #gender 1은 여아 2는 남아
fdata = data[data.gender == 1] #여아의 데이터만 뽑기 위해 gender가 1인 데이터만 뽑아옴
print(fdata.head(3), len(fdata)) #18
print(np.mean(fdata.weight)) #3132  vs  2800  차이가 있는가?

#정규성 확인
print(stats.shapiro(fdata.weight))
#print(stats.shapiro(fdata.iloc[:, 2])) #위와 같다
#statistic=0.8702831864356995, pvalue=0.017984945327043533
#pvalue가 0.05보다 작으므로 정규성을 만족시키지 못 한다

#정규성 시각화
sns.displot(fdata.weight, kde = True)
plt.show()

stats.probplot(fdata.iloc[:,2], plot=plt) #Q-Q plot   커브를 그리는 그래프는 정규성에 좋지 않음
plt.show()

print(stats.ttest_1samp(fdata.weight, popmean=2800))
#statistic=2.233187669387536, pvalue=0.03926844173060218
#pvalue가 0.05보다 작으므로 귀무가설을 기각하고 대립가설을 채택한다




