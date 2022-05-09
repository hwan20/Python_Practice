from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import json
from jikwon_app.models import Jikwon

# Create your views here.

def MainFunc(request):
    return render(request, 'main.html')

#client에서 post방식으로 전송을 할 떄는 보안을 위해 csrf_token이 있어야 하는데
#form태그가 아닌 input과 btn으로 전송해서 csrf_token을 장식자로 해서 예외 적용시킴
@csrf_exempt
def PredictFunc(request):
    year = request.POST['year']
    new_val = pd.DataFrame({'year':[year]}) 
    #넘어오는 year값을 dataframe으로 보기 위해 key,value로 데이터를 넣어줌
    
    #print(year)
    #print(new_val)
    
    #모델 생성
    #input btn을 클릭하면 database의 jikwon table의 아래 칼럼의 전체 데이터를 보내줌
    datas = Jikwon.objects.values('jikwon_ibsail', 'jikwon_pay', 'jikwon_jik').all()
    jikwon = pd.DataFrame.from_records(datas)
    #print(jikwon)
    
    #근무년수 구하기
    for i in range(len(jikwon['jikwon_ibsail'])):
        jikwon['jikwon_ibsail'][i] = int((datetime.now().date() - jikwon['jikwon_ibsail'][i]).days/365)
        #jikwon 테이블의 jikwon_ibsail 칼럼의 i번째 데이터 값의 근무 년수를 확인하기 위해 현재 날짜에서 jikwon_ibsail 날짜를 뺀 후에 년으로 나눔
        
    jikwon.columns = ['근무년수', '연봉', '직급']
    #print(jikwon)
    
    #모델은 처음 한 번만 만들고 별도로 작성해야 함 - coffeedb만들때처럼
    
    train_set, test_set = train_test_split(jikwon, test_size = 0.2)
    print(train_set.shape, test_set.shape) #(24, 3) (6, 3) 30행을 8:2로 나눔
    
    #model
    model_lr = LinearRegression().fit(X = train_set.iloc[:,[0]], y = train_set.iloc[:,[1]])
    
    #성능평가는 test_set
    test_pred = model_lr.predict(test_set.iloc[:,[0]])
    test_real = test_set.iloc[:, 1]
    #print('예측값 : ', test_pred)
    #print('실제값 : ', test_real)
    
    #성능평가 
    lin_mse = mean_squared_error(test_real, test_pred)
    lin_rmse = np.sqrt(lin_mse)
    r2 = r2_score(test_real, test_pred)
    print('RMSE : ', lin_rmse)
    print('r2_score : ', r2)
    
    
    #새로운값 예측
    new_pred = round(model_lr.predict(new_val)[0][0],2)
    print(new_pred)
    
    
    #직급별 연봉 평균
    pay_jik = jikwon.groupby('직급').mean().round(1)
    pay_jik2 = pay_jik.to_html()
    
    #return JsonResponse({'new_pred' : new_pred, 'pay_jik' : pay_jik2, 'r2':r2})
    #아래와 같이 작성해도 됨
    
    context = {'new_pred' : new_pred, 'pay_jik' : pay_jik2, 'r2':r2}
    return HttpResponse(json.dumps(context), content_type='application/json')
    
    
    
    