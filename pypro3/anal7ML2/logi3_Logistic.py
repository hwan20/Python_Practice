#LogisticRegression 클래스를 사용
#pima-indians-diabetes dataset 사용

#피마 인디언 당뇨병 데이터 세트는 아래와 같이 구성되어있다.

#Pregnancies: 임신 횟수
#Glucose: 포도당 부하 검사 수치
#BloodPressure: 혈압(mm Hg)
#SkinThickness: 팔 삼두근 뒤쪽의 피하지방 측정값(mm)
#Insulin: 혈청 인슐린(mu U/ml)
#BMI: 체질량지수(체중(kg)/키(m))^2
#DiabetesPedigreeFunction: 당뇨 내력 가중치 값
#Age: 나이
#Outcome: 클래스 결정 값(0 또는 1)


from sklearn import model_selection
from sklearn.linear_model import LogisticRegression #이항 외에 다항 분류도 가능
import pickle #객체를 저장할 때 사용
import pandas as pd

url = "https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/pima-indians-diabetes.data.csv"
names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
         'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
df = pd.read_csv(url, names=names)
print(df.DiabetesPedigreeFunction.head(10), df.shape) #(768, 9)

arr = df.values
x = arr[:, 0:8] #matrix
print(x[:3], x.shape)

y = arr[:, 8] #vector
print(y[:3], y.shape)

#sklearn  LogisticRegression을 사용하기 위해 dataframe형식을 matrix와 vector로 바꿔줌

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size = 0.33,
                                                                    random_state = 7)
print(x_train.shape, x_test.shape) #(514, 8) (254, 8) 의 비율로 나눔
"""
model = LogisticRegression()
model.fit(x_train, y_train)
print('예측값 : ', model.predict(x_test[:5]))
print('실제값 : ', y_test[:5])
#예측값 :  [0. 1. 1. 0. 0.]
#실제값 :  [0. 1. 1. 0. 1.]

#LogisticRegression은 score로 정확도를 계산할 수가 있다
print((model.predict(x_test) != y_test).sum()) #같지 않은 갯수의 합
#254개의 예측값 중에 54개가 다름
print('test로 분류한 데이터의 정확도 : ', model.score(x_test, y_test)) #0.787
print('train으로 분류한 데이터의 저확도 : ', model.score(x_train, y_train)) #0.774
#test와 train의 두 값의 차이가 크면 과적합. 적당한 차이는 있을 수 있다. 모델의 성능이 좋은 것은 아님.
#샘플 데이터의 칼럼을 선택하여 고르면 정확도가 올라갈 수 있다.


#방식은 다르더라도 값은 같게 나온다
from sklearn.metrics import accuracy_score
pred = model.predict(x_test)
print('분류 정확도 : ', accuracy_score(y_test,pred)) #0.787

#모델의 분류 성능이 목표치에 도달했다면 모델을 저장 후 저장된 모델로 분류 결과 예측
pickle.dump(model, open('pima_model.sav', 'wb'))
"""

#모델을 매번 실행할 때마다 학습 시킬 수가 없으니(시간이 오래 걸림) 어느정도 학습된 모델을 저장하여 불러서 사용
model = pickle.load(open('pima_model.sav', 'rb'))
print('test로 분류한 데이터의 정확도 : ', model.score(x_test, y_test))

print(x_test[:1]) #분류를 원하는 새로운 데이터라고 가정
print('분류 예측 : ', model.predict(x_test[:1]))
 




