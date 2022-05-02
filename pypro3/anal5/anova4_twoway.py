#two-awy anova(이원 분산 분석 - 요인이 두 개) 

import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import urllib.request
import matplotlib.pyplot as plt
import statsmodels.api as sm

url = "https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3_2.txt"
data = pd.read_csv(urllib.request.urlopen(url))
print(data.head(5), data.shape) #(36, 3)

#data.boxplot(column='머리둘레', by='태아수', grid=False)
#plt.show()

#귀무 : 태아수와 관측자수는 태아의 머리 둘레와 관련이 없다. (머리 둘레의 평균과 차이가 없다)
#대립 : 태아수와 관측자수는 태아의 머리 둘레와 관련이 있다. (머리 둘레의 평균과 차이가 있다)

#상호 작용을 주지 않는 경우
reg = ols("data['머리둘레'] ~ C(data['태아수']) + C(data['관측자수'])", data=data).fit()
result = sm.stats.anova_lm(reg, typ=2)
print(result)
print('---------------------------')

#상호 작용이 있는 경우
formula = "머리둘레 ~ C(태아수) + C(관측자수) + C(태아수):C(관측자수)"
#상호작용이 있으면 C(태아수):C(관측자수) 한 번 더 써준다. data=data 해줬기 때문에 data는 생략 가능

reg2 = ols(formula, data).fit()
result2 = sm.stats.anova_lm(reg2, typ=2)
print(result2)

#                    sum_sq    df            F        PR(>F)
#C(태아수)          324.008889   2.0  2113.101449  1.051039e-27
#C(관측자수)           1.198611   3.0     5.211353  6.497055e-03
#C(태아수):C(관측자수)    0.562222   6.0     1.222222  3.295509e-01
#Residual          1.840000  24.0          NaN           NaN

#PR(>F) 3.295509e-01 > 0.05이므로 귀무가설 채택
#태아수와 관측자수는 태아의 머리 둘레와 관련이 없다. (머리 둘레의 평균과 차이가 없다)






