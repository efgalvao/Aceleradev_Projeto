from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import EventAPI_objects, Event_details, Event_list, Events_Agentsid
from api.views import Agent_Create, Agent_Details, Agent_List


app_name = 'api'

urlpatterns = [
        path('event/', EventAPI_objects.as_view()),
        path('event/<int:pk>/', Event_details.as_view()),
        path('event/list/', Event_list.as_view(), name="events_list"),
        path('agent/', Agent_Create.as_view()),
        path('agent/<int:pk>/', Agent_Details.as_view()),
        path('agent/list/', Agent_List.as_view()),
        path('agent/<int:pk>/event/', Events_Agentsid.as_view()),
        ]
urlpatterns = format_suffix_patterns(urlpatterns)
