from bs4 import BeautifulSoup
"""
import numpy as np

data = np.array([[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]])

print(np.flip(data))
"""
"""
import seaborn as sns
titanic = sns.load_dataset('titanic')
print(titanic.head(5))
print('-----------------')
print(titanic.loc[:,'sex'])
print('-----------------')
print(titanic.groupby(['sex'])['survived'].mean())
"""

html_page4 = """
<html>
<body>
<div>
    <a href="https://www.sbs.com">sbs</a>
</div>
<div id="hello">
    <b>파이썬</b>
    <a href="https://www.kbs.com">kbs</a>
    <a href="https://www.naver.com" target="_blank">네이버</a>
    <span>
        <a class href="https://www.tvn.com">tvn</a>
    </span>
</div>
<span>
    <a href="https://www.mbc.com">mbc</a>
</span>
<ul class="world">
    <li>안녕</li>
    <li>반가워</li>
</ul>
<p> 웹문서 읽기 </p>
<p id="my" class="our"> 파이썬 라이브러리 사용 </p>
<div id="hi" class="good">
    second div
    <a href="https://www.daum.net">다음</a>
</div>
</body>
</html>
"""

#convert_data = BeautifulSoup(html_page4, 'lxml')

#for atag in convert_data.findAll('a'), {'target':'_blank'}:
#    print(atag.value_counts())


print("---")

"""
from pandas import DataFrame

frame = DataFrame({'bun':[1,2,3,4], 'irum':['aa','bb','cc','dd']},
                  index=['a','b', 'c','d'])
#print(frame.T)
print(frame.drop('d'))
"""


"""
import pandas as pd
df = pd.read_csv('../testdata/ex2.csv', header = None, names=['a','b','c','d'])
print(df)
#df = pd.DataFrame
"""

"""
import pandas as pd
from pandas import DataFrame
data = {
    'juso':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon':[23, 25, 15]
}
df = DataFrame(data)

result = pd.Series([x.split()[0] for x in df.juso])

print(result)
"""
"""
import pandas as pd
from pandas import DataFrame

data = {
    'product':['아메리카노','카페라떼','카페모카'],
    'maker':['스벅','이디아','엔젤리너스'],
    'price':[5000,5500,6000]
}

df = pd.DataFrame(data)
"""

"""
import numpy as np 

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3]).reshape(3, 1)
print(x)
print(y)
print(x+y)
"""



"""
import urllib.request
from bs4 import BeautifulSoup
try:
    url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
    page = urllib.request.urlopen(url)

    soup = BeautifulSoup(page.read(), "html.parser")
    title = soup.find_all('li')
    print()
    for i in range(0, 10):
        print(str(i + 1) + ") " + title[i].a['title'])
except Exception as e:
    print("처리 오류 : ", e)
"""


















