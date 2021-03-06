"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('demo/', include('demo.urls'))
"""
from django.contrib import admin
from django.urls import path
from demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.hello, name='hello'),
    path('whoami/', views.whoami),
    #path('', views.text_form, name='text_form'),
    path('', views.post_list, name='post_list'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('FastPow/', views.fast_power, name='fast_power'),
]
