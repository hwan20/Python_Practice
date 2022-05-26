#단어의 빈도수를 이용해 문서의 특징 추출
#BOW (Bag Of Words) : 문서가 가지는 모든 단어, 문맥, 순서를 무시하고 단어에 대해 빈도 수를 부여해 벡터를 생성

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

#CountVectorizer : 단순하게 텍스트에서 단위별 등장횟수를 카운팅하여 수치를 벡터화함(BOW)

contents = ['How to format my hard disk', 'Hard disk format format problems']

count_vec = CountVectorizer(analyzer='word', min_df = 1)  #'word', 'char'
tran = count_vec.fit_transform(raw_documents=contents)
print(tran)
print(count_vec.get_feature_names())
print(tran.toarray())
print('-------------------------------------------')

#'disk', 'format', 'hard', 'how', 'my', 'problems', 'to' 토큰의 갯수만큼 만들어짐 대문자 -> 소문자 처리
#  0         1       2      3     4         5       6

#1행 How to format my hard disk
#    3   6   1     4  2     0
#2행 Hard disk format format problems
#    2    0     1      1       5
#몇 행 몇 열이 몇 번 나왔는지를 출력됨

#CountVectorizer은 그냥 카운팅만 해줌 - 이것을 개선해준게 TfidfVectorizer
#의미가 있는 단어는 가중치를 주고 아니면 패널티를 줌

#TfidfVectorizer : 하나의 문단에서 자주 나오는 단어에 대해 가중치를 높게 부여하나,
#전체 문서의 모든 문단에서 자주 등장하는 단어에 대해서는 패널티를 주는 방식으로 값을 부여

tfidf_vec = TfidfVectorizer(analyzer='word', min_df = 1)
tran_idf = tfidf_vec.fit_transform(raw_documents=contents)
print(tran_idf)
#  (0, 0)    0.3347122780719073 가중치를 줄 수가 있다
#  (0, 2)    0.3347122780719073
#  (0, 4)    0.4704264280854632
#  (0, 1)    0.3347122780719073
print(tfidf_vec.get_feature_names())
print(tran_idf.toarray())






