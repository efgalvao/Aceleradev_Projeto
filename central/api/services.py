from django.shortcuts import render
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'api/signup.html', {'form': form})

def get_all_events_by_group(request, group):
    queryset = Event.objects.filter(agent__user__group=group)
    return queryset

def order_events_by_level(request)
    queryset = Event.objects.order_by('level')
