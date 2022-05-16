#sklearn 모듈이 지원하는 분류 모델 사용
#다항 분류 : 출력시 softmax 함수를 사용 - 결과가 확률값으로 출력되며 가장 큰 값의 인덱스를 분류 범주값으로 적용

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler #표준화를 지원
from sklearn.linear_model import LogisticRegression #다항분류시 사용
import pandas as pd
import numpy as np

iris = datasets.load_iris()
print(iris.DESCR)
print(iris.keys())

print(np.corrcoef(iris.data[:, 2], iris.data[:, 3])) #0.96286543 상관관계가 높다

x = iris.data[:, [2, 3]] #petal.length, petal.width
y = iris.target
print(x[:3])
print(y[:3], set(y)) #{0, 1, 2}

#train / test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(105, 2) (45, 2) (105,) (45,)

#학습 데이터 크기의 차이가 심하면 스케일링(크기 표준화 또는 정규화를 시킨다)
#독립 변수를 스케일링 하면 모델이 안정성, 수렴 속도 향상, 오버플로우/언더플로우 등의 방지에 효과적

"""
print(x_train[:3])
sc = StandardScaler() #표준화
#독립변수간에 차이가 크면 표준화를 해야 한다
sc.fit(x_train)
sc.fit(x_test)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)
print(x_train[:3])

#스케일링 원복
inver_x_train = sc.inverse_transform(x_train)
print(inver_x_train[:3])
"""

#model
#model = LogisticRegression(C = 100.0, random_state = 0, solver='lbfgs',
#                           multi_class = 'auto') #C속성 : L2규제 overfitting방지를 위한 목적으로 
#C는 값이 작을 수록 강한 정규화 규제가 진행된다 (모델에 패널티를 적용)
#multi_class = 'auto'는 소프트맥스 ??

#sklearn의 장점 api가 일관성이 있다
#from sklearn.ensemble import RandomForestClassifier
#model = RandomForestClassifier(criterion = 'entropy', n_estimators = 500, random_state = 1, n_jobs = 2)

#import xgboost as xgb
#model = xgb.XGBRFClassifier(boost = 'gbtree', n_estimators = 500, random_state = 1)

#from sklearn import svm
#model = svm.SVC(C = 1) #C의 값이 크면 overfitting됨
#model = svm.LinearSVC(C = 100) #개량된 것 속도가 향상됨 성능이 무조건적으로 좋지는 않음 데이터에 따라 다르다

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()

print(model)
model.fit(x_train, y_train) #학습 진행

#분류 예측
y_pred = model.predict(x_test)
print('예측 값 : ', y_pred)
print('실제 값 : ', y_test)

print('총 갯수 : %d, 오류 수 : %d' %(len(y_test), (y_test != y_pred).sum()))

#분류 정확도 확인
print('분류 정확도 1 : %.3f' %accuracy_score(y_test, y_pred))

con_mat = pd.crosstab(y_test, y_pred, rownames = ['예측치'], colnames = ['관측치'])
print('분류 정확도 2 :',(con_mat[0][0] + con_mat[1][1] + con_mat[2][2]) / len(y_test))

print('분류 정확도 3(test) : ', model.score(x_test, y_test))
print('분류 정확도 3(train) : ', model.score(x_train, y_train))


#모델 저장 후 읽기
import pickle
pickle.dump(model, open('cla_model.sav', 'wb'))
del model
#저장한 다음에 읽어서 할 수가 있다는 것을 보여주기 위해 저장하고 지우고 다시 읽음
read_model = pickle.load(open('cla_model.sav', 'rb'))

print('\n 새로운 값으로 예측 - petal.length, petal.width만 참여')
print(x_test[:3])
new_data = np.array([[5.1, 2.4], [0.3, 0.3], [3.4, 0.2]])

#sc.fit(new_data) #표준화 후 모델을 합습한 경우
#new_data = sc.transform(new_data)

new_pred = read_model.predict(new_data)
#print(read_model.predict_proba(new_data))
print('예측 결과 : ', new_pred)
#[[1.25746594e-11 8.81678920e-04 9.99118321e-01]
# [9.99999491e-01 5.09165588e-07 1.32715590e-21]
# [5.23769548e-03 9.94762295e-01 9.41292541e-09]]
#예측 결과 :  [2 0 1]
#다항 분류시에 행의 가장 큰 값이 있는 곳의 인덱스 번호를 가져와줌






import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import font_manager, rc

plt.rc('font', family='malgun gothic')      
plt.rcParams['axes.unicode_minus'] = False

def plot_decision_region(X, y, classifier, test_idx=None, resolution=0.02, title=''):

    markers = ('s', 'x', 'o', '^', 'v')  # 점 표시 모양 5개 정의
    colors = ('r', 'b', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    #print('cmap : ', cmap.colors[0], cmap.colors[1], cmap.colors[2])

    # decision surface 그리기
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    xx, yy = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))

    # xx, yy를 ravel()를 이용해 1차원 배열로 만든 후 전치행렬로 변환하여 퍼셉트론 분류기의 
    # predict()의 인자로 입력하여 계산된 예측값을 Z로 둔다.
    Z = classifier.predict(np.array([xx.ravel(), yy.ravel()]).T)
    Z = Z.reshape(xx.shape)   # Z를 reshape()을 이용해 원래 배열 모양으로 복원한다.

    # X를 xx, yy가 축인 그래프 상에 cmap을 이용해 등고선을 그림
    plt.contourf(xx, yy, Z, alpha=0.5, cmap=cmap)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    X_test = X[test_idx, :]
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl, 0], y=X[y==cl, 1], c=cmap(idx), marker=markers[idx], label=cl)
        
    if test_idx:
        X_test = X[test_idx, :]
        plt.scatter(X_test[:, 0], X_test[:, 1], c=[], linewidth=1, marker='o', s=80, label='testset')

    
    plt.xlabel('꽃잎 길이')
    plt.ylabel('꽃잎 너비')
    plt.legend(loc=2)
    plt.title(title)
    plt.show()

x_combined_std = np.vstack((x_train, x_test))
y_combined = np.hstack((y_train, y_test))
plot_decision_region(X=x_combined_std, y=y_combined, classifier=read_model,
                     test_idx=range(105, 150), title='scikit-learn제공')



