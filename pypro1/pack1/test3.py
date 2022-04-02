#묶음 자료형
#자료형 중에서 int, float, bool, complex : 객체 하나를 참조
#자료형 중에서 str, list, tuple, set, dict : 객체값 여러 개를 요소로 참조

#str
print("Str type--- : 순서 O(인덱스가 있으며, 슬라이싱이 가능) 수정 X")
#s[0] -> 인덱싱 맨 처음 s를 가르킴
s="sequence" #총 8개의 방의 길이가 있으며 0~7, -7~0까지 방에 숫자를 매김 -> s는 묶음형 변수
print("길이 : ", len(s)) #변수 s에 입력된 길이를 재는 명령어
print("특정문자 포함 위치 확인", s.count("e"), s.count("m"), s.find("e")) #변수 s에 특정 문자를 세거나 위치를 찾아줌

#다량의 문자열 관련 함수 구글에 python 문자열 함수 검색해서 사용 -> 너무 많아서 
#변수 s는 문자열을 저장한 묶음형 변수이다 여러 가지의 요소를 가지고 있어 순서가 있다
print(id(s))
s="bequence" #새로운 객체를 치환한 것임 수정이 아니라 대상이 바뀐 것
print(id(s)) #새로운 객체를 만들고 객체의 주소를 받아온 것

#인덱싱, 슬라이싱 가능
s="sequence"
print(s, s[0], s[3], s[7], s[-1], s[-3]) #방을 찾아서 불러옴 -1은 맨 끝을 가르킴    인덱싱
print(s[0:3]) #0 이상 3 미만    슬라이싱은 [시작:끝:간격] [s(tart):t():s(tep)]
print(s[-4:-1]) #-4이상 -1미만 -1은 맨 끝을 가르킴
print(s[:3]) #3번째 까지
print(s[3:]) #3번째 부터
print(s[2:7:1]) #2에서부터 7미만까지 바로 옆에 문자를 더함
print(s[2:7:2]) #2에서부터 7미만까지 두 칸 옆에 문자를 더함
print(s[::2]) #시작부터 끝까지 한 칸 건너띄기
print(s[2:5]+"만세") #2에서부터 5미만까지와 + 만세 

ss="mbc kbs"
result = ss.split(sep=" ") #문자열을 자름 sep는 어떤 부분을 자를지 정해주는 것
print(result)
print(" ".join(result)) #앞에 오는 구분자로 문자열을 합침

print()

#list
print("List type--- : 순서 O, 수정 O, 요소값 중복O 요소들을 대괄호 [] 로 감쌈")
a=[1, 2, 3, "문자열", 4.5, True, 1, 2, 3] #여러 타입의 요소들을 넣어도 상관 X
print(a, type(a))
b=[a, 100, 200] #list를 넣어서 사용할 수도 있음
print(b) #list를 넣어서 사용하는게 중복 list
family=["엄마", "아빠"]
print(id(family))
print(family)
family[0] = "어머니" #내용 수정이 가능함
print(id(family)) #내용 수정이 가능하니 참조값의 주소가 바뀌지 않음
print(family)
family.append("나") #append 명령어는 list의 맨 뒤에 삽입 됨
family.append("나")
family.append("나")
family.insert(1, "여동생") #insert 명령어는 index를 지정해주고 value를 정해주면 해당 인덱스에 삽입이 되고 나머지는 뒤로 밀림
print(family)
family.remove("나") #'나' 라는 value값이 하나만 list에서 사라짐    값에 의한 삭제 
family.remove("나")
family.extend(["삼촌", "이모"]) #append 명령어와 같으며, 주로 append 명령어를 사용
family += ["고모"] #append 명령어와 같으며, 주로 append 명령어를 사용
family.append("나")
family.remove("나") #같은 value가 여러 곳에 있을 때 index 번호가 앞에 있는 value부터 삭제
print(family)
del family[0] #family list의 0번째 값을 지움    순서에 의한 삭제
del family[0] #remove와의 차이점 remove는 value에 의한 삭제라서 value가 없을 때 사용 불가
print(family)
del family #변수를 삭제하는 명령어 family변수가 사라짐
#print(family)

print()

#tuple
print("Tuple type--- : 리스트와 유사하지만 수정 X 리스트에 비해 검색 속도가 빠름 요소들을 소괄호 () 로 감쌈")
#t=("a", 10, "b")
t="a", 10, "b", 10 #위와 같음 괄호 없어도 상관은 X
print(t, type(t))
print(t[0])
#t[0] = "k"     TypeError: 'tuple' object does not support item assignment 수정 X
a=(1) # <class 'int'>
b=(1,) # <class 'tuple'> 요소가 하나 이상이면 tuple
print(type(a), type(b))

#형 변환
aa=[1,2,3]
bb=tuple(aa) #list타입인 aa를 tuple타입으로 바꿀 수가 있음
print(type(bb))
aa=list(bb) #tuple 타입인 bb를 list타입으로도 바꿀 수가 있다
print(type(aa))

print()

#set

print("Set type--- : 순서 X, 수정 X, 중복 X 요소들을 중괄호 {}로 감쌈")
a={1, 2, 3, 1} #중복되는 value인 마지막 1은 저장 X
print(a, type(a))
#print(a[0]) TypeError: 'set' object is not subscriptable 순서가 X
b={3, 4}
print(a.union(b)) #변수 a와 변수 b의 합집합
print(a.intersection(b)) #a와 b의 교집합
print(a - b, a | b, a & b) 

b.update({5,6}) #update 명령어를 통해 value 삽입 가능 index를 이용한 삽입이 아니니 수정 X
b.update([7,8])
b.update((9,10))
print(b)
b.discard(6) #해당하는 value를 삭제
print(b)
b.discard(6) #해당하는 value가 없으면 실행 X
b.remove(7) #해당 value를 삭제
#b.remove(7) #해당 value가 없으면 에러
print(b)

print()

aa=[1,2,2,3,4,5,5]
print(aa, type(aa))
bb=set(aa) #중복된 데이터를 set에 넣으면 사라짐
print(bb)
aa=list(bb)
print(aa, type(aa))

print()

#dict
print("Dict type--- : 순서 X, 수정 O, 요소들을 {'키' : '값'}로 감쌈") #index는 없지만 key로 value를 지정해서 수정
#json과 형식이 비슷해서 데이터를 주고 받을 때 많이 사용함
mydic = dict(k1 = 1, k2 = "abc", k3 = 3.4) #문자는 반드시 '', ""로 감싸야 하며 숫자는 상관 X
print(mydic, type(mydic)) #순서가 없어서 k1, k2, k3 순서 상관 없이 나옴

dic={"파이썬" : "뱀", "자바" : "커피", "스프링" : ["용수철", "웹처리"]} #value값이 list형식으로도 가능
print(dic)
print(dic["파이썬"]) #key값을 가지고 value를 가져올 수가 있음 
#print(dic[0]) KeyError: 0 index 번호로는 X

dic["오라클"] = "예언자" #데이터 추가 가능 데이터를 추가할 때 key값은 [] 대괄호로 감싸야 하나?
print(dic)
del dic["오라클"] #key 값으로 삭제 value값으로 key값 삭제 X
print(dic)
dic["파이썬"] = "만능 언어" #key에 해당하는 value값을 수정 가능
print(dic)





