#json문서 읽기
import json

json_data = {}

def read_data(filename):
    f = open(filename, 'r', encoding="UTF-8")
    lines = f.read()
    f.close()

    jdata = json.loads(lines) #str을 json으로 디코딩
    return jdata

def main():
    global json_data
    json_data = read_data("pan13.json")
    print(json_data, type(json_data)) #<class 'dict'>
    
    #key, value는 dict타입이 좋으니 string을 dict로 형변환(casting)
    
    d1 = json_data['직원']['이름']
    d2 = json_data['직원']['직급']
    d3 = json_data['직원']['전화번호']
    print(d1, d2, d3)
    print('-------------')
    
    d4 = json_data["웹사이트"]["카페명"]
    d5 = json_data["웹사이트"]["userId"]
    print(d4, d5)
    print('-------------')
    
    
    
if __name__ == "__main__":
    main()










