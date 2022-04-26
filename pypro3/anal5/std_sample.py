#표준편차, 분산의 중요성 : 데이터의 분포를 파악할 수가 있다

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

np.random.seed(1)
print(stats.norm(loc = 1, scale = 2).rvs(10)) #10개의 샘플링을 얻음

print("---------")
centers = [1, 1.5, 2]
col = 'rgb'

std = 0.05 #표준편차  0에 가까울 수록 모여있다
datas = []

for i in range(3):
    datas.append(stats.norm(loc= centers[i], scale=std).rvs(100))
    plt.plot(np.arange(100) + i * 100, datas[i], '*', color = col[i])

plt.show()

