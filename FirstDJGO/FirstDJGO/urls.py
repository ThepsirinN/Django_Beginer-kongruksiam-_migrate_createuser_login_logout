"""FirstDJGO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# import views เพิ่มจาก blogs
from blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # ใส่ path เพือให้วิ่งไป def hello() ใน views.py
    path('', views.hello,name = 'หน้าแรกนะจ๊ะ'),
    path('page1/', views.page1),
    path('createForm/', views.createForm),
    path('addForm', views.addUser),
    path('loginForm', views.loginForm),
    path('login', views.login),
    path('logout', views.logout),
]
