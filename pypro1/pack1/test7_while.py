# while : continue, break

a = 0

while a < 10:
#while 1:
#while 1.5:
#while -1.5: #보통은 True, False나 1, 0을 사용
#while True: #break가 있으니 반복 수행하는 while문을 만들어도 됨
    a += 1
    if a == 5:continue #continue는 자신을 만나면 밑에 줄을 실행하지 않고 자신이 속해있는 while문 상단으로 다시 올라감
    if a == 8:break #break는 자신을 만나면 반복 수행하는 while문을 강제적으로 꺼줌
    print(a)
else:
    print("while의 정상 처리") #while문이 조건에 의해서 정상적으로 탈출하면 수행하게 하는 코드
print("while 수행 후 a : %d " %a)
    
#난수 
import random #난수를 사용하기 위해서는 import random을 해야 한다
print(random.random()) #실수
print(random.randint(1, 10)) #1~10 사이의 난수
#나오는 난수를 고정시키고 싶으면
random.seed(1) #1번에 저장된 난수와 실수만이 고정되어 출력한다    random.seed가 입력되면 밑에 입력되는 난수들도 고정된다
print(random.random())
print(random.randint(1, 10))

print()
#임의의 숫자 알아내기
num = random.randint(1,22)
while True: #무한 루프에 빠뜨려 놓고 작업한 후에 break 입력하기
    #print("1~10 사이의 컴이 가진 예상 숫자 입력 : ")
    guess = int(input("예상 숫자 입력 : ")) #input () 안에 글을 넣어서 출력할 수도 있다

    if guess == num:
        print("이걸~~맞춰?!")
        break
    elif guess < num:
        print("더 큰 수 입력")
    elif guess > num : 
        print("더 작은 수 입력")
    
    
    
    
    
    
    
    
    
    