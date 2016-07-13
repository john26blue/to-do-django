"""tododjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from apps.views import *
from apps.auth import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', Login, name='login'),
    url(r'^logout/', Logout, name='logout'),
    url(r'^register/', Register, name='register'),

    url(r'^create/', Create.as_view(), name='create'),
    url(r'^delete/(?P<pk>[0-9]+)', Delete.as_view(), name='delete'),
    url(r'^mdelete/', MDelete, name='mutiple delete'),
    url(r'^change/(?P<pk>[0-9]+)', Change.as_view(), name='change'),
    url(r'finish/(?P<pk>[0-9]+)', Finish, name='finish'),

    url(r'^', MainPage.as_view(), name='mainpage'),
]
