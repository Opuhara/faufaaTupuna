# users/views.py
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import AppUserCreationForm, AppUserChangeForm


def register(request):
	if request.method == "POST":
		form = AppUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('profile')
	else:
		form = AppUserCreationForm()
	return render(request, 'register.html', {'form': form})


def login_view(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('profile')
	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {'form': form})


def logout_view(request):
	if request.method == "POST":
		logout(request)
		return redirect('login')


def profile(request):
	if request.method == "POST":
		form = AppUserChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = AppUserChangeForm(instance=request.user)
	return render(request, 'profile.html', {'form': form})
