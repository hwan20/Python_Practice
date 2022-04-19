#file i/o

import pandas as pd
from pandas.tests.frame.methods.test_sort_values import ascending

#읽기
df = pd.read_csv('../testdata/ex1.csv')
print(df, type(df)) #<class 'pandas.core.frame.DataFrame'>
print('-----------------------------')

print(pd.read_table('../testdata/ex1.csv', sep=',', skipinitialspace=True))
print('-----------------------------')

print(pd.read_csv('../testdata/ex2.csv'))
print('-----------------------------')

print(pd.read_csv('../testdata/ex2.csv', header = None))
print('-----------------------------')

print(pd.read_csv('../testdata/ex2.csv', header = None, names=['a','b']))
print('-----------------------------')

print(pd.read_csv('../testdata/ex2.csv', header = None, names=list('korea')))
print('-----------------------------')

print(pd.read_csv('../testdata/ex3.txt'))
print('-----------------------------')

print(pd.read_csv('../testdata/ex3.txt').describe())
print('-----------------------------')

print(pd.read_csv('../testdata/ex3.txt', sep=' '))
print('-----------------------------')

print(pd.read_csv('../testdata/ex3.txt', sep=' ').describe())
print('-----------------------------')

print(pd.read_csv('../testdata/ex3.txt', sep='\s+'))
print('-----------------------------')

print(pd.read_csv('../testdata/ex3.txt', sep='\s+').describe())
print('-----------------------------')

print(pd.read_csv('../testdata/ex3.txt', sep='\s+', skiprows=[1, 3]))
print('-----------------------------')

print(pd.read_fwf('../testdata/data_fwt.txt', widths=(10,3,5), header=None,
                  names=('date', 'name', 'price'), encoding='UTF-8'))
print('-----------------------------')

#chunk : 대용량의 파일인 경우에는 chunk 단위로 부분 씩 읽어 들일 수 있다 
test = pd.read_csv("../testdata/data_csv2.csv", header=None)
print(test)
print('-----------------------------')

test2 = pd.read_csv("../testdata/data_csv2.csv", header=None, chunksize=3) #TextFileReader object
print(test2) #데이터 파일이 됨

for p in test2:
    print(p.sort_values(by=2, ascending=True)) #2번째 칼럼 명을 내림차순으로 정렬해서 chunk단위로 읽음
print('-----------------------------')

#저장
items = {'apple' : {'count' : 10, 'price' : 1500}, 'orange' : {'count' : 5, 'price' : 1000}}
df = pd.DataFrame(items)
print(df)
print('-----------------------------')

#df.to_clipboard() #데이터가 복사가 되어 있어 ctrl + v로 붙여넣을 수 있다
#print(df.to_html()) #데이터를 테이블 형태로 만들어준다
#print(df.to_json) #데이터를 json 형태로 만들어준다
#print(df.to_xml) #데이터를 xml 형태로 만들어줌

df.to_csv('pan5ex1.csv', sep=',') #파일을 저장함
df.to_csv('pan5ex1.csv', sep=',', index=False) #색인은 제외
df.to_csv('pan5ex1.csv', sep=',', index=False, header=False) #색인, 칼럼명은 제외
#csv가 아닌 기타 다른 형식으로도 저장 가능




















