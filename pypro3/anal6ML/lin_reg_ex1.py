#회귀분석 문제 1) scipy.stats.linregress() <= 꼭 하기 : 심심하면 해보기 => statsmodels ols(), LinearRegression 사용
#나이에 따라서 지상파와 종편 프로를 좋아하는 사람들의 하루 평균 시청 시간과 운동량 대한 데이터는 아래와 같다.
# - 지상파 시청 시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
# - 지상파 시청 시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#    참고로 결측치는 해당 칼럼의 평균 값을 사용하기로 한다. 이상치가 있는 행은 제거. 10시간 초과는 이상치로 한다.  
#구분,지상파, 종편, 운동
#1,  0.9,  0.7, 4.2
#2,  1.2,  1.0, 3.8
#3,  1.2,  1.3, 3.5
#4,  1.9,  2.0, 4.0
#5,  3.3,  3.9, 2.5
#6,  4.1,  3.9, 2.0
#7,  5.8,  4.1, 1.3
#8,  2.8,  2.1, 2.4
#9,  3.8,  3.1, 1.3
#10, 4.8,  3.1, 35.0
#11, NaN,  3.5, 4.0
#12, 0.9,  0.7, 4.2
#13, 3.0,  2.0, 1.8
#14, 2.2,  1.5, 3.5
#15, 2.0,  2.0, 3.5

from scipy import stats
import pandas as pd
import numpy as np

data = pd.DataFrame({'구분' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                    '지상파' : [0.9, 1.2, 1.2, 1.9, 3.3, 4.1, 5.8, 2.8, 3.8, 4.8, np.NaN, 0.9, 3.0, 2.2, 2.0],
                    '종편' : [0.7, 1.0, 1.3, 2.0, 3.9, 3.9, 4.1, 2.1, 3.1, 3.1, 3.5, 0.7, 2.0, 1.5, 2.0],
                    '운동' : [4.2, 3.8, 3.5, 4.0, 2.5, 2.0, 1.3, 2.4, 1.3, 35.0, 4.0, 4.2, 1.8, 3.5, 3.5]})

data = data.fillna({'지상파' : data['지상파'].mean()})
data1 = data.drop(9)
print(data1, data1.info())
#print(data1.shape) #(14, 4)

a = data1.지상파
b = data1['운동']

#print(a, b)

#선형회귀 분석 모델 작성
model = stats.linregress(a, b)
print(model) #slope=-0.6684550167105406, intercept=4.709676019780582,
print('x slope : ', model.slope) #-0.6684550167105406
print('y intercept : ', model.intercept) #4.709676019780582
print('pvalue : ', model.pvalue) #6.347578533142469e-05  pvalue인 0.05보다 작으므로 유의한 모델이다

#y = wx + b    w = slope, b = intercept
print('운동 예상치에 대한 예측 값은 : ', model.slope * 0.9 + model.intercept) #4.108066504741095
print('운동 예상치에 대한 예측 값은 : ', model.slope * 1.2 + model.intercept) #3.9075299997279327

#polyval 값
print('운동 예상치에 대한 예측 값은 : ', np.polyval([model.slope, model.intercept], 0.9)) #4.108066504741095
print('-----------------------------')

new_data = pd.DataFrame({'new_watch' : [1.5, 3.0, 2.2]})
print('새로운 운동 예상치에 대한 예측 값은 : ', np.polyval([model.slope, model.intercept], new_data).flatten())
#[3.70699349 2.70431097 3.23907498]
