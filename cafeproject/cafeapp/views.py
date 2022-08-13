from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html') #html 요청을 받고 로직처리후 템플릿 처리를 하고 html로 된 최종 데이터를 클라이언트로 반환

    
def detail(request):
    return render(request, 'portfolio-details.html')