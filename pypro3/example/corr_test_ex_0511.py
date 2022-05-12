#에이콘 주식회사에서 영업사원들의 '지각횟수'와 '판매횟수' 간에 관계가 있는지 알아보려고 한다.
#영업사원 5명을 대상으로 한 달 동안 '지각횟수'와 '판매횟수'를 조사했더니 아래와 같은 결과를 얻었다.
#둘 사이의 상관계수를 출력하고 상관관계가 있는지 설명하시오.

#지각횟수(x) = 1,2,3,4,5
#판매횟수(y) = 8,7,6,4,5

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='malgun gothic')

df = pd.DataFrame({'x' : (1,2,3,4,5), 'y' : (8,7,6,4,5)})

print(df)
print(df.corr()) #지각횟수 x와 판매횟수 y는 음의 상관관계를 가지고 있다

plt.scatter(df.x, df.y)
plt.xlabel('지각횟수(x)')
plt.ylabel('판매횟수(y)')
plt.show()