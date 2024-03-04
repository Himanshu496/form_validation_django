from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('Name:', form.cleaned_data['name'])
            print('Email:', form.cleaned_data['email'])
            print('Password:', form.cleaned_data['password'])
        else:
            form = RegistrationForm()
    form = RegistrationForm()
    return render(request, 'register.html',{'form':form})
