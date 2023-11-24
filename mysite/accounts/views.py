from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('stacktry:profile', user_id=user.id)  # Replace 'home' with the desired URL after signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
