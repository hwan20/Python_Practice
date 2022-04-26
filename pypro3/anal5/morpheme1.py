#형태소 분석 : 자연어 처리를 위하여 언어적 속성의 구조를 파악하는 것
#konlpy 라이브러리를 사용(JAVA로 만듬)

from konlpy.tag import Kkma, Okt, Komoran

kkma = Kkma() #생성자로 생성함. JAVA로 만들어 JAVA의 형식
print(kkma.sentences('한글 데이터 형태소 분석을 위한 라이브러리 설치를 합니다. 잘되길 바랍니다'))
print(kkma.nouns('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123')) #영어를 버리고 한글이랑 숫자만
print(kkma.pos('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123'))
print(kkma.morphs('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123'))

print('---------------------------')

okt = Okt() #생성자로 생성함. JAVA로 만들어 JAVA의 형식
print(okt.nouns('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123')) 
print(okt.pos('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123'))
print(okt.pos('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123', stem = True)) #원형 어근을 추출
print(okt.morphs('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123'))
print(okt.phrases('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123')) #어절 추출

print('---------------------------')

ko = Komoran() #생성자로 생성함. JAVA로 만들어 JAVA의 형식
print(ko.nouns('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123')) 
print(ko.pos('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123'))
print(ko.morphs('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123'))