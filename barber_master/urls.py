"""barder_proj URL Configuration

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
from django.conf.urls import url, include
from django.urls import path
from . import views
from . import forms

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^master_info/$', views.form),
    url(r'^add_master/$', views.add_master),
    url(r'^$', views.MainView.as_view()),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^current_master_info/$', views.current_master_info),
    url(r'^change_masters_info/$', views.change_masters_info),
    url(r'^set_time_for_haircut/$', views.time_for_haircut),
    url(r'^add_time_for_haircut/$', views.add_time_for_haircut),
]
