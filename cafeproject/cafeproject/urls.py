
from django.contrib import admin
from django.urls import path
from cafeapp import views

urlpatterns = [
    path('admin/', admin.site.urls), #url리스트 검사-url 패턴이 일치하면 검사를 종료-호출
    path('', views.home, name='home'), 
    path('detail/', views.detail, name='detail'),
]
