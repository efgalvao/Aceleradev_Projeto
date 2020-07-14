from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Events_Search_description, Events_Search_address, Events_Search_level

urlpatterns = [
        path('search/level/', Events_Search_level.as_view()),
        path('search/desc/', Events_Search_description.as_view()),
        path('search/address/', Events_Search_address.as_view()),
        ]
urlpatterns = format_suffix_patterns(urlpatterns)
