#우편 번호 data 파일 사용
#키보드로 동을 입력하면 해당 동의 정보를 읽어오기

try:
    dong = input("동 이름 입력 : ")
    #dong = "개포"
    #print(dong)
    
    with open(r'zipcode.txt', 'r', encoding="euc-kr") as f:
        line = f.readline() #맨 위에 한 줄을 읽어옴
        #print(line)
        
        #Tab을 구분으로 잘라서 원하는 정보에 대한 글을 읽어옴
        #ASCII 코드로 정보를 입력해줌 Tap은 10진수로 9, Enter은 10진수로 10~13이다
        
        while line: #자료가 있으면 true, 없으면 false 자료가 없을 때까지 반복해서 출력한다
            #lines = line.split("\t") #line에 입력된 정보를 Tab을 기준으로 잘라서 읽어옴
            lines = line.split(chr(9)) #chr(9)은 tap과 같다
            #print(lines)
            
            #출력되는 정보의 4번째 정보에 주소가 있으니 해당 정보에 if문을 걸어 조건을 건다
            if lines[3].startswith(dong): #lines의 4번째에 dong 변수에 입력된 글자로 시작하면
                #명령이 길어져서 줄을 바꾸고 싶으면\를 넣는다
                print("[" + lines[0] + "]" + lines[1] + " " + \
                      lines[2] + " " + lines[3] + " " + lines[4])
            
            line = f.readline() #한 번 처리하고 다음 정보를 처리한다
        
except Exception as e:
    print("err : ", e)





