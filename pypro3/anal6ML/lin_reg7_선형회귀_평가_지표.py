#Linear Regression - 선형회귀의 평가 지표 score 정리 : MAE, MSE, RMSE, R_Squared...
#r2_score, explained_variance_score, mean_squared_error를 사용하기


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression #OLS Regression Results를 지원하지 않음
from sklearn.metrics import r2_score, explained_variance_score, mean_squared_error
from sklearn.preprocessing import MinMaxScaler #데이터를 0~1사이의 범위로 표준화

#편차가 큰 표본 데이터 작성
sample_size = 100
np.random.seed(1)
x = np.random.normal(0, 10, sample_size)
y = np.random.normal(0, 10, sample_size) + x*30

print(x[:5]) #[ 16.24345364  -6.11756414  -5.28171752 -10.72968622   8.65407629]
print(y[:5]) #[ 482.83232345 -171.28184705 -154.41660926 -315.95480141  248.67317034]
print('상관계수 : ', np.corrcoef(x, y)) #0.99939357


#독립변수(x)에 대한 표준화
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x.reshape(-1, 1)) #matrix형태로 표준화 -1, 1  -> 행의 갯수는 컴퓨터가 처리, 열의 갯수는 하나 100행 1열  100사이즈니?
print(x_scaled[:5], x_scaled.shape) #[[0.87492405] ....  (100, 1)



#시각화
#plt.scatter(x_scaled, y)
#plt.show()


#모델 작성
model = LinearRegression().fit(x_scaled, y) 
#print(model.summary()) #'LinearRegression' object has no attribute 'summary'
#summary가 지원하지 않으니 따로 계산

y_pred = model.predict(x_scaled) #학습한 데이터로 예측결과를 얻어 실제값과 비교
print('예측값 : ', y_pred[:5]) #[ 490.32381062 -182.64057041 -157.48540955 -321.44435455  261.91825779]
print('실제값 : ', y[:5]) #[ 482.83232345 -171.28184705 -154.41660926 -315.95480141  248.67317034]

#모델 성능 파악
def regScore_func(y_true, y_pred):
    print('r2_score(결정계수) : {}'.format(r2_score(y_true, y_pred)))
    print('explained_variance_score(설명분산점수) : {}'.format(explained_variance_score(y_true, y_pred)))
    print('mean_squared_error(평균제곱근오차) : {}'.format(mean_squared_error(y_true, y_pred)))
    #mean_squared_error : 잔차 제곱의 합을 표본수로 나눈 값. 분산 분석의 SSE와 같다 

regScore_func(y, y_pred)
#r2_score(결정계수) : 0.9987875127274646
#explained_variance_score(설명분산점수) : 0.9987875127274646   r2_score와 이 값이 다르면 에러에 편향이 있다 - 모델 학습이 잘못됐다
#mean_squared_error(평균제곱근오차) : 86.14795101998747





#분산을 다르게
#분산이 큰 표본 데이터 작성
x = np.random.normal(0, 1, sample_size)
y = np.random.normal(0, 500, sample_size) + x*30

print(x[:5]) #[-0.40087819  0.82400562 -0.56230543  1.95487808 -1.33195167]
print(y[:5]) #[1020.86531436 -710.85829436 -431.95511059 -381.64245767 -179.50741077]
print('상관계수 : ', np.corrcoef(x, y)) #0.00401167


#독립변수(x)에 대한 표준화
scaler2 = MinMaxScaler()
x_scaled2 = scaler2.fit_transform(x.reshape(-1, 1)) 
print(x_scaled2[:5], x_scaled2.shape) #[[0.45631435]... 


#모델 작성

model2 = LinearRegression().fit(x_scaled2, y) 

y_pred2 = model2.predict(x_scaled2) #학습한 데이터로 예측결과를 얻어 실제값과 비교
print('예측값 : ', y_pred2[:5]) #[-10.75792685  -8.15919008 -11.10041394  -5.7599096  -12.73331002]
print('실제값 : ', y[:5]) #[1020.86531436 -710.85829436 -431.95511059 -381.64245767 -179.50741077]


regScore_func(y, y_pred2) 
#r2_score(결정계수) : 1.6093526521765433e-05  설명력이 매우 낮다
#explained_variance_score(설명분산점수) : 1.6093526521765433e-05
#mean_squared_error(평균제곱근오차) : 282457.9703485092   #평균제곱근오차가 매우 커졌다







