import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open('mydb.dat', mode = 'rb') as obj:
    config = pickle.load(obj)

conn = MySQLdb.connect(**config)
cursor = conn.cursor()
sql = """
    select buser_name, jikwon_gen, jikwon_pay
    from jikwon inner join buser on buser_no=buser_num
"""
cursor.execute(sql)

#for (a, b, c) in cursor:
#    print(a, b, c)

data=pd.DataFrame(cursor, columns=["부서", "성별", "연봉"])
#print(data.head(2))

#print(data.pivot_table(['연봉'], index=['성별'], aggfunc = np.mean))
#pay = data.pivot_table(['연봉'], index=['성별'], aggfunc = np.mean)
pay = data.groupby(['성별'])['연봉'].mean()
print(pay, type(pay))


#plt.bar(range(len(pay)), pay) #막대형 그래프
#plt.show()

plt.bar(range(len(pay)), pay, alpha = 1, color = ['black', 'r'])
plt.xlabel('gender')
plt.xticks([0,1], labels=['Male', 'Female'])
plt.ylabel('pay')
plt.show()



