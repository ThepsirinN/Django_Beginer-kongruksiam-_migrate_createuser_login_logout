# นอกจาก render แล้วใส่ redirect เพิ่ม
from django.shortcuts import render,redirect
# from django.http import HttpResponse,HttpRequest

from FirstDJGO.settings import TEMPLATES

# ดึง model Post เข้ามาเพื่อใช้ฐานข้อมูล
from .models import Post

# ดึง model user เข้ามาเพื่อใช้สมัครสมาชิก
# เพิ่ม auth เพือ ใช้ สอบ login
from django.contrib.auth.models import User,auth

# ไว้ส่งค่าข้อความ Error
from django.contrib import messages

# Create your views here.
def hello(request):
    """ # สร้าง Tag เพื่อนำไปใช้กับ For loop
    tags = ['น้ำตก','ธรรมชาติ','หน้าผน','ตากหมอก',]
    rating = 4
    # ทำการรับ request ให้วิ่งไปที่ templates/index.html *** dictionary ใช้ส่งค่าไป HTML ได้
    return render(request,'index.html',
    {'name':'บทความท่องเที่ยวภาคเหนือ',
    'author':'Thepsirin',
    'tags':tags,
    'rating':rating,
    }); """
    # Query data from model
    data = Post.objects.all()
    return render(request,'index.html',{'posts': data})

def page1(request):
    # สร้าง Tag เพื่อนำไปใช้กับ For loop
    tags = ['น้ำตก','ธรรมชาติ','หน้าผน','ตากหมอก',]
    rating = 4
    # ทำการรับ request ให้วิ่งไปที่ templates/index.html *** dictionary ใช้ส่งค่าไป HTML ได้
    return render(request,'page1.html',)
    
def createForm(request):
    # สร้าง Tag เพื่อนำไปใช้กับ For loop
    tags = ['น้ำตก','ธรรมชาติ','หน้าผน','ตากหมอก',]
    rating = 4
    # ทำการรับ request ให้วิ่งไปที่ templates/index.html *** dictionary ใช้ส่งค่าไป HTML ได้
    return render(request,'Form.html',)

def addUser(request):
    # for GET Mehthod
    """ name = request.GET['name']
    desc = request.GET['description'] """
    # for POST Method 
    usern = request.POST['username']
    first = request.POST['Firstname']
    last = request.POST['Lastname']
    email = request.POST['Email']
    passw = request.POST['Password']
    cfpass = request.POST['cfpass']
    if passw == cfpass:
        if User.objects.filter(username=usern).exists():
            messages.info(request,"entered User is existed")
            return redirect('/createForm')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"entered Email is existed")
            return redirect('/createForm')
        else:
            user = User.objects.create_user(
                username = usern,
                password = passw,
                email = email,
                first_name = first,
                last_name = last,
                )
            user.save()
            messages.info(request,'Success')
            return redirect('/')
    else:
        messages.info(request,"password not match")
        return redirect('/createForm')

def loginForm(request):
    return render(request,"login.html")

def login(request):
    usern = request.POST['username']
    passw = request.POST['Password']
    
    # check login
    clog = auth.authenticate(username=usern,password=passw)
    
    if clog is not None:
        auth.login(request,clog)
        return redirect('/')
    else:
        messages.info(request,'เข้าสู่ระบบไม่ถูกต้อง')
        return redirect('/loginForm')

def logout(request):
    auth.logout(request)
    return redirect('/')