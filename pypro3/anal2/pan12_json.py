#JSON 처리
#JSON 객체(string)를 dict로 JSON 디코딩
#dict 객체를 JSON으로 JSON 인코딩

import json

dict = {'name' : 'tom', 'age' : 22, 'score' : ['90', '80', '100']}

print(dict, type(dict)) #<class 'dict'>
print('-------------')

#인코딩
str_val = json.dumps(dict) #dict를 JSON인 str로
print(str_val, type(str_val)) #<class 'str'>
print(str_val[0:20]) #str이 할 수 있는 것만 작업이 가능
#print(str_val['name']) #str은 칼럼명으로 지정 안 됨   TypeError: string indices must be integers
print('-------------')

#디코딩
json_val = json.loads(str_val)
print(json_val, type(json_val)) #<class 'dict'>
print(json_val['name']) #json(dict) type이 할 수 있는 명령을 사용할 수 있다
