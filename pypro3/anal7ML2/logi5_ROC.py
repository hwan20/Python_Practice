#ROC curve 모델의 성능을 파악하기 위해 그리는 그래프
#ROC(Receiver Operating Characteristic) curve는 다양한 threshold에 대한 이진분류기의 성능을 한번에 표시한 것이다.
#이진 분류의 성능은 True Positive Rate와 False Positive Rate 두 가지를 이용해서 표현하게 된다.
#ROC curve를 한 마디로 이야기하자면 ROC 커브는 좌상단에 붙어있는 커브가 더 좋은 분류기를 의미한다고 생각할 수 있다.

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

#분류 연습용 샘플용 데이터를 작성할 수가 있다 n_samples
x, y = make_classification(100, n_features = 2, n_redundant = 0, random_state = 123) #샘플 수 100개 독립 변수 2개
print(x[:3])
print(y[:3]) #[1 0 0]

#모델을 작성하여 값을 예측함
model = LogisticRegression().fit(x, y)
y_hat = model.predict(x)
print('y_hat : ', y_hat[:3]) #[0 0 0] 하나의 예측이 틀림
print()

f_value = model.decision_function(x) #결정함수(판별함수) : 불확실성 추정함수 - 판별 경계선 설정을 위함
print('f_value : ', f_value[:10])
df = pd.DataFrame(np.vstack([f_value, y_hat, y]))
#print(df[:3])
print(df.head(3))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y, y_hat)) #logi4_iris에서는 crosstab을 사용해서 만든 것을 간단하게 만듬
#[[44  4]
# [ 8 44]]

#정리의 의미로 보여주는 것 이렇게 작성 안 해도 함수로 나와있음
acc = (44 + 44) / 100 #TP + TN / 전체수  정밀도 Accuracy
recall = 44 / (44 + 4) #TP / TP + FN  재현도 Recall
precision = 44 / (44 + 8) #TP / TP + FP  정밀도 Precision
specificity = 44 / (8 + 44)#TN / (FP + TN) 특이도 Specificity
fallout = 8 / (8 + 4)#FP / (FP + TN)  위양성율(틀린 값에 대해서 모델이 잘못 예측한 비율)

print('acc(정밀도) : ', acc)
print('recall(재현도) : ', recall) #TPR : 전체 양성 샘플 중에 양성으로 예측된 것의 비율
print('specificity(특이도) : ', specificity)
print('fallout(위양성율) : ', fallout) #FPR(1- specificity) : 전체 음성 샘플 중에 양성으로 잘못 예측된 것의 비율
#TPR은 1에 가까울 수록 좋고 FPR은 0에 가까울 수록 좋다
#make_classification은 샘플용이라 데이터가 잘 나온다
print()


#중요한건 모델을 만들어서 나온 값으로 아래와 같이 값을 가져오는 것

from sklearn import metrics
ac_sco = metrics.accuracy_score(y, y_hat)
print('ac_sco : ', ac_sco) #정밀도 acc

cl_rep = metrics.classification_report(y, y_hat)
print('cl_rep : ', cl_rep)
print()

fpr, tpr, thresholds = metrics.roc_curve(y, model.decision_function(x))
print('fpr : ', fpr)
print('tpr : ', tpr)
print('분류결정 임계값 thresholds : ', thresholds)


#ROCcurve 시각화
import matplotlib.pyplot as plt
plt.plot(fpr, tpr, 'o-', label = 'LogisticRegression')
plt.plot([0, 1], [0, 1], 'k--', label = 'random classifier line(AUC:0.5)')
plt.plot([fallout], [recall], 'r+', ms=20)
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC curve')
plt.legend()
plt.show()

#AUC(Area Under the ROC Curve)는 ROC curve의 밑면적을 말한다.
#성능 평가에 있어 수치적인 기준이 될 수 있는 값으로, 1에 가까울 수록 그래프가 좌상단에 근접하게 되므로 좋은 모델이라고 할 수 있다.
print('AUC : ', metrics.auc(fpr, tpr)) #0.9547

#분류모델에서 ROC 커브에서 Accuracy, Precision, Recall 분류해야함
#ROC커브에서 왼쪽 위로 붙을 수록 좋음

#해석 : 





