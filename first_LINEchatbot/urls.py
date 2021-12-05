"""first_LINEchatbot URL Configuration

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
from django.urls import path, include
from django.conf.urls import url

from chatbot.views import RESUME
from chatbot.views import meichu_hackathon
from chatbot.views import LINE_FRESH
from chatbot.views import about_me
from chatbot.views import database
from chatbot.views import machine_learning
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('chatbot.urls')), #包含應用程式的網址
    url(r'^RESUME/$', RESUME),
    url(r'^meichu_hackathon/$', meichu_hackathon),
    url(r'^LINE_FRESH/$', LINE_FRESH),
    url(r'^about_me/$', about_me),
    url(r'^database/$', database),
    url(r'^machine_learning/$', machine_learning),
]
