#web에서 JSON문서 읽기

import json
import urllib.request as req
import pandas as pd

#데이터를 뽑을 주소를 적음
url = "http://127.0.0.1:8888/library.json"

#주소에서 뽑은 데이터를 변수에 저장함 -> string 타입
libdata = req.urlopen(url).read().decode()
print(libdata, type(libdata)) #<class 'str'> 웹에서 읽어드리면 무조건 str
print('-------------')

#저장된 string 타입의 데이터를 json형식의 dict 타입으로 바꿈
jsondata = json.loads(libdata)
print(jsondata, type(jsondata)) #<class 'dict'>
print('-------------')

#dict의 기능을 이용해서 원하는 자료를 얻기
print(jsondata['row'][0]['LIBRARY_NAME'])
print('-------------')

#저장된 dict타입에 있는 데이터를 추출해옴
libData = jsondata.get('row')
print(libData)
print('-------------')

#추출해온 데이터의 1번째 행에 있는 LIBRARY_NAME을 출력
name = libData[0].get('LIBRARY_NAME')
print(name)
print('-------------')

datas = []
for ele in libData:
    name = ele.get('LIBRARY_NAME')
    addr = ele.get('ADDRESS')
    tel = ele.get('TEL_NO')

    print(name + " " + addr + " " + tel)
    imsi = [name, tel, addr]
    datas.append(imsi)

print('-------------')

#위에서 출력된 정보를 저장시켜서 DataFrame로 뽑아넴
df = pd.DataFrame(datas, columns=['도서관명', '주소', '전화번호'])
print(df)






