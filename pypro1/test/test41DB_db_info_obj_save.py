#DB연결 객체를 파일로 만들어서 저장하기

import pickle

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8', 
    'use_unicode':True 
}

with open(file = "mydb.dat", mode = "wb") as obj:
    pickle.dump(config, obj)







