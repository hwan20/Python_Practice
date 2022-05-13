#SVM으로 이미지 분류
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.metrics._classification import classification_report

faces = fetch_lfw_people(min_faces_per_person = 60, color = False) #color는 흑백 기본이 False
#min_faces_per_person = 60 각 인물당 사진수는 60개로 제한
print(faces) #faces는 아스키 코드로 되어있음
#print(faces.DESCR)

print(faces.data)
print(faces.data.shape) #(1348, 2914)
print(faces.target) #[1 3 3 ... 7 3 5]
print(faces.target_names) #'Ariel Sharon' 'Colin Powell' 'Donald Rumsfeld' 'George W Bush' ....
print(faces.images.shape) #(1348, 62, 47)
print('====================================================')

#print(faces.images[1])
#print(faces.target_names[faces.target[1]])
#plt.imshow(faces.images[1], cmap='bone')
#plt.show()
#62행 47열로 이미지를 그림
#[[ 71.333336  56.        67.666664 ...  74.333336  89.666664  78.666664] ...
#각 행에 RGB 255 까지의 크기로 색상을 표시함

#여러 이미지를 한 번에 보기
fig, ax = plt.subplots(3, 5)
#print(fig) #Figure(640x480)의 크기를 가짐
#print(ax.flat)
#print(len(ax.flat))

#for i, axi in enumerate(ax.flat):
#    axi.imshow(faces.images[i], cmap='bone')
#    axi.set(xticks = [], yticks = [], xlabel = faces.target_names[faces.target[i]]) #xticks, yticks는 눈금 없에기
#plt.show()


#PCA로 이미지 차원을 축소한 후 분류 모델 작성    62행 47열을 축소하기 
m_pca = PCA(n_components = 150, whiten = True, random_state = 0) #whiten = True스케일이 작아지도록 조정
#이미지에 가장 큰 영향을 주는 150개의 주성분. 차원 축소된 데이터로 추출
x_row = m_pca.fit_transform(faces.data)
print('x_row : ', x_row, x_row.shape) #(1348, 150)
#[138.         135.66667    127.666664   ...   1.6666666    1.6666666    0.33333334] ...
#[ 1.2901428   0.8120209   1.1569177  ...  0.2896217  -0.93606  -1.4897981 ] ...
#원본 데이터에 근사 행렬 값으로 바뀜

#PCA가 선행된 데이터로 SVM 모델 작성
m_svc = SVC(C = 1)
model = make_pipeline(m_pca, m_svc) #선처리를 한 후에 분류기를 넣어놓음
#파이프라인에서 하나로 묶어서 실행
print(model)

#train / test 
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(faces.data, faces.target, random_state = 1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(1011, 2914) (337, 2914) (1011,) (337,)
#print(x_train[:1])
print(x_train[0])
print(y_train[0])

model.fit(x_train, y_train)
pred = model.predict(x_test)
print('pred : ', pred[:10]) #pred :  [1 4 1 3 3 3 7 3 3 3]
print('real : ', y_test[:10]) #real :  [1 4 1 5 3 2 7 3 1 3]

from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
mat = confusion_matrix(y_test, pred)
print('confusion matris : \n', mat)
print('accu4racy : ', accuracy_score(y_test, pred)) #0.795
print(classification_report(y_test, pred, target_names = faces.target_names))
#                   precision recall   f1-score   support
# Ariel Sharon       1.00      0.50      0.67        14
# macro avg          0.93      0.65      0.73       337


#분류 결과 시각화
fig, ax = plt.subplots(4, 6)

for i, axi in enumerate(ax.flat):
    axi.imshow(x_test[i].reshape(62, 47), cmap='bone') #차원을 축소해놨기 때문에 다시 늘려주기 위해 reshape사용
    axi.set(xticks = [], yticks = [])
    axi.set_ylabel(faces.target_names[pred[i]].split()[-1], color='black' if pred[i]==y_test[i] else 'red') 
    #맞은 건 검은색으로 표시하고 틀린 건 빨간색으로 표시
    #first name, middle name 다 빼고 last name만
plt.show()

#오차 행렬 시각화
import seaborn as sns
sns.heatmap(mat.T, square = True, annot = True, fmt = 'd', cbar = False, xticklabels = faces.target_names,
            yticklabels = faces.target_names)
plt.xlabel('real label')
plt.ylabel('predict label') #예측라벨

plt.show()











