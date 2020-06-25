from django.shortcuts import render
from .forms import SignUpForm
from .models import Event

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'api/signup.html', {'form': form})

def get_all_events():
    queryset = Event.objects.all()
    return queryset

def get_all_events_by_group(request, group):
    queryset = Event.objects.filter(agent__user__group=group)
    return queryset

def order_events_by_level(request):
    queryset = Event.objects.order_by('level')
    return queryset

def order_events_by_frequency():# Frequencia baseada em que ?
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
