#[one-sample t 검정 : 문제1]  
#영사기에 사용되는 구형 백열전구의 수명은 250시간이라고 알려졌다. 
#한국연구소에서 수명이 50시간 더 긴 새로운 백열전구를 개발하였다고 발표하였다. 
#연구소의 발표결과가 맞는지 새로 개발된 백열전구를 임의로 수집하여 수명시간을 수집하여 다음의 자료를 얻었다. 
#한국연구소의 발표가 맞는지 새로운 백열전구의 수명을 분석하라.
#   305 280 296 313 287 240 259 266 318 280 325 295 315 278

#귀무 : 백열전구의 수명은 300시간이다     한국연구소의 발표가 맞는지.... 니까 귀무는 300시간이다 이다
#대립 : 백열전구의 수명은 300시간이 아니다

import numpy as np
import pandas as pd
import scipy.stats as stats


sdata = [305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278]
print(np.array(sdata).mean()) #289.7857142857143   평균 시간 300시간이랑 통계적으로 차이가 있는가?

#정규성 확인
print(stats.shapiro(sdata))
#statistic=0.9661144614219666, pvalue=0.8208622932434082
#pvalue가 유의확률 0.05보다 크므로 만족


#검정 수행

result = stats.ttest_1samp(sdata, popmean=300)
print("검정 값은 : %.3f 이며, pvalue 값은 : %.3f 이다" %result)
#검정 값은 : -1.556 이며, pvalue 값은 : 0.144 이다
#pvalue가 0.05보다 크므로 귀무가설은 채택된다
#배열전구의 수명은 300시간이다 해당 데이터는 우연적으로 나온 데이터이다

