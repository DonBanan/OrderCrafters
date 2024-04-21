from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import CustomUserCreationForm


# Так как проект требует небольшого количеством логики то я буду использовать функциональные представлени.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_customer = form.cleaned_data['is_customer']
            user.is_performer = form.cleaned_data['is_performer']
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('home')
