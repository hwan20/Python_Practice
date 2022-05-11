#앙상블 학습(Ensemble Learning)은 여러 개의 분류기를 생성하고,
#그 예측을 결합함으로써 보다 정확한 예측을 도출하는 기법을 말합니다.
#강력한 하나의 모델을 사용하는대신 보다 약한 모델 여러개를 조합하여
#더 정확한 예측에 도움을 주는 방식입니다.
#현실세계로 예를 들면, 어려운 문제를 해결하는데 한 명의 전문가보다
#여러명의 집단지성을 이용하여 문제를 해결하는 방식을 앙상블 기법이라 할 수 있습니다.

#LogisticRegression과 DecisionTreeClassification, KNN 분류기로 앙상블 분류기 작성

import pandas as pd
from sklearn.datasets import load_breast_cancer #sklearn에 기본적으로 제공되는 학습용 데이터 베이스
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#LogisticRegression, KNeighbors, DecisionTree 3가지를 묶어서 VotingClassifier를 만들어 사용함
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

cancer = load_breast_cancer()
#print(cancer.DESCR)
print(cancer.keys()) #key, value로 저장되어 있는 cancer의 key를 뽑아옴
data_df = pd.DataFrame(cancer.data, columns = cancer.feature_names)
print(data_df) #[569 rows x 30 columns]

x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size = 0.2,
                                                    random_state = 12)

#개별 분류기 생성
logi_regression = LogisticRegression()
knn = KNeighborsClassifier(n_neighbors = 3) #옵션으로 n_neighbors 꼭 줘야함
dec_model = DecisionTreeClassifier()

#위의 3가지 모델로 voting model을 만듦
voting_model = VotingClassifier(estimators=[('LR', logi_regression), ('KNN', knn), ('Decision', dec_model)],
                                voting = 'soft')

#hard와 soft가 있음 Voting모델은 hard가 기본 옵션
#hard는 soft는 투표해서 정함

classifiers = [logi_regression, knn, dec_model] 

for classifier in classifiers: #개별 모델의 학습 및 평가
    
    classifier.fit(x_train, y_train) #학습
    pred = classifier.predict(x_test) #검정 실제 검증할 때 예측
    class_name = classifier.__class__.__name__ #클래스의 이름을 얻을 수가 있다
    print('{} 정확도 : {:.4f} '.format(class_name, accuracy_score(y_test, pred)))



voting_model.fit(x_train, y_train) #앙상블 기법을 쓴 방법 위에는 따로 따로 3가지를 for문을 돌려서 뽑음
vpred = voting_model.predict(x_test)
print('voting_model 정확도 : {:.4f}'.format(accuracy_score(y_test, vpred)))


#LogisticRegression 정확도 : 0.9386 
#KNeighborsClassifier 정확도 : 0.8947 
#DecisionTreeClassifier 정확도 : 0.9123

#voting_model 정확도 : 0.9474


