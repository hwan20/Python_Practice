#반복문 : while 조건

a=1

while a <= 5:
    print(a, end = " ")
    a = a + 1 #while문이 빠져나갈 문장을 주어야 한다
    
print("\nwhile 종료")

print()

i = 1
while i <= 3:
    j = 1
    while j <= 4:
        print("i:" + str(i) + ", j:" + str(j))
        j += 1
    i += 1
print("\nwhile 종료 2")

print("1~100 사이의 정수 중 3의 배수의 합")
i = 1; hap = 0
while i <= 100:
    #print(i, end="") #항상 조금씩 확인해가면서 하기
    if i%3==0: #증가된 i중에 3으로 나눈 몫이 0인 경우 즉 i가 3의 배수인 경우만
        #print(i, end="")
        hap += i
    i += 1

print("합은:", hap)

print()
colors = ["r", "g", "b"]
print(len(colors))
a = 0
while a < len(colors):
    print(colors[a], end = ":")
    a += 1

print()
while colors: #colors의 r,g,b가  모두 빠져나가서 [] 빈 공간이 되면 false가 되어 while문을 빠져나감
    print(colors.pop()) #pop은 추출 하나씩 빼내는 것 index의 뒤에서 부터 하나씩 빠져나감
    
print(len(colors)) #모두 빠져나가 colors의 크기는 0이 된다

print()
i = 1
while i <= 10:
    j = 1
    res = ""
    while j <= i:
        res = res + "*"
        j += 1
    print(res)
    i += 1






















