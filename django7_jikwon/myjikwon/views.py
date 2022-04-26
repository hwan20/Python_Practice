from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from myjikwon.models import Jikwon
#위의 모듈로는 기술통계만 가능 추론 통계 X

plt.rc('font', family='malgun gothic') #한글 나오게 하려고

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def showFunc(request):
    #이미 있는 테이블의 데이터 출력
    jikwons = Jikwon.objects.all().values()
    #print(jikwons)
    df = pd.DataFrame.from_records(data = jikwons)
    df.columns = ['사번', '직원명', '부서', '직급', '연봉', '입사', '성별', '평점']
    print(df.head(2))
    
    
    #부서별 연봉합/평균
    buser_group = df['연봉'].groupby(df['부서'])
    buser_group_detail = {'sum':buser_group.sum(), 'avg':buser_group.mean()}
    print(buser_group_detail, type(buser_group_detail)) #<class 'dict'>
    

    #dict type은 web에 출력하기 어려우니
    #부서별 연봉합/평균 -> DataFrame으로 처리하여 넘김
    print('--------df2--------')
    df2 = pd.DataFrame(buser_group_detail)
    print(df2)    
    
    
    #시각화 이미지로 저장
    print('--------시각화--------')
    bu_result = buser_group.agg(['sum', 'mean']) #agg는 함수를 실행하는 명령어
    print(bu_result)
    
    bu_result.plot(kind='barh')
    plt.title('부서별 연봉의 합/평균')
    plt.xlabel('연봉')
    fig = plt.gcf()
    fig.savefig('django7_jikwon/myjikwon/static/images/buser.png') #저장할 경로를 적어줌
    
    return render(request, 'list.html', {'datas':df.to_html(index=False), #dataframe은 to_html 명령어로 html에 넘길 수가 있따
                                         'buser_group':buser_group_detail,
                                         'buser_group2':df2.to_html()})



