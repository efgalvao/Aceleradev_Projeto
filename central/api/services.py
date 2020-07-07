from django.shortcuts import render
from .models import Event


def get_all_events(): # ok
    queryset = Event.objects.all()
    return queryset

def get_all_events_by_group(request, group):# ok
    queryset = Event.objects.filter(agent__user__group=group)
    return queryset

def order_events_by_level(request): # ok
    queryset = Event.objects.order_by('level')
    return queryset

def order_events_by_frequency():# Frequencia baseada em que ?
    queryset = Event.objects.order_by
    pass

def search_events_for_level(request, campo):
    queryset = Event.objects.filter(level__search=campo)
    return queryset

def search_events_for_description(request, campo):# data é diferente de description
    queryset = Event.objects.filter(data__search=campo)
    return queryset

def search_events_for_address(request, campo):
    queryset = Event.objects.filter(agent__address__search=campo)
    return queryset

def get_all_events_by_agent(request, id): # ok
    queryset = Event.objects.filter(agent__id__filter=id)
    return queryset

