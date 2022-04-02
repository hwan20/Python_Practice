
#맷팅과 기본 연산 연습
i=14; n=i//3; m=i%3; age=30; name="최일환"
#% 포맷팅 연습
print("14를 3으로 나눈 몫은 %d이며, 나머지는 %d이다" %(n,m) )
print("내 나이는 %d이야" %age)
print("내 나이는 %s이고 이름은 %s이야" %(age, name))

#.format 연습
print()
print("14를 3으로 나눈 몫은 {0}이며, 나머지는 {1}이다" .format(n, m))
print("내 나이는 {}이야".format(age))
print("내 나이는 {0}이고 이름은 {1}이야".format(age, name))
print("내 나이는 {}이고 이름은 {}이야".format(age, name))

#f-string 연습
print()
print(f"14를 3으로 나눈 몫은 {n}이며, 나머지는{m}이다")
print(f"내 나이는 {age}이야")
print(f"내 나이는 {age}이고 이름은 {name}이야")

# 문자열 구하는 len
print()
a="I need python study It's to hard"
print(len(a))
print(a[3])
b=a[2]+a[-3]+a[5]+a[-3]
print(b)
print(a[2:6])

#if문 연습
print()
a="가나다라마바사"
#print(len(a))
b=6 if len(a)<6 else 7

print(b)

print()
a=[0,1,2,3,4,5,6]

b=True if a[0]==0 else False
print(b)

print()
a=7
if a<4:
    print("a는 %s 보다 작다" %4)
elif a<10:
    print("a는 %s 보다 크고 %s보다 작다" %(4, 10))
else:
    print("a는 %s보다 크다" %10)

print()
print("a는 4보다 작다" if a<4 else "a는 4 보다 크고 10보다 작다" if a<10 else "a는 10보다 크다" )


i=1; j=1

while i <= 10:
    while j<=i:
        print("*"*j)
        j += 1
    i += 1

#난수 연습하기
print()
import random
print(random.random())
print(random.randint(1, 4))

random.seed(2)

print(random.random())
print(random.randint(1, 10))







