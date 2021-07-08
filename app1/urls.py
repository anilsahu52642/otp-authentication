
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name='signup'),
    path('otp/', views.varifyotp, name='otp'),
    path('signin/', views.signin, name='signin'),


    path('profile/',views.profile,name='profile'),
    path('logout/',views.mylogout,name='logout')


]