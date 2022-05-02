#data.go.kr 사이트에서 날씨 데이터를 이용하여 어느 음식점 매출 데이터와 온도 높낮이에 따른 매출의 평균에 차이를 검정

#
#1. 온도가 더울 때의 매출
#2. 온도가 보통일 때의 매출
#3. 온도가 낮을 때의 매출

#귀무 : 매출액은 온도에 따라 차이가 없다.
#대립 : 매출액은 온도에 따라 차이가 있다.

#별도의 파일을 가지고 데이터를 합쳐서 검정할 수도 있다
#제일 중요한건 데이터를 어디서 어떻게 가지고 어떻게 가공하느냐가 중요하다


import numpy as np
import pandas as pd
import scipy.stats as stats

#자료 읽기1
sales_data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tsales.csv',
                         dtype={'YMD':'object'}) #int타입인 날짜를 데이터 2와 병합하기 위해 obj타입으로 바꾼다
print(sales_data.head())
print(sales_data.info())
print('---------------------------')

#자료 읽기2
wt_data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tweather.csv')
print(wt_data.head())
print(wt_data.info())

#자료 1과 자료 2의 필요한 부분을 병합하려면 데이터의 타입을 맞춰줘야 한다
#자료 1의 날짜는 int타입 자료 2의 날짜는 obj타입이다
#20190514, 2018-06-01 '-'을 넣거나 빼서 동일하게 만든다

wt_data.tm = wt_data.tm.map(lambda x:x.replace('-','')) #tm 데이터의 '-'을 지운 후 덮어쓰기
print(wt_data.head())
print('---------------------------')


#데이터의 타입을 맞춰주었으면 두 데이터를 병합하여 정보를 알아내기
#날짜를 기준으로 비가 왔는지, 매출은 어땠는지를 보기 위해 병합
frame = sales_data.merge(wt_data, how='left', left_on='YMD', right_on='tm')
#sales_data를 기준으로 YMD와 tm을 머지
print(frame.head(5))
print(len(frame))
print(frame.columns)

data = frame.iloc[:, [0, 1, 7, 8]] #'YMD', 'AMT', 'maxTa', 'sumRn' 칼럼을 가져온다
print(data.head(5), len(data)) #328
print(data.isnull().sum()) #결측치 없음
print('---------------------------')


#이번에는 maxTa를 사용 -> 구간을 3구간으로 나눔

#일별 최고 온도 구간을 설정
print(data.maxTa.describe())
import matplotlib.pyplot as plt
#plt.boxplot(data.maxTa)
#plt.show()

data['ta_gubun'] = pd.cut(data.maxTa, bins=[-5, 8, 24, 38], labels = [0, 1, 2])
print(data.head(3), ' ', data['ta_gubun'].unique())
print('---------------------------')
#        YMD    AMT  maxTa  sumRn ta_gubun
#0  20190514      0   26.9    0.0        2
#1  20190519  18000   21.6   22.0        1
#2  20190521  50000   23.8    0.0        1

#상관분석
print(data.corr)
print('---------------------------')
x1 = np.array(data[data.ta_gubun==0].AMT)
x2 = np.array(data[data.ta_gubun==1].AMT)
x3 = np.array(data[data.ta_gubun==2].AMT)
print(x1[:3])
print(x2[:3])

#등분산성
print(stats.levene(x1, x2, x3)) #pvalue=0.03900 만족X

#정규성
print(stats.ks_2samp(x1, x2).pvalue)
print(stats.ks_2samp(x1, x3).pvalue)
print(stats.ks_2samp(x2, x3).pvalue) #만족X
print('-----------ㅈ----------------')

#세 그룹의 평균 매출액
spp = data.loc[:, ['AMT', 'ta_gubun']]
print(spp.groupby('ta_gubun').mean())

print(pd.pivot_table(spp, index = ['ta_gubun'], aggfunc='mean'))
print(spp[:3])

sp = np.array(spp)
group1 = sp[sp[:, 1] == 0, 0]
group2 = sp[sp[:, 1] == 1, 0]
group3 = sp[sp[:, 1] == 2, 0]


#매출액 시각화
#plt.boxplot([group1, group2, group3])
#plt.show()

#일원 분산분석
print(stats.f_oneway(group1, group2, group3))
#F_onewayResult(statistic=99.1908012029983, pvalue=2.360737101089604e-34)
#pvalue가 0.05보다 매우 작으므로 귀무가설 기각, 대립가설 채택
#매출액은 온도에 따라 차이가 있다.
print('---------------------------')


#정규성이 만족하지 않으니 확인을 위해 Kruskal을 확인해봄 27분
print(stats.kruskal(group1, group2, group3))  #kruskal-Wallis test
#KruskalResult(statistic=132.7022591443371, pvalue=1.5278142583114522e-29)
print('---------------------------')


#등분산성 만족하지 않으니 
# pip install pingouin
from pingouin import welch_anova
print(welch_anova(data=data, dv='AMT', between='ta_gubun'))
#     Source  ddof1     ddof2           F         p-unc       np2
#0  ta_gubun      2  189.6514  122.221242  7.907874e-35  0.379038
#pvalue는 7.907874e-35로 0.05보다 작으므로 귀무가설 기각 매출액은 온도에 영향이 있다
#해석 : 날씨(온도 : 더움, 보통, 추움)에 따라 매출액은 차이가 있다.
print('---------------------------')

#사후검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
turkey_result = pairwise_tukeyhsd(endog = spp['AMT'], groups = spp['ta_gubun'], alpha=0.05)
print(turkey_result)

turkey_result.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()






