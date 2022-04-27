from django.shortcuts import render, redirect
from mysurvey.models import Survey
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.rc('font', family='malgun gothic')

# Create your views here.

def surveyMain(request):
    
    return render(request, 'main.html')


def surveyView(request):
    
    return render(request, 'survey.html')


def surveyprocess(request):
    insertData(request)  #설문조사 결과를 DB에 저장
    return redirect('/coffee/surveyshow') #client를 통해서 redirect방식으로 분석 결과 보기를 요청

#설문완료 버튼을 누르면 surveyprocess 함수를 실행하여 inserData함수를 호출한다
#호출된 insertData는 분석 결과를 리턴한다

#1. 설문조사 화면에서 설문완료를 누르면 surveyprocess함수를 실행한다
#2. surveyprocess함수를 실행하면 안에 있는 insertData함수를 호출하게 되고
#3. insertData함수는 radio버튼으로 넘어오는 데이터를 가지고 분석 결과를 리턴한다
#4. 그 후 forward 방식이 아닌 direct방식으로 클라이언트에서 요청을 하게 되는데
#5. /coffee 요청에 대해서 매인 urls가 아닌 mysurvey urls에서 처리를 하게 되고
#6. mysurvey urls에서는 /surveyshow 요청에 대해 dataAnalysis 함수를 실행하게 했다
#7. 즉 설문완료를 누르면 클라이언트에서 direct요청으로 dataAnalysis 함수를 실행하게 됨


def insertData(request):
    if request.method == 'POST':
        #print(request.POST.get('gender'))
        #print(request.POST.get('age'))
        #print(request.POST.get('co_survey'))
        
        #직접 sql문을 작성해서 입력 가능하지만 그러려면 conn연결 객체 등 해야할 것이 많으니 다른 방식으로 적음
        Survey(
            gender = request.POST.get('gender'), #ladio버튼은 반드시 입력값이 넘어오므로 이렇게 받을 수 있다
            age = request.POST.get('age'),
            co_survey = request.POST.get('co_survey')
        ).save()
        

def dataAnalysis(request):
    rdata = list(Survey.objects.all().values())
    df = pd.DataFrame(rdata)
    df.dropna() #데이터베이스에 맨 처음 값을 안 넣어주면 결측값이 생성됨
    ctab = pd.crosstab(index = df['gender'], columns = df['co_survey']) 
    
    #카이제곱 검정
    chi, pv, _, _ = stats.chi2_contingency(observed=ctab)
    print(chi, pv)
    if pv > 0.05 :
        result = "p값이 {0} >= 0.05이므로 성별과 커피 브랜드 선호도는 관련이 없다. (귀무채택, 대립가설 기각)".format(pv)
    else:
        result = "p값이 {0} < 0.05이므로 성별과 커피 브랜드 선호도는 관련이 있다. (귀무기각, 대립가설 채택)".format(pv)
    count = len(df) 
        
    
    #시각화 : 세로 막대
    #dummy변수 생성 문자열을 숫자로 바꿔줌
    df['co_num'] = df['co_survey'].apply(lambda c:1 if c == '스타벅스' else 2 if c == '커피빈' else 3 if c == '이디야' else 4)
    print(df)
    
    #이미지를 여기서 저장하고 있지만 안 좋은 방식이다
    fig = plt.gcf()
    gender_group = df['co_survey'].groupby(df['co_num']).count()
    gender_group.index = ['스타벅스', '커피빈', '이디야', '탐앤탐스']
    gender_group.plot.bar(subplots=True, color=['cyan', 'green'], width = 0.5)
    plt.xlabel('커피 브랜드명')
    plt.ylabel('커피 브랜드별 선호도')
    plt.grid()
    fig.savefig('django8_coffeedb/mysurvey/static/images/coffeebar.png')
    
    return render(request, 'list.html', {'ctab':ctab.to_html(), 'result':result, 'count':count})






