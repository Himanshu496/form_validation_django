from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            return render(request, 'submitt.html', {'name': name , 'email':email, 'password':password})
        else:
            form = RegistrationForm()
    form = RegistrationForm()
    return render(request, 'register.html',{'form':form})
