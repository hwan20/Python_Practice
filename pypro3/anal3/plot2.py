import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)

"""
#방법 1 : matplotlib style의 인터페이스로 시각화
plt.figure() #영역 생성
plt.subplot(2,1,1) #2행 1열로 칸을 2칸으로 나눔. panel number는 1

#칸이 2개니 sin과 cosin으로
plt.plot(x, np.sin(x))
plt.subplot(2,1,2)
plt.plot(x, np.cos(x))
plt.show()



#방법 2 : matplotlib의 객체지향 인터페이스로 시각화
fig, ax = plt.subplots(nrows=2, ncols=1) 
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
plt.show()
"""


"""
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.hist(np.random.randn(10), bins=10, alpha=0.9) #bins는 간격을 뜻하고 alpha가 0에 가까울 수록 투명
ax2.plot(np.random.randn(10))
plt.show()
"""



data = [50, 80, 100, 70, 90] #데이터의 양이 많을 때 hist, 산점도, box 등이 좋다
"""
plt.bar(range(len(data)), data) #막대형 그래프
plt.show()

err = np.random.rand(len(data)) #표준편차, 오차, 신뢰구간 등 표시
plt.barh(range(len(data)), data, xerr=err, alpha = 0.3) #가로 막대는 barh로 하면 된다
plt.show()

plt.pie(data, explode=(0, 0.1, 0, 0, 0), colors=['yellow', 'red', 'blue']) #pie모양 보여줌
plt.title('pie chart')
plt.show()


plt.boxplot(data) #데이터 분포를 알기에 적합하다
plt.show()
"""


"""
n = 30
np.random.seed(0)
x = np.random.rand(n)
y = np.random.rand(n)

color = np.random.rand(n)
#버블차트
scale = np.pi * (15 * np.random.rand(n)) ** 2 #pi값이 작으니 제곱과 곱을 함
plt.scatter(x, y, s = scale, c = color)
plt.show()
"""




#시계열 데이터 : 일정한 시간동안 순차적으로 수집하고 분류한 데이터

import pandas as pd
fdata = pd.DataFrame(np.random.randn(1000,4),
                     index=pd.date_range('1/1/2000', periods=1000),
                     columns=list('abcd'))
print(fdata.head())

fdata = fdata.cumsum()
plt.plot(fdata)
plt.show()



#pandas의 plot기능
fdata.plot()
fdata.plot(kind='bar')
fdata.plot(kind='box')
plt.xlabel('time')
plt.xlabel('data')
plt.show()

