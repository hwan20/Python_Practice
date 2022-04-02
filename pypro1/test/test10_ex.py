# 문1) 2~9단 모두 출력
"""
for a in range(2,10):
    #print(a)
    for b in range(1,10):
        print("%d * %d = %d" %(a,b,a*b))


# 문2) 1~100 사이의 정수 중 3의 배수이면서 5의 배수의 합 출력
b=0
for a in range(1,101):
    #print(a)
    if a%3==0 and a%5==0:
        b+=a
        
print(b)
"""    
    
    

# 문3) 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수인 경우만 출력
#예) 1 3
#예) 2 2
#예) 2 6
"""
import random

a=random.randint(1, 6)
b=random.randint(1, 6)

for c in range(1) :
    
    #print(a)
    #print(b)
    if (a+b)%4==0:
        print("%d+%d=%d"%(a,b,a+b))
"""

for d in range(1,7):
    #print(d)
    for e in range(1,7):
        #print(e+d)
        if (e+d)%4==0:
            print("{} * {} = {}".format(d,e,d+e))







