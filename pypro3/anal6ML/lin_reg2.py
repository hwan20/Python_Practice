#모델 맛 보기4 : linregression을 사용. model 생성 O

from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#IQ에 따른 시험성적 값 예측
score_iq = pd.read_csv('../testdata/score_iq.csv')
print(score_iq.info())
print(score_iq.head(3), score_iq.shape) #(150, 6)

x = score_iq.iq
y = score_iq.score


#상관계수 확인
print(np.corrcoef(x, y)) #numpy  0.88222034
print(score_iq.corr()) #pandas  0.882220
print('-------------------------')
#plt.scatter(x, y)
#plt.show()

#선형회귀분석
model = stats.linregress(x, y) 
print(model) #LinregressResult(slope=0.6514309527270075, ..........
print('x slope : ', model.slope) #0.6514309527270075
print('y interccept : ', model.intercept) #-2.8564471221974657
print('pvalue : ', model.pvalue) #2.8476895206683644e-50  < 0.05  이므로 유의한 모델이다
#y = model.slope * x + model.intercept

print('IQ에 따른 점수 예측 : ', model.slope * 140 + model.intercept) #점수 예측 :  88.34388625958358  실제 점수 : 90
print('IQ에 따른 점수 예측 : ', model.slope * 120 + model.intercept) #점수 예측 :  75.31526720504343  실제 점수 : 77

#linregression은 predict를 지원하지 않는다
#predict대신에 numpy의 polyval([slope, bias], x)을 이용한다
print('IQ에 따른 점수 예측 : ', np.polyval([model.slope, model.intercept], 140)) #점수 예측 :  88.34388625958358
print('-------------------------')

newdf = pd.DataFrame({'iq' : [55, 66, 77, 88, 150]})
print('새로운 점수 예측 : ', np.polyval([model.slope, model.intercept], newdf).flatten())
#[32.97225528 40.13799576 47.30373624 54.46947672 94.85819579]













