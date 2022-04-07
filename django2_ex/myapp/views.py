from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, "main.html")

def transFunc(request):
    request.method == 'GET' 
    gender = request.GET['gender']
    return render(request, "show.html", {'gender':gender})


