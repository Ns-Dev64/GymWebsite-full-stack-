"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from mygym import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('admin/', admin.site.urls),
    path('dashboard/',views.dashboard,name='profile'),
    path('editdashboard/',views.editdashboard,name='edit'),
    path('',views.homepage,name='home'),
    path('qrcode/',views.genqrcode,name='qrcode'),
    path('logout/',views.logout_page,name='logout'),
    path('contactus/',views.contact,name='contact'),
    path('login/',views.login_page,name='login'),
    path('extends/',views.test),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('deleteprofile/',views.deleteprofile,name='deleteprofile'),
    path('accountcreated/',views.accountcreated,name='accountcreate'),
    path('accountdeleted/',views.accountdeleted,name='accountdelete'),
]
