"""central URL Configuration

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
from django.urls import path, include
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from api.views import EventViewSet, Register_View, Filter, Level, Freq
from rest_framework.routers import DefaultRouter
from rest_framework import permissions


router = DefaultRouter()
router.register(r'event', EventViewSet, basename="Events")

urlpatterns = [
        path('', include(router.urls)),
        path('admin/', admin.site.urls),
        path('api/', include('api.urls')),
        path('register/', Register_View.as_view()),
        path('get_token/', obtain_auth_token),
        url('^event/(?P<env>.+)/$', Filter.as_view()),
        url('^event/level', Level.as_view()),
        url('^event/freq', Freq.as_view()),

]
