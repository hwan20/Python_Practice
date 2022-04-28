#data.go.kr 사이트에서 날씨 데이터를 이용하여 어느 음식점 매출 데이터와 강수 여부에 따른 매출의 평균에 차이를 검정

#데이터는 두 개가 필요하다
#1. 비가 올 때의 매출
#2. 비가 안 올 때의 매출

#귀무 : 강수량에 따른 매출액에 차이가 없다.
#대립 : 강수량에 따른 매출액에 차이가 있다.

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
print(data.head(5), len(data))
print(data.isnull().sum()) #결측치 없음
print('---------------------------')


#독립표본 t-test 검정     강수 여부에 따라서 맻출액의 평균에 차이가 있는가?
#print(data['sumRn']>0) #강수량이 있는 날은 True로 뽑기  328일의 데이터를 가지고 있다

#data['rain_yn'] = (data['sumRn']>0).astype(int)  #강수량이 0이상(비가 오는 날)은 int 타입 1로 만듬
#뜨는 경고는 무시
#print(data.head())


#다른 방법
#print(True*1, False*1) #True * 1 = 1 // False * 1 = 0
data['rain_yn'] = (data.loc[:, ('sumRn')]>0) * 1 #True아니면 False가 나오는데 *1을 해서 강수량이 있는 날은 1로 만듬 위와 같게 만든다
print(data.head())


#시각화
import matplotlib.pyplot as plt

sp = np.array(data.iloc[:,[1, 4]])  #data의 칼럼을 빼옴
print(sp[:2]) #[[0 0]]  0번째 1번째  [18000     1]]  AMT 칼럼과 rain_yn 칼럼
tg1 = sp[sp[:, 1] == 0, 0] #비가 안 올 때의 매출액 
tg2 = sp[sp[:, 1] == 1, 0] #비가 올 때의 매출액
print(tg1[:3])
#print(tg2)
print(tg2[:3])
print('---------------------------')

#plt.plot(tg1)
#plt.show()
#plt.plot(tg2)
#plt.show()

#plt.boxplot([tg1, tg2], notch = True, meanline = True, showmeans = True)
#plt.show()


#두 집단의 각 평균
print('비 안 올 때 : ', np.mean(tg1), ', 비 올 때 : ', np.mean(tg2)) 
#비 안 올 때 :  761040.2542372881 , 비 올 때 :  757331.5217391305
#차이가 있는지 없는지 애매하다


#정규성
print(len(tg1), len(tg2)) #비가 안 온 날 : 236, 비가 온 날 : 92
print(stats.shapiro(tg1).pvalue) #0.056049469858407974 > 0.05 만족
print(stats.shapiro(tg2).pvalue) #0.882739782333374 > 0.05 만족
print('---------------------------')

#등분산성
print(stats.levene(tg1, tg2).pvalue) #0.7123452333011173 > 0.05 만족


#아래의 결과를 얻기 위해 지금까지 데이터 분석을 함
print(stats.ttest_ind(tg1, tg2, equal_var = True))
#Ttest_indResult(statistic=0.10109828602924716, pvalue=0.919534587722196)
#해석 : pvalue=0.91953 > 0.05 이므로 귀무가설 채택, 대립가설 기각
#강수량에 따라 매출액은 차이가 없다

