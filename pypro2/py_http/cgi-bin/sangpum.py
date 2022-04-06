#DB자료 출력
import MySQLdb #DB 데이터를 config 로 입력해도 되고 데이터를 해도 되지만 config는 데이터 정보가 보이니 X
import pickle

with open("mydb.dat", "rb") as obj:
    config = pickle.load(obj)

print("Content-Type:text/html;charset=utf-8\n")

print("<head><body>")
print("<h2>상품 정보</h2>")
print("<a href='../main.html'>메인으로</a>")
print("<table border='1'><tr><th>코드</th><th>상품명</th><th>수량</th><th>단가</th></tr>")

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    
    cursor.execute("select * from sangdata") #*로 모든 칼럼 하면 안 좋음 많이 잡아먹음
    datas = cursor.fetchall() #모든 데이터를 보기 위해
    
    for code, sang, su, dan in datas:
        print("""
           <tr>
               <td>{0}</td>
               <td>{1}</td>
               <td>{2}</td>
               <td>{3}</td>
            </tr>
        """.format(code, sang, su, dan))
    
except Exception as e:
    print("처리 오류 : ", e)

finally:
    cursor.close()
    conn.close()
    
print("</table>")
print("</body></head>")





