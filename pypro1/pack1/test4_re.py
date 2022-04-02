#정규표현식 패턴을 통해서 원하는 정보를 얻어낼 수가 있다
#정규표현식 : 대량의 문자열에 대해 일정한 패턴을 부여해 원하는 문자열만 취할 수가 있다

import re

ss = "234 가abc가나다abcABC_123555_6Python나 if fun" 
print(ss)
print(re.findall("123", ss)) #패턴과 문자열을 주고 패턴에 맞는 문자열을 가져옴 list 타입의 값을 return 시킨갇
aa = re.findall(r"123",ss) #패턴 앞에 r이 붙으면 escape 문자로 되어 특수 기호도 사용 가능 보통 정규표현식에는 앞에 r을 붙임
print(aa[0]) # list의 0번째 방을 가져옴
print(re.findall("가나", ss)) #'가나'만 리턴된다
print(re.findall("[12]", ss)) #숫자 1과 2를 리턴시켜 준다
print(re.findall("[0-9]", ss)) #모든 숫자를 리턴해준다
print(re.findall("\d", ss)) #모든 숫자 하나씩 위와 같다
print(re.findall("\d\d", ss)) #모든 숫자 두개씩 \D \s \S \w \W 등이 있다 \d가 3개면 3글자씩
print()
print(re.findall("[0-9]+", ss)) #1번 이상 반복되는 모든 숫자를 리턴한다 ['1234', '123555', '6']
print(re.findall("[0-9]?", ss)) #0번 또는 1번 이상 반복되는 모든 숫자를 리턴 숫자 사이에 있는 다른 문자는 공백으로 출력 ['1', '2', '3', '4', '', '', '']
print(re.findall("[0-9]*", ss)) #0번 이상 반복되는 모든 숫자를 리턴 숫자가 아닌 곳은 공백으로 출력 ['1234', '', '', '', '']
print()
print(re.findall("[0-9]{2}", ss)) #{} 문자의 반복 횟수를 정의할 수가 있다 2번 반복 모든 숫자를 2글자씩 끊어서 리턴 2글자가 안 되면 리턴 X
print(re.findall("[0-9]{1,3}", ss)) #{} 패턴 안에 있는 문자를 앞에 있는 숫자의 최소 갯수와 뒤에 있는 숫자 최대 갯수만큼 출력 최소 갯수가 안 되거나 최대 갯수를 넘어가면 출력 X
print(re.findall("[a-z]", ss)) #영어 소문자 모두를 출력
print(re.findall("[a-zA-Z]", ss)) #소문자와 대문자를 포함한 모든 영어 출력
print(re.findall("[a-zA-Z ]", ss)) #맨 끝에 공백을 넣어 소문자와 대문자 영어와 공백 출력
print(re.findall("[가-힣]", ss)) #모든 한글을 출력
print(re.findall("[^가-힣]", ss)) #^가 붙으면 부정 한글만 빼고 출력
print('매칭')
print(re.findall(".bc",ss)) #첫 글자는 아무거나 상관 X 두 번째는 b, 세 번째는 c
print(re.findall("a..",ss)) #첫 글자는 a로 시작 두 번째, 세 번째는 상관 X
print(re.findall("^123",ss)) #^은 문자 집합 내에 들어가면 부정, 집합 앞에 들어가면 시작되는 단어를 칭함
#맨 앞에 123으로 시작되지 않으면 리턴 X
print(re.findall(".bc",ss)) #앞 글자는 상관 없이 뒤에 bc가 있으면 리턴
print(re.findall("fun",ss)) 
print(re.findall("fun$",ss)) #$은 문자열로 끝나는 것을 리턴함 없으면 X 
print(re.findall("12|34",ss)) #12 or 34를 리턴함
print("그룹화") #list와 tuple 타입으로 리턴함 
print(re.findall("(ab)+(c)",ss)) #두 문자를 한 그룹으로 리턴되게 해줌

p = re.compile("abc") #패턴을 가지고 있는 객체
print(re.findall(p,ss)) #객체를 가지고 패턴을 넣어줄 수도 있다

print()

p = re.compile("the", re.IGNORECASE) #re.IGNORECASE를 작성하면 대소문자 신경 안 씀
print(p.findall("The DoG the dog")) 










