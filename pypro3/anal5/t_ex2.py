#[one-sample t 검정 : 문제2] 
#국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간으로 파악되었다.
#A회사에서 생산된 노트북 평균시간과 차이가 있는지를 검정하기 위해서
#A회사 노트북 150대를 랜덤하게 선정하여 검정을 실시한다.
#실습 파일 : one_sample.csv
#참고 : time에 공백을 제거할 땐 ***.time.replace("     ", "")

#귀무 : A회사에서 생산된 노트북의 평균 사용 시간은 5.2시간이다.
#대립 : A회사에서 생산된 노트북의 평균 사용 시간은 5.2시간이 아니다.

import pandas as pd
import scipy.stats as stats
import numpy as np

data = pd.read_csv("../testdata/one_sample.csv")

print(data['time'].head(8))
print("---------------------------")

data = data.replace("     ","") #공백 제거이지만 바로 제거되지는 않음
#print(data.head(8), data.info())
#print("---------------------------")

data['time'] = pd.to_numeric(data['time']) #공백 제거를 위해 time 칼럼을 numeric타입으로 바꿈
#print(data.head(8), data.info())
#print("------------2---------------")

data = data.dropna(axis=0) #Nan값이 된 공백을 제거함
print(data['time'].head(10))
print(data.time.mean())  #5.2  vs  5.55688  차이가 있나? 없나?

#정규성 확인
print(stats.shapiro(data.time))
#statistic=0.9913735389709473, pvalue=0.7242600917816162
#p값은 0.05보다 매우 작으므로 정규성을 만족한다


#검정 수행
print(stats.ttest_1samp(data.time, popmean=5.2))
#statistic=3.9460595666462432, pvalue=0.00014166691390197087
#p값은 0.00014로 0.05보다 작으므로 귀무가설을 기각하고 대립가설을 채택한다

#해석 : A회사에서 생산된 노트북의 평균 시간은 5.2시간이 아니다

