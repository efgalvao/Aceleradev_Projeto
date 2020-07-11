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
from api.views import EventViewSet, Register_View
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()
router.register(r'event', EventViewSet, basename="Events")

schema_view = get_schema_view(
   openapi.Info(
      title="Central de Erros API",
      default_version='v1',
      description="API for manage error logs saved in DB",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="efgalvao@mail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
        path('', include(router.urls)),
        path('admin/', admin.site.urls),
        path('api/', include('api.urls')),
        path('register/', Register_View.as_view(), name='register'),
        path('get_token/', obtain_auth_token),
        url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
        url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
                                     name='schema-swagger-ui'),
        url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

        ]