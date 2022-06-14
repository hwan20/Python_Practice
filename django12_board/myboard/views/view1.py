from django.shortcuts import render, redirect
from myboard.models import BoardTab
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage #리스트의 page처리위해
from datetime import datetime #게시글 작성 시간을 알리기 위해 import 

def mainFunc(request):
    ss = "난 메인 화면 ~~~"
    imsi = "<div><h2>"+ss+"</h2></div>"
    return render(request, 'main.html', {"msg":imsi})


def listFunc(request):
    data_all = BoardTab.objects.all().order_by('-id') #id desc
    
    paginator = Paginator(data_all, 10)
    page = request.GET.get('page')
    
    try:
        datas = paginator.page(page)
    except PageNotAnInteger:
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages())
        
    return render(request, 'board.html', {'datas':datas})


def insertFunc(request):
    return render(request, 'insert.html')


def insertOkFunc(request):
    if request.method == 'POST':
        try:
            gbun = 1 #group num 구하기,  원글과 답글을 묶어주는
            datas = BoardTab.objects.all()
            if datas.count() != 0: #BoardTab에서 읽어온 데이터의 숫자가 0이 아니라면 - 데이터가 이미 있으면
                gbun = BoardTab.objects.latest('id').id + 1 #가장 마지막 숫자의 +1을 해줌
                
            BoardTab(
                name = request.POST.get('name'),
                passwd = request.POST.get('passwd'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                #작성되어 넘어오는 데이터는 이렇게 작성, 추가로 작성해줘야 할 내용은 다음과 같이 작성
                bip = request.META['REMOTE_ADDR'],
                bdate = datetime.now(),
                readcnt = 0,
                gnum = gbun,
                onum = 0,
                nested = 0, 
            ).save()
        except Exception as e:
            print('추가 에러', e)
            return render(request, 'error.html')
    
    return redirect('/board/list') #추가 후 목록을 보기 위해 redirect요청


def searchFunc(request): #검색용
    if request.method == 'POST':
        s_type = request.POST.get('s_type')
        s_value = request.POST.get('s_value')
        # print(s_type, s_value)
        
        #sql의 like연산자와 비슷
        #이렇게 작성하면 dataset으로 넘어가고 sql문으로 작성하면 tuple로 넘어감
        if s_type == 'title':
            datas_search = BoardTab.objects.filter(title__contains=s_value).order_by('-id') #id별 desc 
        elif s_type == 'name':
            datas_search = BoardTab.objects.filter(name__contains=s_value).order_by('-id')
        
        #검색 데이터가 많으면 페이징 처리
        paginator = Paginator(datas_search, 10)
        page = request.GET.get('page')
        
        try:
            datas = paginator.page(page)
        except PageNotAnInteger:
            datas = paginator.page(1)
        except EmptyPage:
            datas = paginator.page(paginator.num_pages())
        
    return render(request, 'board.html', {'datas':datas})

        
def contentFunc(request):
    page = request.GET.get('page') #get방식으로 page와 id가 넘어오는 것에서 page를 받음
    data = BoardTab.objects.get(id=request.GET.get('id')) #get방식으로 page와 id가 넘어오는 것에서 id를 받음
    data.readcnt = data.readcnt+1 #조회수 +1
    data.save() #조회수 갱신
    
    return render(request, 'content.html', {'data_one':data, 'page':page}) #이렇게 하기 싫으면 session을 활용
    

def updateFunc(request):
    #에러가 발생할지 안 할지 모르지만 작성해야함
    try:
        data = BoardTab.objects.get(id=request.GET.get('id'))
    except Exception as e:
        print('수정 자료 읽기 오류 : ', e)
        return render(request, 'error.html')
    
    return render(request, 'update.html', {'data_one':data})

def updateOkFunc(request):
    try:
        upRec = BoardTab.objects.get(id=request.POST.get('id'))
        
        #여기서 비밀번호 비교 후 수정 처리를 하면 됨
        
    except Exception as e:
        print('수정 자료 업데이트 오류 : ', e)
        return render(request, 'error.html')
    
    return redirect("/board/list") #수정 후 목록 보기

def deleteFunc(request):
    pass


def deleteOkFunc(request):
    pass

    