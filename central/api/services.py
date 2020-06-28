from django.shortcuts import render
from .models import Event
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm

"""
def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'api/register.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            #elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                #return render(request, template, {
                    #'form': form,
                    #'error_message': 'Passwords do not match.'
                #})
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.save()
                messages.success(request, 'Account created successfully')
               
                # Login the user
                #login(request, user)
               
                # redirect to accounts page:
                return HttpResponseRedirect('/admin')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})
"""
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

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
 
 
        
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
 

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
 
    else:
        f = CustomUserCreationForm()
 
    return render(request, 'cadmin/register.html', {'form': f})