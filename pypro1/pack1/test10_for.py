 # 반복문 for와 range()
# range(초기치, 목적치, 증가치): 는 수열을 만들어주는 함수

print(list(range(1, 6, 1))) #1로 시작, 5까지 증가, 1씩 증가
print(list(range(1, 6))) #증가치가 1이라면 생략 가능
print(set(range(1, 6)))
print(tuple(range(1, 6)))
print(list(range(6))) #숫자 하나만 적어주면 목적치가 돼서 0부터 시작함
print(list(range(0, 6))) #위와 같음
print(list(range(1, 11, 2)))
print(list(range(0, -100, -20)))

#이게 range()의 다 for문에서 자주 쓰임

print()
for i in range(6):
    print(i, end = " ")

print()
for i in range(1, 10):  #java에서는 for(int i=1; i<=10; i++) {} 와 같음
    print("{0}*{1}={2}". format(2, i, i*2), end = " ")

print()
tot = 0
for i in range(1, 11):
    tot += i
print("1~11 합은 : " + str(tot))
print("1~11 합은 : " + str(sum(range(1, 11))))

#참고하기 n-gram : 문자열에서 n개의 연속되는 요소를 추출하기 
#문자 단위 2-gram 3-gram 이런 식으로 갈 수가 있음
text = "hello"
for i in range(len(text)):
    #print(text[i:i+2]) #i로 시작해서 i+2까지 2글자씩 나눔
    print(text[i:i+3]) #3그램은 숫자만 바꾸면 됨. 글자를 앞당겨와서 겹쳐서 나눔
    
print()
#단어 단위
text = "this is python program"
words = text.split() #text 글자를 공백으로 나눔
print(words)
print(len(words))
for i in range(len(words) - 1): #-1을 빼면 range는 4 그렇게 되면 아래 print 문에서 오류가 생긴다 더 이상 출력할 것이 없는데 for 문이 4번 반복하기 때문이다
    print(words[i], words[i + 1])
    #i가 0일때 0번 인덱스인 this가, 0+1이라서 1번 인덱스인 is가 출력
















