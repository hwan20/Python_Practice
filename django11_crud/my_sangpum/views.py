from django.shortcuts import render, redirect
from my_sangpum.models import Sangdata
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    """
    sql="select * from sangdata"
    cursor - conn.cursor()
    cursor.execute(sql)
    datas=cursor.fatchall()
    ...
    """
    # 페이지 나누기 안 함
    # datas=Sangdata.objects.all()
    # return render(request, 'list.html', {'sangpums':datas}) # forward 방식 서버에서 바로 클라이언트로 푸쉬하는 방식
    
    #페이지 나누기
    datas=Sangdata.objects.all().order_by('-code') #code별로 순서를 뒤집음
    
    #django에서 지원하는 page나누는 라이브러리
    paginator=Paginator(datas, 5) #한 페이지에서 5개씩 보겠다.
    try:
        page=request.GET.get('page') #get방식으로 페이지가 들어옴
    except: 
        page=1 #get방식으로 페이지가 안 떨어지면 페이지 1을 보여줌

    try:
        data = paginator.page(page)
    except PageNotAnInteger: #페이지 명을 입력하는데 정수가 아닐 경우
        data = paginator.page(1)
    except EmptyPage: #페이지가 받아지지 않은 경우
        data = paginator.page(paginator.num_pages())
    
    #개별 페이지 번호를 표시하고 싶을 경우
    allpage = range(paginator.num_pages + 1) 
    # print('allpage : ', allpage) #range(0, 4)
    
    return render(request, 'list2.html', {'sangpums':data, 'allpage':allpage})

def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        code = request.POST.get("code")
        print(code)
        
        #신상 code 중복 확인 후 추가 작업
        #코드 번호를 읽고 중복되면 에러가 안 떨어짐
        try:
            Sangdata.objects.get(code=request.POST.get("code"))
            #중복되는 코드가 있을 때
            return render(request, 'insert.html', {'msg':'이미 등록된 code입니다.'})
        except: #중복되는 코드 번호가 없어야 등록됨
            Sangdata(
                code = request.POST.get("code"),
                sang = request.POST.get("sang"),
                su = request.POST.get("su"),
                dan = request.POST.get("dan")
            ).save() #forward방식으로 전달하면 list를 못 만남
            return HttpResponseRedirect("/sangpum/list") #redirect 방식 클라이언트를 통해서 요청하는 방식
    
def UpdateFunc(request):
    data=Sangdata.objects.get(code=request.GET.get('code')) #query문으로 줘도 됨
    return render(request, 'update.html', {'sang_one':data})
    
    
def UpdateOkFunc(request):
    if request.method == 'POST':
        upRec = Sangdata.objects.get(code=request.POST.get('code')) #DB에서 code를 읽어옴
        upRec.code = code=request.POST.get('code')
        upRec.sang = code=request.POST.get('sang')
        upRec.su = code=request.POST.get('su')
        upRec.dan = code=request.POST.get('dan')
        upRec.save()
    
    #페이지번호도 넘겨줘야 2 페이지에서 수정완료해도 2 페이지가 보임 지금은 안 함
    return redirect("/sangpum/list") #HttpResponseRedirect를 줄여쓸수 있다

def DeleteFunc(request):
    delRec = Sangdata.objects.get(code=request.GET.get('code')) #get방식으로 넘기는 code번호를 받음
    delRec.delete()
    
    return redirect("/sangpum/list") #삭제 후 상품 보기



