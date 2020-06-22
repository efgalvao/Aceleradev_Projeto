from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (UserAPI_objects, UserAPI_objects_details, AgentAPI_objects,
                    AgentAPI_objects_details, GroupAPI_objects, GroupAPI_objects_details,
                    EventAPI_objects, EventPI_objects_details, )

urlpatterns = [
        path('user/', UserAPI_objects.as_view()),
        path('user/<int:pk>/', UserAPI_objects_details.as_view()),
        path('agent/', AgentAPI_objects.as_view()),
        path('agent/<int:pk>/', AgentAPI_objects_details.as_view()),
        path('group/', GroupAPI_objects.as_view()),
        path('group/<int:pk>/', GroupAPI_objects_details.as_view()),
        path('event/', EventAPI_objects.as_view()),
        path('event/<int:pk>/', EventPI_objects_details.as_view()),

        ]
urlpatterns = format_suffix_patterns(urlpatterns)
