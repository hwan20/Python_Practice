#MLP : 다층신경망 노드의 갯수를 복수로 준다 - 선형 / 비선형 분류가 가능하다
#breast_cancer dataset을 사용

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

x = cancer.data
y = cancer.target
print(x[:2])
print(y[:2])
print(cancer.target_names) #['malignant' 'benign'] 양성과 악성 두 가지

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 42, test_size = 0.3)

#데이터의 크기가 제각각이니 정규화나 표준화로 스케일링
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train)
scaler.fit(x_test)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
print(x_train[:1])

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(10), max_iter = 10, learning_rate_init = 1, 
                    solver = 'adam', random_state = 1, verbose = 1)#adam 코스트를 미니마이즈 하기 위해
mlp.fit(x_train, y_train)
#verbose = 1 진행 과정을 콘솔창에 보여줌 안 쓰면 디폴트값 0 진행 과정을 볼 필요가 없으니 대부분 0을 준다. 2는 tensorflow에서 쓰임
#hidden_layer_sizes의 노드 수를 몇 개를 줄 것이냐, 레이어의 갯수를 몇 개를 줄 것이냐
#max_iter의 학습수를 어떻게 줄 것이냐
#learning_rate_init를 어떻게 줄 것이냐 등을 통해 결과를 가져올 수가 있다

pred = mlp.predict(x_test)
print('실제 값 : ', y_test[:10]) #[1 0 0 1 1 0 0 0 1 1]
print('예측 값 : ', pred[:10]) #[1 0 0 1 1 0 0 0 1 1]
print('acc(train) : ', mlp.score(x_train, y_train)) #0.97738
print('acc(test) : ', mlp.score(x_test, y_test)) #0.98830


