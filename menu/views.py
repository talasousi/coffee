from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .models import *
from django.shortcuts import get_object_or_404
from .forms import *
from django.contrib	import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout


def usersignup(request):
	context = {}
	form = UserSignUp()
	context['form'] = form
	if request.method == "POST":
		form = UserSignUp(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			username = user.username
			password = user.password
			user.set_password(password)
			user.save()
			auth_user = authenticate(username=username, password=password)
			login(request, auth_user)

			return redirect("posts:list")

		messages.error(request, form.errors)
		return redirect("posts:signup")
	return render(request, 'signup.html', context)

def userlogin(request):
	context = {}
	form = UserLogin()
	context['form'] = form
	if request.method == "POST":
		form = UserLogin(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect("posts:list")
			messages.warning(request, "Wrong Username/password combination. Please try again.")
			return redirect("posts:login")
		messages.warning(request, form.errors)

		return redirect("posts:login")
	return render(request, 'login.html', context)

def userlogout(request):
    logout(request)
    return redirect("posts:list")

