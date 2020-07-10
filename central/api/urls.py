from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_auth.views import LoginView
from .views import Events_Search_description, Events_Search_address, Events_Search_level
from .views import Cadastrar_View, User_list



urlpatterns = [
        #path('erro/', Erro_List.as_view()), # get all events
        #path('agent/<int:agent_id>/event/', Events_Agentsid.as_view()), #get_all_events
        #path('group/<int:id>/event/', Events_By_Groupid.as_view()), # ok
        #path('event/level/', Events_Ordered_by_Level.as_view()),  # ok
        path('search/level/', Events_Search_level.as_view()),
        path('search/desc/', Events_Search_description.as_view()),
        path('search/address/', Events_Search_address.as_view()),

        #path('event/<int:pk>/', Event_details.as_view()),
        #path('event/list/', Event_List.as_view(), name="events_list"),
        #path('agent/', Agent_Create.as_view()),
        #path('agent/<int:pk>/', Agent_Details.as_view()),
        #path('agent/list/', Agent_List.as_view()),
        #path('agent/<int:agent_id>/event/<int:id>/', Event_details.as_view()),
        #path('list/', User_list.as_view(), name='user_list'),
        path('cadastrar/', Cadastrar_View.as_view(), name='cadastrar'),

        ]
urlpatterns = format_suffix_patterns(urlpatterns)
