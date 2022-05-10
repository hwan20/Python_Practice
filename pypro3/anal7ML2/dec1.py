#DecisionTree(의사결정 나무)
#DecisionTree는 classification과 regression 모두 가능하나 분류 모델로 더 많이 사용된다
#DecisionTree는 여러 가지 규칙을 순차적으로 적용하면서 독립 변수 공간을 분할하는 분류 모형이다

import collections
from sklearn import tree

x = [[180, 15], [177, 42], [156, 35], [174, 5], [166, 33], [170, 12], [171, 7]]
y = ['man', 'woman', 'woman', 'man', 'woman', 'man', 'woman']
label_names = ['height', 'hair length']

#모델을 만들어 예측값을 계산
model = tree.DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
#entropy 데이터 집합의 혼잡도 더 이상 나눌 수가 없으면 entropy가 낮다
model.fit(x, y)
pred = model.predict(x)
print(pred)
#예측값 ['man' 'woman' 'woman' 'man' 'woman']

mydata = [[171, 18]]
new_pred = model.predict(mydata)
print('mydata에 대한 예측 결과 : ', new_pred)

#DecisionTree 는 시각화 하려면 별도의 창을 띄어야 하기 때문에 프로그램을 깔아야 함
#graphviz, pydotplus
#그래프를 만드는 형식은 아래와 같다

import pydotplus

dot_data = tree.export_graphviz(model, feature_names = label_names,
                                out_file = None, filled = True, rounded = True)
graph = pydotplus.graph_from_dot_data(dot_data)
colors = ('red', 'orange')
edges = collections.defaultdict(list)
print(edges, type(edges)) #defaultdict(<class 'list'>, {}) <class 'collections.defaultdict'>

for e in graph.get_edge_list():
    edges[e.get_source()].append(int(e.get_destination()))

print(edges) #{'0': [1, 2]})

for e in edges:
    edges[e].sort()
    for i in range(2):
        dest = graph.get_node(str(edges[e][i]))[0]
        dest.set_fillcolor(colors[i])

graph.write_png('tree.png')

#파일 불러오기

import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

img = imread('tree.png')
plt.imshow(img)
plt.show()











