
"""
print("연습 문제 1")

i = 1; j = 0
while i <= 100:
    #print(i, end="")
    i+=1
    if i%3==0:
        #print(i, end="")
        if i%2==1:
            print(i, end=" ")
            j+=i
print(j)

print()

print("연습 문제 2")

i = 2
while i <= 5:
    #print(i, end="")
    j = 1
    while j <= 9:
        print(i*j, end=" ")
        j += 1
    print()
    i += 1 

print()

print("연습 문제 3")

i = 11; j = 0
while i <= 99:
    #print(i, end=" ")
    j += i
    i += 1
    #while 

print(j, end=" ")

#무한루프 안 쓰고
i = 1; cnt = 1; hap = 0
while 1<100:
    if cnt % 2 == 0:
        hap += i
    else:
        k = -1 * i
        hap += k
    
    cnt += 1
    i += 2
print("합은", hap)


print()

print("연습 문제 4")

aa = 2; count = 0
while aa <= 1000:
    imsi = False
    bb = 0
    while bb <= aa - 1:
        if aa % bb == 0:
            imsi = True
        bb += 1
        
    if imsi ==False:
        print(aa, end = " ")
        count += 1

    aa += 1

print("갯수 : ", count)

"""














"""
#while문을 이용하여 출력 -> 성공하면 for 문을 이용해서도 출력해 보기


#1번 문제 1부터 100 사이의 숫자 중 3의 배수이지만 2의 배수가 아닌 수를 출력하고 합을 출력

i=0; S=0
while i<=100:
    i += 1
    if i%3==0 and i%2!=0:
        print(i,end=" ")
        S += i
    #print(i if i%3==0 and i%2!=0)
print("\n1~100까지의 숫자 중 3의 배수이면서 2의 배수가 아닌 수의 합 : %d" %S)




#2번 문제 2~5까지의 구구단 출력

i = 2

while i <= 5:
    j=1
    while j <= 9:
        print("{} * {} = {}".format(i,j,i*j))
        j+=1
    i+=1


"""



#3번 문제 -1, 3, -5, 7, -9, 11 이런 식으로 증가하는 숫자의 99까지 합을 출력


i=-1; S=0

while i<100:   
    
    if i>0 : 
        S+=i
        #print(i)
        #print(S)
        i=(i+2)*-1
        #print(i)
    else :
        S+=i
        #print(S)
        print(i)
        i=i*-1+2

    
print("합은 : %s" %S)


i = 1; cnt = 1; hap = 0
while i<100:
    if cnt % 2 == 0:
        hap += i
        #print(hap)
    else:
        k = -1 * i
        hap += k
        #print(hap)
    cnt += 1
    i += 2
print("합은", hap)    





#4번 문제 1~1000사이의 소수와 그 갯수를 출력


















