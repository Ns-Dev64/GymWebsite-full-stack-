# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login , logout , authenticate 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User , Member , queries
import stripe
from django.http import HttpResponse
import io
import qrcode
stripe.api_key='sk_test_51OdrStSGscJjE81T5VKGeFcXGy8DWplhGaCWuqoMa4ZJjWZoXgMm4TDxkeR6Cbyp3z02Vbn17HZmFB5ybCngHchj00qGpwT8Pz'

@login_required(login_url="/login/")
def accountcreated(request):
    return render(request,'AccountCreated.html')
@login_required(login_url="/login/")
def accountdeleted(request):
    return render(request,'AccountDeleted.html')
def test(request):
    return render(request,'test.html')
@login_required(login_url="/login/")
def deleteprofile(request):
    if request.method=="POST":
        data=request.POST
        password=data.get("cf-password")
        user=authenticate(username=request.user.username,password=password)
        if user is None:
            messages.error(request,"Invalid password")
        else:
            user=User.objects.filter(username=request.user.username)
            member=Member.objects.filter(username=request.user.username)
            user.delete()
            member.delete()
            return redirect('accountdelete')
    return redirect('home')
@login_required(login_url="/login/")
def editdashboard(request):
    queryset=Member.objects.filter(username=request.user.username)
    context={'member':queryset}
    if request.method=="POST":
        data=request.POST
        password=data.get("cf-password")
        user=authenticate(username=queryset[0].username,password=password)
        if user is None:
            messages.error(request,"Invalid password")
            return redirect('/editdashboard/')
        else:
            if 'cf-name' in data and data['cf-name'].strip() != '':
                updated_username=data.get("cf-name")
            else:
                updated_name=queryset[0].username
            if 'cf-full_name' in data and data['cf-full_name'].strip !='':
                updated_fullname=data.get("cf-full_name")
            else:
                updated_fullname=queryset[0].full_name
            if 'cf-email' in data and data['cf-email'].strip() != '':
                updated_email=data.get("cf-email")
            else:
                updated_email=queryset[0].email
            if  'cf-phone' in data and data['cf-phone'].strip() != '':
                updated_phone=data.get("cf-phone")
            else:
                updated_phone=queryset[0].phone
            user=User.objects.filter(username=queryset[0].username).update(
                username=updated_username,
                email=updated_email
            )
            member=Member.objects.filter(username=queryset[0].username).update(
                username=updated_username,
                full_name=updated_fullname,
                email=updated_email,
                phone=updated_phone
            )
            return redirect('/dashboard/')           
    return render(request,'editdashboard.html',context)

@login_required(login_url="/login/")
def dashboard(request):
    queryset=Member.objects.filter(username=request.user.username)
    context={'member':queryset}
    return render(request,'dashboard.html',context)

@login_required(login_url="/login/")
def genqrcode(request):
    qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
    )
    item=''
    queryset1=User.objects.filter(username=request.user.username)
    item=item+' '+queryset1[0].username
    item=item+' '+queryset1[0].password
    data=item
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return HttpResponse(buffer.read(), content_type="image/png")


def homepage(request):
    
    return render(request,'index.html')


def register(request):
    logout(request)
    if request.method=="POST":
        data=request.POST
        name=data.get("cf-name")
        email=data.get("cf-email")
        phone=data.get("cf-phone")
        comment=data.get("cf-message")
        full_name=data.get("cf-full_name")
        classes=[]
        if 'yoga' in data:
            classes.append("yoga")
        if 'cardio' in data:
            classes.append("cardio")
        if 'aerobics' in data:
            classes.append("aerobics")
        password=data.get("cf-password")
        user=User.objects.filter(username=name)
        if user.exists():
            messages.error(request,'Username already exsits')
            return redirect('/register/')
        user=User.objects.filter(email=email)
        if user.exists():
            messages.error(request,'email is already associated with a different account')
            return redirect('/register/')
        
        user=User.objects.create(
                username=name,
                email=email,
            )
        user.set_password(password)
        user.save()
        member=Member.objects.filter(username=name)
        if member.exists():
            messages.error(request,'Username already exsits')
            return redirect('/register/')
        member=Member.objects.filter(email=email)
        if member.exists():
            messages.error(request,'email is already associated with a different account')
            return redirect('/register/')
        item=''
        for i in classes:
            item=item+','+' '+i.strip()
        classes=item
        member=Member.objects.create(
               username=name,
               full_name=full_name,
               email=email,
               phone=phone,
               comment=comment,
               classes=classes
        )
        
        member.save()
        messages.info(request,'account created successfully')
        login(request,user)
        return redirect('accountcreate')
    return render(request,'memebership.html')
    

def login_page(request):
    logout(request)
    if request.method=="POST":
        data=request.POST
        username=data.get("username")
        password=data.get("password")
        user=User.objects.filter(username=username)
        if user.exists():
            user=authenticate(username=username,password=password)
            if user is None:
                messages.error(request,'invalid password')
                return redirect('/login/')
            else:
                login(request,user)
                return redirect('/dashboard/')
        else:
            messages.error(request,'Invalid username')
            return redirect('/login/')
    return render(request,'login.html')

def contact(request):
    if request.method=="POST":
        data=request.POST
        name=data.get("cf-name")
        email=data.get("cf-email")
        comment=data.get("cf-message")
        query=queries.objects.create(
            name=name,
            email=email,
            comment=comment
        )
        query.save()
        messages.info(request,"We'll send you a response on your email ASAP!!")
    return redirect('home')
def logout_page(request):
    logout(request)
    return redirect('/login/')

def forgotpassword(request):
    
    return render(request,'forgotpassword.html')