from django.shortcuts import render

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def page1Func(request):
    return render(request, 'page1.html')

def page2Func(request):
    return render(request, 'page2.html')

def cartFunc(request):
    name = request.POST["name"] #form태그에서 POST방식으로 name이 넘어옴
    price = request.POST["price"]
    # name = request.GET["name"] #form태그에서 POST방식으로 name이 넘어옴
    # price = request.GET["price"]
    
    print(name, price)
    product = {"name" : name, "price" : price} #넘어온 데이터를 key, value형태로 dict 타입으로 저장한다 객체를 저장하는 java의 List와 비슷
    productList = [] #session에 상품의 정보를 key, value인 장바구니를 list형태로 넣는다
    
    if "shop" in request.session: #session이 생성되어있지 않으면, 즉 첫 번째 상품이 아니라면 productList에 상품 정보 저장하기
        productList = request.session["shop"]
        productList.append(product)
        request.session["shop"] = productList
    else: #session에 shop이 없으면 productList에 상품을 넣고 request.session에 "shop" 이라는 키를 만든다
        productList.append(product)
        request.session["shop"] = productList #접속자의 session 공간에 상품이 들어가있다
    
    #장바구니에 담기를 눌렀을 때 하나의 상품에 대한 정보가 product에 담겨서 넘어온다
    #이때 session에 shop이라는 이름의 session이 없으면 넘어온 product 정보를 productList에 담고
    #shop이라는 이름을 가진 session에 넣어놓는다.
    #이후 다른 product가 새로 장바구니에 담길 때 session이 아직 남아있다면
    #session에서 productList를 꺼낸후 product를 넣고 다시 session에 집어넣는다
    
    #productList에 담긴 내용 확인하기 위해서
    print(productList)
    context = {} #html에 보낼 용도
    context['products'] = request.session['shop']
    return render(request, 'cart.html',context) #html에 보낼 때는 반드시 key, value 형태



def buyFunc(request):
    if "shop" in request.session: #session이 있어야만 결제가 되니
        productList = request.session['shop']
        print(productList) #session에 있는게 다 보임
        total = 0 #고객한테 금액을 보여줘야 하니
        for pro in productList: #장바구니에 있는 상품들의 정보를 가져옴
            total += int(pro['price']) #client에서 넘오는 것은 무조건 str 형태이니 int로 바꿔줌
        print(total)
        request.session.clear() #session안에 모든 키 삭제
        
    return render(request, "buy.html",{'total':total}) #결제 총액을 buy.html 페이지에 렌더링해줌






