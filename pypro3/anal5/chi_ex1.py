"""
부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
  예제파일 : cleanDescriptive.csv
  칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
  조건 :  level, pass에 대해 NA가 있는 행은 제외한다.
"""

#귀무가설 : 부모의 학력 수준이 자녀의 대학 진학여부와 관련이 없다 (독립이다)
#대립가설 : 부모의 학력 수준이 자녀의 대학 진학여부와 관련이 있다 (독립이 아니다)

import pandas as pd
import scipy.stats as stats

data = pd.read_csv("../testdata/cleanDescriptive.csv")

print(data.head(5))
print(data.tail(5))
#print(data.columns)
print()

print(data['level'].unique())
print(data['pass'].unique())
print()

ctab = pd.crosstab(index=data['level'], columns=data['pass']).fillna(0)
ctab.columns=['진학', '비진학']
ctab.index=['고졸', '대졸', '대학원졸']
print(ctab)
"""
pass     진학  비진학
level          
고졸       49   40
대졸       55   27
대학원졸    31   23
"""

chi2, p, df, _ = stats.chi2_contingency(ctab)
print("chi2 : {}, p : {}, df : {}".format(chi2, p, df))
#chi2 : 2.7669512025956684, p : 0.25070568406521365, df : 2
#p값이 0.25로 유의 수준 0.05보다 높으므로 귀무가설은 기각하지 않으며 대립가설은 채택하지 않는다

#카이제곱분포표로 확인
#검정통계량 값인 chi2는 2.76695이고, 자유도는 2일 때 카이제곱표에 있는 임계값은 5.99이다
#이때 검정통계량 값이 임계값 안에 있으므로 대립가설은 채택하지 않는다.


