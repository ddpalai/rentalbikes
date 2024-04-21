from django.shortcuts import render, redirect
from .models import UserRegistration
from testapp.forms import UserRegistrationForm

def welcome_page(request):
    return render(request, 'testapp/welcome_page.html')

def scooty_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result-page')  # Redirect to welcome page after successful submission
    else:
        form = UserRegistrationForm()
    return render(request, 'testapp/scooty_page.html', {'form': form})
def bike_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result-page')  # Redirect to welcome page after successful submission
    else:
        form = UserRegistrationForm()
    return render(request, 'testapp/bike_page.html', {'form': form})
def result_page(request):
    return render(request, 'testapp/result.html')
