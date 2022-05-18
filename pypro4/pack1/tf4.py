#연산자, 함수

#add, subtract, multiply, divide
#삼항연산

import numpy as np
import tensorflow as tf

f1 = lambda : tf.constant(1)
print(f1())

f2 = lambda : tf.constant(2)
a = tf.constant(3)
b = tf.constant(4)

#case 조건문
result = tf.case([(tf.less(a, b), f1)], default = f2) #if(a < b) return f1 else return f2 이런 뜻
#greater ~~보다 크다 less ~~보다 작다 tf.less(a, b) a는 b보다 작다
print(result.numpy()) #a는 b보다 작으니 f1을 출력
print('---------------------------------')


#관계 / 논리 연산
print(tf.equal(1, 2).numpy()) #False
print(tf.not_equal(1, 2)) #tf.Tensor(True, shape=(), dtype=bool)
print(tf.less(1, 2)) #tf.Tensor(True, shape=(), dtype=bool)
print(tf.greater(1, 2)) #tf.Tensor(False, shape=(), dtype=bool)
print(tf.greater_equal(1, 2)) #tf.Tensor(False, shape=(), dtype=bool) 

print(tf.logical_and(True, False).numpy()) #False
print(tf.logical_or(True, False).numpy()) #True
print(tf.logical_not(True, False).numpy()) #False
print('---------------------------------')


#tf.reduce 차원 축소
ar = [[1, 2], [3, 4]] #2차원 매트릭스
print(tf.reduce_sum(ar)) #합을 구하는데 차원을 떨어뜨림  10 
print(tf.reduce_mean(ar)) #전체 평균
print(tf.reduce_mean(ar, axis = 0)) #열 기준
print(tf.reduce_mean(ar, axis = 1)) #행 기준



