#Deep Learning library : TensorFlow

#텐서플로우의 이해
import tensorflow as tf
print(tf.__version__) #tf의 버전을 볼 수가 있다
#2022-05-17 12:17:18.603390: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cudart64_110.dll'; dlerror: cudart64_110.dll not found
#2022-05-17 12:17:18.604339: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
#gpu가 없어서 warning가 나는것

#상수 정의
print(1, type(1))
print([1], type([1]))
print(tf.constant(1), type(tf.constant(1))) #shape=() scalar 0 D tensor
#EagerTensor 즉시 실행 가능한 이라는 뜻. 버전 1에서는 즉시 실행이 불가능했음
print(tf.constant([1])) #shape=(1,) vector 1 D tensor
print(tf.constant([[1]])) #shape=(1, 1) matrix 2 D tensor
#이후에 나오는 것은 n tensor
print(tf.rank(tf.constant([[1]]))) #2차원
#상수 설정은 constant로 함

a = tf.constant([1, 2])
b = tf.constant([3, 4])
c = a + b
print(c, type(c)) #[4 6]
c = tf.add(a, b) #add외에 다른 것도 있다
print(c, type(c)) #[4 6]
#d = tf.constant([3])
#d = tf.constant(3)
d = tf.constant([[3]]) #[[7 9]] 큰 차원에 맞춰줌
e = c + d #broadcast 연산
print(e)
print('-----------------------------------------------')

print(7, type(7))
print(tf.convert_to_tensor(7, dtype=tf.float32)) #tf.Tensor(7.0, shape=(), dtype=float32)
print(tf.cast(7, dtype=tf.float32))
print(tf.constant(7.0))
print(tf.constant(7, dtype=tf.float32))
print('-----------------------------------------------')

import numpy as np
arr = np.array([1, 2, 3])
print(arr, type(arr)) #[1 2 3] <class 'numpy.ndarray'>
#arr = [1, 2, 3] 이렇게 하면 list형식 list는 속도가 느리다
tfarr = tf.add(arr, 5)
print(tfarr) #tf.Tensor([6 7 8], shape=(3,), dtype=int32)
#ndarray에서 tensor로 바뀜
print(tfarr.numpy()) #[6 7 8] 다시 ndarray로 돌아옴 numpy type으로 형변환 (강제)
print(np.add(tfarr, 3)) #[ 9 10 11] numpy 타입으로 형변환 numpy type으로 형변환 (자동)
print(list(tfarr.numpy())) #[6, 7, 8]
#대부분 사용하는 것은 numpy 기반 list 
