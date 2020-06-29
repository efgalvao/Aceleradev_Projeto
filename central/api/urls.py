from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import EventAPI_objects, EventAPI_objects_details, Event_list


app_name = 'api'

urlpatterns = [
        path('event/', EventAPI_objects.as_view()),
        path('event/<int:pk>/', EventAPI_objects_details.as_view()),
        path('event/list/', Event_list.as_view(), name="events_list"),
        path('get_token', obtain_auth_token),
               
        ]

urlpatterns = format_suffix_patterns(urlpatterns)
