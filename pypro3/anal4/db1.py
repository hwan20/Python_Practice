#Local Database 연동 후 DataFrame으로 저장
import sqlite3

sql = """create table if not exists mytab(product varchar(10),
            maker varchar(10), weight real, price integer)"""

conn = sqlite3.connect(":memory:") #ram상으로 작성 휘발성이라 1회용이다
#conn = sqlite3.connect("testdb")
conn.execute(sql)
conn.commit()

stmt = "insert into mytab values(?, ?, ?, ?)"

data1 = ('신상1', '롯데리아', 45, 5000)
conn.execute(stmt, data1)

data2 = ('신상2', '맥도날드', 55, 5500)
conn.execute(stmt, data2)

cursor = conn.execute("select * from mytab")
rows = cursor.fetchall()

for a in rows:
    print(a)
print('-------------')

import pandas as pd



#방법1
df1 = pd.DataFrame(rows, columns = ['product', 'maker', 'weight', 'price'])
print(df1)
print('-------------')



#방법 2
df2 = pd.read_sql("select * from mytab", conn)
print(df2)
print('-------------')
#print(df2.to_html()) #테이블이 자동으로 만들어짐



#DataFrame을 DB로 저장
#1. DataFrame 작성
data = {
    'product' : ['연필', '볼펜'],
    'maker' : ['모닝글로리', '모나미'],
    'weight' : [1.5, 2.3],
    'price' : [500, 1000]
}
frame = pd.DataFrame(data)
print(frame)
print('-------------')

#2. DB에 저장
frame.to_sql("mytab", con=conn, if_exists="append", index=False)

df3 = pd.read_sql("select * from mytab", conn)
print(df3)
print('-------------')

print(pd.read_sql("select count(*) as count from mytab", conn))


#원격으로 sql 집어넣는 곳에서는 DataFrame을 위와같이 저장하지 못함










