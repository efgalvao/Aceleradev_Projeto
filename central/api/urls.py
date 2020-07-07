from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_auth.views import LoginView
from .views import Event_Detail, Event_List, Events_Agentsid, Events_By_Groupid
from .views import Agent_Create, Agent_Details, Agent_List, Cadastrar_View, User_list
from .views import Events_Ordered_by_Level, Events_Search_level, Event_Create

urlpatterns = [
        path('event/create/', Event_Create.as_view()), # Create an event
        path('event/', Event_List.as_view()), # get all events
        path('agent/<int:agent_id>/event/', Events_Agentsid.as_view()), #get all events of an agent
        path('group/<int:id>/event/', Events_By_Groupid.as_view()), # get all events of an group
        path('event/level/', Events_Ordered_by_Level.as_view()),  # get all events of an ordered by level
        path('event/search/', Events_Search_level.as_view()),
        


        path('evento/', Event_Detail.as_view({'get': 'list'})),
        path('event/list/', Event_List.as_view(), name="events_list"),
        path('agent/', Agent_Create.as_view()),
        path('agent/<int:pk>/', Agent_Details.as_view()),
        path('agent/list/', Agent_List.as_view()),
        
        path('list/', User_list.as_view(), name='user_list'),
        path('cadastrar/', Cadastrar_View.as_view(), name='cadastrar'),



        ]
urlpatterns = format_suffix_patterns(urlpatterns)
