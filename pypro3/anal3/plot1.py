#시각화 : 많은 양의 데이터를 효율적으로 봄으로써 인사이트를 정확하게 얻어 낼 수 있다

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic') #한글이 깨지니 보여지도록 하기 위해 하지만 이것만 주면 -값이 깨짐
plt.rcParams['axes.unicode_minus'] = False #한글이 안 깨지게 하니 깨지는 -를 안 깨지도록 하는

x = ["서울", "인천", "수원"] #set은 순서가 없어서 X
y = [5, 3, 7]

plt.plot(y)
plt.xlim([-1, 3]) #x축의 크기를 정함
plt.ylim([0, 10]) #y축의 크기를 정함
plt.yticks(list(range(0, 11, 3))) #y의 ticks(표현되는 숫자) 를 정해줌
plt.plot(x, y) #x에 서울, 인천, 수원이 들어오는 것은 한글이 들어오는게 아니고 문자에 대한 index값이 들어옴
plt.show()

#data = np.arange(1, 11, 2)
#print(data)
#plt.plot(data)
#x = [0, 1, 2, 3, 4]
#for a, b in zip(x, data):
#    plt.text(a, b, str(b))
#plt.show()

#sin곡선
#x = np.arange(10)
#y = np.sin(x)
#print(x, y)
#plt.plot(x, y)
#plt.plot(x, y, 'bo')
#plt.plot(x, y, 'r')
#plt.plot(x, y, 'r+')
#plt.plot(x, y, 'go')
#plt.plot(x, y, 'go--')
#plt.plot(x, y, 'go--', linewidth=2) #lw = 2
#plt.plot(x, y, 'go--', linewidth=2, markersize=12) #marker = 'o' , c = 'g'
#plt.plot(x, y, 'go-.', linewidth=2, markersize=12)
#plt.plot(x, y, 'go:', linewidth=2, markersize=12) #여러 가지 다양한 옵션이 있다
#plt.show()

#hold
x = np.arange(0, np.pi * 3, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

#plt.figure(figsize=(10, 5))
#plt.plot(x, y_sin, c='r')
#plt.scatter(x, y_cos) #산점도
#plt.xlabel('x축')
#plt.ylabel('y축')
#plt.legend(['sine', 'cosine'])
#plt.show()

#subplot
#plt.subplot(2, 1, 1)
#plt.plot(x, y_sin, c='r')
#plt.title('사인 그래프')

#plt.subplot(2, 1, 2)
#plt.scatter(x, y_cos)
#plt.title('코사인 그래프')
#plt.show()

#꺾은 선 그래프
#irum = ['a', 'b', 'c', 'd', 'e']
#kor = [80, 50, 70, 70, 90]
#eng = [60, 70, 80, 70, 60]
#plt.plot(irum, kor, 'ro-')
#plt.plot(irum, eng, 'bs--')
#plt.title("시험 점수")
#plt.ylim([0, 100])
#plt.legend(['국어', '영어'], loc = 2) #loc는 legend의 글이 작성되는 위치. 1,2,3,4 시계 반대방향 순
#plt.grid(True)

#fig = plt.gcf() #그래프를 이미지로 저장
plt.show()
#fig.savefig('plot1.png')

#이렇게 저장된 이미지는 다른 곳에서 불러서 사용하기에는 이쁘지가 않음
#그래서 저장된 이미지의 데이터만 가져오고 거기서 이미지를 따로 고쳐줌

#from matplotlib.pylab import imread
#img = imread('plot1.png')
#plt.imshow(img)
#plt.show()
