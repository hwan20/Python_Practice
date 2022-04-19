import numpy as np
import pandas as pd

#구조 변경

df = pd.DataFrame(np.arange(6).reshape(2,3)+1000, index = ['대전', '서울'],
                columns = ['2020', '2021', '2022'])

print(df)
print('-------------')

print(df.stack()) #index를 기준으로 열 쌓기
print('-------------') #데이터 타입 변환?? 동영상 5분 2시 36분

df_row = df.stack() #위와 같음
print(df_row)
print('-------------')
df_col = df_row.unstack() #stack한 데이터 복원
print(df_col)
print('-------------')

#범주화 - 연속형 데이터들을 범주형 데이터로 바꿈 
price = [10.3, 5.5, 7.8, 3.6] #[(9, 11], (3, 7], (7, 9], (3, 7]]   
cut = [3, 7, 9, 11] #구간 기준 값 나누는 기준은 자기 마음
result_cut = pd.cut(price, cut)
print(result_cut) #(a, b]의 중괄호 대괄호 뜻은 a < x <= b 
print('-------------')
print(pd.value_counts(result_cut)) #각 범위에 해당하는 데이터의 숫자를 알려줌

print('-------------')
datas = pd.Series(np.arange(1, 1001))
print(datas.head(2))
print('-------------')

print(datas.tail(2))
print('-------------')

cut2 = [0, 300, 600, 1000]
result_cut2 = pd.cut(datas, cut2)
print(result_cut2)
print('-------------')

result_cut3 = pd.qcut(datas, 3) #지정한 숫자 만큼 범주화 
print(result_cut3)
print('-------------')
print(pd.value_counts(result_cut3))
print('-------------')

#그룹화
group_col = datas.groupby(result_cut3) #범주화 시키고 그룹화
print(group_col) #SeriesGroupBy object
print('-------------')

#pandas : agg('함수명') 함수를 실행하는 메소드
print(group_col.agg(['count', 'mean', 'std', 'min'])) #그룹화 시킨 데이터의 정보를 가져옴
print('-------------')

#agg함수 내부 작성
def summaryFunc(gr):
    return {
        'count' : gr.count(),
        'mean' : gr.mean(),
        'std' : gr.std(),
        'min' : gr.min()
    }

print(group_col.apply(summaryFunc))
print('-------------')

print(group_col.apply(summaryFunc).unstack())


#DataFrame자료 합치기 Merge
df1 = pd.DataFrame({'data1':range(7), 'key':['b', 'b', 'a', 'c', 'a', 'a', 'b']})
print(df1)
print('-------------')

df2 = pd.DataFrame({'key':['a', 'b', 'd'], 'data2':range(3)})
print(df2)
print('-------------')

#inner Join
print(pd.merge(df1, df2, on='key')) #'key'를 기준으로 병합. inner join : 교집합
#df1에 a, b, d 외에 다른 키는 참여하지 않음
#겹치는 칼럼만 합침
print('-------------')

print(pd.merge(df1, df2, on='key', how='inner'))
print('-------------')

#Outer Join
print(pd.merge(df1, df2, on='key', how='outer')) #full outer join 겹치지 않는 부분도 병합
print('-------------')

print(pd.merge(df1, df2, on='key', how='left')) #left outer join df1을 위주로 병합 df2의 d는 안 나옴
print('-------------')

print(pd.merge(df1, df2, on='key', how='right')) #right outer join df2을 위주로 병합 df1의 c는 안 나옴
print('-------------')

#공통 칼럼이 없는 경우 merge
df3 = pd.DataFrame({'key2':['a', 'b', 'd'], 'data2':range(3)})
print(df3)
print('-------------')
print(pd.merge(df1, df3, left_on='key', right_on='key2')) #칼럼명을 따로 줌

#자료 이어 붙이기 concat
print('-------------')
print(pd.concat([df1, df3]))
print('-------------')

print(pd.concat([df1, df3], axis = 0)) #열단위
print(pd.concat([df1, df3], axis = 1)) #열단위
print('-------------')

#DataFrame관련 집계 메소드 : pivot, groupby, pibot_table  다 집계를 만드는 것들

data = {'city' : ['강남', "강북", '강남', '강북'], 'year':[2000, 2001, 2002, 2002], 'pop':[3.3, 2.5, 3.0, 2.0]}
df = pd.DataFrame(data)
print(df)
print('-------------')

print(df.pivot('city', 'year', 'pop')) #구조를 재구성 45분 3시 15분
print(df.pivot('year', 'city', 'pop'))
print('-------------')

print(df.set_index(['year', 'city']).unstack())
print('-------------')

#groupby : 특정 칼럼을 기준으로 그룹화해서 소계

hap = df.groupby(['city']) #[]안에 여러 가지 쓸 수가 있음   city로 그룹 obj를 만들 수가 있음
print(hap) #DataFrameGroupBy object
print(hap.sum())
print('-------------')

print(df.groupby(['city']).sum()) #위 소스 코드를 한 줄로 표현
print('-------------')

print(df.groupby(['city']).agg('sum')) #위와 같음
print('-------------')

print(df.groupby(['city', 'year']).mean()) #city별 year별 평균
print('-------------')

#피벗 테이블(pivot table)은 커다란 표(예 : 데이터 베이스, 스프레드 시트, 비즈니스 인텔리전스 프로그램 등)의 데이터를 요약하는 통계표이다
#이 요약에는 합계, 평균, 기타 통계가 포함될 수 있으며 피벗 테이블이 이들을 함께 의미있는 방식으로 묶어준다
#피벗 테이블은 데이터 처리의 한 기법이다
#유용한 정보에 집중할 수 있도록 하기 위해 통계를 정렬 또는 재정렬한다


#pivot_table : pivot과 groupby 기능을 모두 사용 가능하다
print(df)
print(df.pivot_table(index=['city'])) #기본 함수는 평균(mean) city에 대한 year와 pop의 평균
print(df.pivot_table(index=['city'], aggfunc=np.mean)) #aggfunc=np.mean이 기본 값
print('-------------')

print(df.pivot_table(index=['city', 'year'], aggfunc=[len, np.mean]))
print(df.pivot_table(index=['city', 'year'], aggfunc=[len, np.sum])) 
print('-------------')

print(df.pivot_table(values=['pop'], index=['city']))
print('-------------')

print(df.pivot_table(values=['pop'], index='city', aggfunc=len))
print('-------------')

print(df.pivot_table(values=['pop'], index=['year'], columns='city', aggfunc=np.mean))
print('-------------')

print(df.pivot_table(values=['pop'], index=['year'], columns='city',
                     aggfunc=np.mean, margins=True))
print('-------------')

print(df.pivot_table(values=['pop'], index=['year'], columns='city',
                     aggfunc=np.mean, margins=True, fill_value=0))
print('-------------')







