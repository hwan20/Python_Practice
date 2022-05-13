#BMI 지수를 계산하는 모델을 만듦
#모델을 만들기 위해서는 데이터의 양이 많아야 됨
#우리가 직접 데이터를 만들어서 모델을 만들어 보기

#BMI식을 이용해 dataset을 작성 후 SVM 분류 모델을 생성
#데이터로 모델을 만든 후 수식을 이용하여 BMI지수를 계산하는 것이 아니고
#분류하여 BMI지수를 나눔

#BMI식 = 몸무게(kg) / 키(m)^2
print(70 / ((175/100)*(175/100))) #내 BMI 22.857

"""
#BMI식을 이용해 무작위 자료 작성
import random

def calc(h, w):
    bmi = w / (h/100)**2
    if bmi < 18.5 :
        return 'thin'
    elif bmi < 25.0 :
        return 'normal'
    else : 
        return 'fat' 
    
print(calc(175, 70)) #normal

fp = open('bmi.csv','w')
fp.write('height,weight,label\n')
cnt = {'thin':0,'normal':0,'fat':0}

#난수를 생성하고 50000번의 반복문을 돌면서 데이터를 입력시킴
random.seed(12)
for i in range(50000):
    h = random.randint(150, 200) # 키는 150부터 200까지의 랜덤한 난수
    w = random.randint(35, 100) # 몸무게는 35부터 100까지의 랜덤한 난수
    label = calc(h, w) #키와 무게를 함수에 입력한 후 리턴된 결과값을 label에 받음
    cnt[label] += 1 #??
    fp.write('{0},{1},{2}\n'.format(h, w, label)) #리턴받은 결과값을 엑셀 칸에 하나씩 집어넣음 

fp.close()
"""



#SVM분류 모델을 적용
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tbl = pd.read_csv('bmi.csv')
print(tbl.head(3))

label = tbl['label']

#weight, height는 정규화
w = tbl['weight']/100
print(w[:3])
h = tbl['height']/200
print(h[:3])
wh=pd.concat([w, h], axis = 1)
print(wh.head(3), wh.shape)
print(label[:3], label.shape)
print('==============================')
label = label.map({'thin':0,'normal':1,'fat':2}) #dummy 범주형 자료를 숫자값으로
print(label[:3]) #dummy로 변환하지 않아도 된다 숫자로 바꾸면 컴퓨터가 처리하기 편하니 속도가 빨라진다

data_train, data_test, label_train, label_test = train_test_split(wh, label, random_state = 1)
print(data_train.shape, data_test.shape, label_train.shape, label_test.shape) #(37500, 2) (12500, 2) (37500,) (12500,)

#model = svm.SVC(C = 1).fit(data_train, label_train)
model = svm.LinearSVC(C=1).fit(data_train, label_train)

pred = model.predict(data_test)
print('실제값 : ', label_test[:10].values) #[2 0 1 1 0 0 2 1 0 0]
print('예측값 : ', pred[:10]) #[2 0 1 1 0 0 2 2 0 0]

print('정확도 : ', metrics.accuracy_score(label_test, pred)) #0.93784
print(metrics.classification_report(label_test, pred))

tbl2 = pd.read_csv('bmi.csv', index_col = 2)
print(tbl2.head(2))
def scatter_func(lbl, color):
    b = tbl2.loc[lbl]
    plt.scatter(b['weight'], b['height'], c = color, label = lbl)


scatter_func('fat', 'red')
scatter_func('normal', 'yellow')
scatter_func('thin', 'blue')
plt.legend()
plt.show()






"""
# SVM 분류 모델을 적용
from sklearn import svm,metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tbl = pd. read_csv('bmi2.csv')
print(tbl.head(3))

label = tbl['label']

# weight, height는 정규화
w = tbl['weight'] / 100
print(w[:3])
h = tbl['height'] / 200
print(h[:3])
wh = pd.concat([w,h],axis=1)
print(wh.head(3),wh.shape)
print(label[:3],label.shape)
label = label.map({'thin':0,'normal':1,'fat':2,}) # dummy
print(label[:3])

data_train,data_test,label_train,label_test=train_test_split(wh,label,random_state=1)
print(data_train.shape,data_test.shape,label_train.shape,label_test.shape) # (37500, 2) (12500, 2) (37500,) (12500,)
# print(data_train[:3])

# model = svm.SVC(C=1).fit(data_train,label_train)
model = svm.LinearSVC(C=1).fit(data_train,label_train)

pred = model.predict(data_test)
print('실제값 :',label_test[:10].values)
print('예측값 :',pred[:10])

print(metrics.accuracy_score(label_test,pred))
print(metrics.classification_report(label_test,pred))

tbl2 = pd. read_csv('bmi.csv',index_col = 2)
print(tbl2.head(2))
def scatter_func(lbl,color):
    b = tbl2.loc[lbl]
    plt.scatter(b['weight'],b['height'],c=color,label=lbl)

scatter_func('fat','red')
scatter_func('normal','yellow')
scatter_func('thin','blue')
plt.legend()
plt.show()
"""
