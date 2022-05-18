#단순 선형회귀 모델 생성 : 
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#하이테크적 기법을 사용하려면 이렇게 작성해야 함. 직접 작성해서 융통성이 있음
opti = tf.keras.optimizers.SGD() #SGD대신에 RMSProp, Adam 사용 가능 (코스트를 미니마이즈 하는 기능) 단점을 보완한게 Adam
#기능이 좋은 Adam~ 나쁜 SGD 경사하강법. 
w = tf.Variable(tf.random.normal((1, )))
b = tf.Variable(tf.random.normal((1, )))
print(w.numpy())
print(b.numpy())

@tf.function
def train_step(x, y):
    with tf.GradientTape() as tape: #자동으로 미분 계산을 해줌
        hypo = tf.add(tf.multiply(w, x), b) #1차 방정식으로 예측값 hypo 구함
        loss = tf.reduce_mean(tf.square(tf.subtract(hypo, y))) #예측값 hypo과 실제값 y의 차이의 제곱의 평균
    
    #loss값 미분을 해야함
    grad = tape.gradient(loss, [w, b]) #편미분이 수행이 됨 - 딥러닝에서는 편미분
    opti.apply_gradients(zip(grad, [w, b])) #튜플로 grad와 [w, b]가 쌍을 이룸
    
    return loss

x = [1., 2., 3., 4., 5.] #feature
y = [1.2, 2.0, 3.0, 3.5, 5.5] #label
print(np.corrcoef(x, y)) #0.97494708


w_val = []
cost_val = []

for i in range(101):
    loss_val = train_step(x, y)
    cost_val.append(loss_val.numpy())
    w_val.append(w.numpy())
    if i % 10 == 0:
        print(loss_val)

print(cost_val)
print(w_val)


plt.plot(w_val, cost_val, 'o')
plt.xlabel('w')
plt.ylabel('cost')
plt.show()

print('cost가 최소일 때 w : ', w.numpy())
print('cost가 최소일 때 b : ', b.numpy())

y_pred = tf.multiply(x, w) + b #y = wx + b
print('예측값 : ', y_pred.numpy())
print('실제값 : ', y)

plt.plot(x, y, 'ro', label='real')
plt.plot(x, y_pred, '-b', label = 'pred')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print('---------------------------------')
#미지의 새로운 값으로 y를 예측
new_x = [3.5, 9.0]
new_pred = tf.multiply(new_x, w) + b
print('새로운 값으로 y를 예측 : ', new_pred.numpy())




