#심장병 환자 데이터를 사용하여 분류 정확도 분석 연습
#https://www.kaggle.com/zhaoyingzhu/heartcsv
#https://github.com/pykwon/python/tree/master/testdata_utf8         Heartcsv

#Heart 데이터는 흉부외과 환자 303명을 관찰한 데이터다. 
#각 환자의 나이, 성별, 검진 정보 컬럼 13개와 마지막 AHD 칼럼에 각 환자들이 심장병이 있는지 여부가 기록되어 있다. 
#dataset에 대해 학습을 위한 train과 test로 구분하고 분류 모델을 만들어, 모델 객체를 호출할 경우 정확한 확률을 확인하시오. 
#임의의 값을 넣어 분류 결과를 확인하시오.     
#정확도가 예상보다 적게 나올 수 있음에 실망하지 말자. ㅎㅎ

#feature 칼럼 : 문자 데이터 칼럼은 제외
#label 칼럼 : AHD(중증 심장질환)

#데이터 예)
#"","Age","Sex","ChestPain","RestBP","Chol","Fbs","RestECG","MaxHR","ExAng","Oldpeak","Slope","Ca","Thal","AHD"
#"1",63,1,"typical",145,233,1,2,150,0,2.3,3,0,"fixed","No"
#"2",67,1,"asymptomatic",160,286,0,2,108,1,1.5,2,3,"normal","Yes"



# SVM 연습문제 
import pandas as pd 
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

# 데이터 가공 
heartdata = pd.read_csv("../testdata/Heart.csv")
print(heartdata.info())
data = heartdata.drop(["Thal", "ChestPain"], axis = 1) # object type은 제외
data.loc[data.AHD=="Yes", 'AHD'] = 1
data.loc[data.AHD=="No", 'AHD'] = 0

print(heartdata.isnull().sum())      # Ca에 4개
Heart = data.fillna(data.mean())     # CA의 결측치는 평균으로 대체
label = Heart["AHD"]
features = Heart.drop(["AHD"], axis = 1)

# 훈련, 검정 데이터로 나누기 
data_train, data_test, label_train, label_test = \
    train_test_split(features, label, test_size = 0.3, random_state = 12)

model = svm.LinearSVC(C=10).fit(data_train, label_train)

# 예측치 구하기 
import numpy as np
pred = model.predict(data_test)
print('예측값 : ', pred[:10])
print('실제값 : ', np.array(label_test)[:10])

print(model.score(data_train, label_train))
print(model.score(data_test, label_test))
print('분류 정확도 : ', metrics.accuracy_score(label_test, pred))
