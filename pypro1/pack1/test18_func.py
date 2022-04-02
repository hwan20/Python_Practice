#재귀함수(recursive function) : 함수가 자기 자신을 호출

def countDown(n):
    if n == 0:
        print("완료")
    else:
        print(n, end = " ")
        countDown(n-1) #자기 자신을 호출
    
countDown(5)

print()

def tot(n):
    if n==1:
        print("탈출")
        return True #빠져나옴
    return n+tot(n-1) #n이 1이 아니라 if문을 가지 않고 return에 들어가게 되는데 이때 자기 자신을 호출하여 빠져나가지 않고 계속 반복하게 됨

res = tot(10) #res가 tot의 수행 결과를 만남
print("10까지의 합은", res)

print()
#factorial : 1부터 어떤 양의 정수 n까지의 정수를 모두 곱한 것 ex) 5!  5*4*3*2*1
def facFunc(a):
    if a == 1: return 1 #a가 1이되면 함수를 빠져나가게 되는데 1은 곱하나 마나이니 1때 나감
    print(a)
    return a*facFunc(a-1) #자기 자신을 호출함. 현재 a의 값과 a-1의 값을 곱함 반복하며 이런식으로 1까지 곱하게 됨

print("5! : " ,facFunc(5))

print("종료")







