#소득 수준에 따른 외식 성향을 나타내고 있다. 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다.
#'eat_out.txt' 데이터에 대하여 소득 수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시한다.
#1. 소스 코드와 모델의 분류정확도를 출력하시오.
#2. 키보드로 소득 수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하시오.

#조건1 : 모델 생성은 glm 함수를 사용하도록 한다.
#조건2 : 키보드로 입력할 소득 수준 값은 45로 한다.

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
from sklearn.metrics import accuracy_score

data = pd.read_csv('../testdata/eat_out.txt')
data = data.drop(['요일'], axis=1)
print(data.head())

formula = '외식유무 ~ 소득수준' 
result = smf.glm(formula = formula, data=data, family = sm.families.Binomial()).fit()
print(result)
print(result.summary())
pred2 = result.predict(data[:10])
print('예측값 : ', np.around(pred2.values)) 
print('실제값 : ', data['외식유무'][:10].values)
pred3 = result.predict(data)
print('정확도 : ', accuracy_score(data['외식유무'], np.around(pred3)))

tmp = int(input('소득수준 : '))
newData = pd.DataFrame({'소득수준':[tmp]})
new_pred = result.predict(newData)[0]
new_pred2 = np.round(new_pred)
print('newpred : ', new_pred)
if new_pred2 == 0:
    print('{}의 소득은 주말에 외식을 하지 않음'.format(tmp))
else:
    print('{}의 소득은 주말에 외식을 함'.format(tmp))
