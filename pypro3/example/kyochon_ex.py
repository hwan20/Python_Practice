from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd

url = "http://www.kyochon.com/menu/chicken.asp"
# 이하 소스 코드와 결과만 제출하시오.

data = req.urlopen(url)
soup = BeautifulSoup(data,"lxml")
pName = soup.select("dl.txt > dt")
pPrice = soup.select("p.money > strong")
#print(pPrice)
#print(pName)
a=[]
b=[]
for name, price in zip(pName, pPrice):
    if name.string != None:
        a.append(name.string)
        b.append(price.string)
        #print(name.string, price.string)
print("--")
#print(a, len(a))
aa=pd.Series(a)
#print(aa)
#print("--")
#print(b, len(b), type(b))
bb=pd.Series(b)
#print(bb)


df=pd.DataFrame(zip(aa, bb), columns=['상품명', '가격'])
print(df)


