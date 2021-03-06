"""Swan_Task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Swan_App import views
from Swan_Task import settings
from Swan_App import views

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('demo/', views.demo, name='demo'),
    path('category/', views.category, name='category'),
    path('elements/', views.elements, name='elements'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('registrationaction/', views.registrationaction, name='registrationaction'),
    path('loginaction/',views.loginaction, name='loginaction'),
    path('addcartaction/',views.addcartaction, name='addcartaction'),
    path('logout/',views.logout, name='logout')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
