"""recruitme URL Configuration

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

from recruit import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sith/', views.choose_sith, name='chose_sith'),
    path('new_recruit/', views.RecruitCreate.as_view(), name='new_recruit'),
    path('test/<str:recruit>/<int:num>', views.test, name='test'),
    path('success/', views.success, name='success'),
    path('sith/<int:pk>', views.ChooseRecruit.as_view(), name='choose_recruit')

]
