# -*- coding: utf-8 -*-
"""RV1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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

# Use to map urls with python function
from django.conf.urls import url
# Use to have access to python functions that load the templates
from RV1.views import welcome, login, home

""" url('regexp', f) --> url(^welcome$, project.views.welcome)
        regexp   = url / string after "www.project.com/"
        f        = python function
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', login),
    url('^welcome$', welcome),
    url('^login$', login),
    url('^home$', home)
]
