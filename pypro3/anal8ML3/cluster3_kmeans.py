#비계층적 군집분석 : k-means - 평균을 새로운 기준으로 갱신해가며 군집화 

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs #클러스터에는 make_blobs를 사용

x, y = make_blobs(n_samples = 150, n_features = 2, centers = 3, 
                  cluster_std = 0.5, shuffle = True, random_state = 0)
#print(x)
#print(y) #안 씀
print(x[:3], x.shape) #(150, 2)

plt.scatter(x[:, 0], x[:, 1], s = 50, c = 'gray', marker = 'o') #0열 값과 1열 값을 가지고 함
plt.grid()
plt.show() #make_blobs를 사용해서 3개의 군집으로 나뉘어져있다

from sklearn.cluster import KMeans
#init_centroid = 'random' #초기 클러스터 중심점. 임의로 선택
init_centroid = 'k-means++' #초기 클러스터 중심점을 할당하고, 나머지 후속 중심을 멀리 떨어뜨려 중심을 선택   주로 이 방법으로 선택

kmodel = KMeans(n_clusters = 3, init = init_centroid, random_state = 0).fit(x)
pred = kmodel.predict(x) #비지도 학습이라 y값이 없음

print('pre : ', pred)
print('-----------------------------------')
#print(x[pred == 0])
#print('-----------------------------------')
#print(x[pred == 1])
#print('-----------------------------------')
#print(x[pred == 2])
#나누는 것이 목적

print('중심점 : ', kmodel.cluster_centers_)
plt.scatter(x[pred == 0, 0], x[pred == 0, 1], s = 50, c = 'red', marker = 'o', label = 'cluster1')
plt.scatter(x[pred == 1, 0], x[pred == 1, 1], s = 50, c = 'green', marker = 's', label = 'cluster2')
plt.scatter(x[pred == 2, 0], x[pred == 2, 1], s = 50, c = 'blue', marker = 'v', label = 'cluster3')
plt.scatter(kmodel.cluster_centers_[:, 0], kmodel.cluster_centers_[:, 1],
            s = 100, c = 'black', marker = '+', label = 'center')
plt.legend()
plt.grid()
plt.show()

#k값을 얼마를 줘야 하는지?
#방법 1. 엘보우 기법(elbow) 클러스터 간 SSE의 차이를 이용해 최적의 클러스터 수를 제시(그림으로)

def elbow_func(x):
    sse = []
    for i in range(1, 11):
        km = KMeans(n_clusters = i, init = init_centroid, random_state = 0).fit(x)
        sse.append(km.inertia_)
    plt.plot(range(1, 11), sse, marker = 'o')
    plt.xlabel('cluster')
    plt.ylabel('sse')
    plt.show()

elbow_func(x) #그래프의 경사가 급격히 떨어지다가 완만하게 떨어지는 구간을 구함 i가 3일 때

#방법 2. 실루엣 기법(silhoutte) 클러스터의 품질을 정량적으로 계산해 표현

'''
실루엣(silhouette) 기법
  클러스터링의 품질을 정량적으로 계산해 주는 방법이다.
  클러스터의 개수가 최적화되어 있으면 실루엣 계수의 값은 1에 가까운 값이 된다.
  실루엣 기법은 k-means 클러스터링 기법 이외에 다른 클러스터링에도 적용이 가능하다
'''

import numpy as np
from sklearn.metrics import silhouette_samples
from matplotlib import cm

# 데이터 X와 X를 임의의 클러스터 개수로 계산한 k-means 결과인 y_km을 인자로 받아 각 클러스터에 속하는 데이터의 실루엣 계수값을 수평 막대 그래프로 그려주는 함수를 작성함.
# y_km의 고유값을 멤버로 하는 numpy 배열을 cluster_labels에 저장. y_km의 고유값 개수는 클러스터의 개수와 동일함.

def plotSilhouette(x, pred):
    cluster_labels = np.unique(pred)
    n_clusters = cluster_labels.shape[0]   # 클러스터 개수를 n_clusters에 저장
    sil_val = silhouette_samples(x, pred, metric='euclidean')  # 실루엣 계수를 계산
    y_ax_lower, y_ax_upper = 0, 0
    yticks = []

    for i, c in enumerate(cluster_labels):
        # 각 클러스터에 속하는 데이터들에 대한 실루엣 값을 수평 막대 그래프로 그려주기
        c_sil_value = sil_val[pred == c]
        c_sil_value.sort()
        y_ax_upper += len(c_sil_value)

        plt.barh(range(y_ax_lower, y_ax_upper), c_sil_value, height=1.0, edgecolor='none')
        yticks.append((y_ax_lower + y_ax_upper) / 2)
        y_ax_lower += len(c_sil_value)

    sil_avg = np.mean(sil_val)         # 평균 저장
    plt.axvline(sil_avg, color='red', linestyle='--')  # 계산된 실루엣 계수의 평균값을 빨간 점선으로 표시
    plt.yticks(yticks, cluster_labels + 1)
    plt.ylabel('클러스터')
    plt.xlabel('실루엣 개수')
    plt.show() 


#그래프를 보면 클러스터 1~3 에 속하는 데이터들의 실루엣 계수가 0으로 된 값이 아무것도 없으며, 실루엣 계수의 평균이 0.7 보다 크므로 잘 분류된 결과라 볼 수 있다.

X, y = make_blobs(n_samples=150, n_features=2, centers=3, cluster_std=0.5, shuffle=True, random_state=0)
km = KMeans(n_clusters=3, random_state=0) 
y_km = km.fit_predict(X)

plotSilhouette(X, y_km)












