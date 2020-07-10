from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_auth.views import LoginView
from .views import Events_Search_description, Events_Search_address, Events_Search_level
from .views import Cadastrar_View, User_list



urlpatterns = [
        path('search/level/', Events_Search_level.as_view()),
        path('search/desc/', Events_Search_description.as_view()),
        path('search/address/', Events_Search_address.as_view()),
        path('cadastrar/', Cadastrar_View.as_view(), name='cadastrar'),

        ]
urlpatterns = format_suffix_patterns(urlpatterns)
