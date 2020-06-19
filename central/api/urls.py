from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('basic/', views.LivroAPI_objects.as_view()),
    path('basic/<int:pk>/', views.LivroAPI_objects_details.as_view()),
    path('basic/', views.AutorAPI_objects.as_view()),
    path('basic/<int:pk>/', views.AutorAPI_objects_details.as_view()),    
    path('basic/', views.GeneroAPI_objects.as_view()),
    path('basic/<int:pk>/', views.GeneroAPI_objects_details.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)