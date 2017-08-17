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

			return redirect("menu:list")

		messages.error(request, form.errors)
		return redirect("menu:signup")
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
				return redirect("menu:list")
			messages.warning(request, "Wrong Username/password combination. Please try again.")
			return redirect("menu:login")
		messages.warning(request, form.errors)

		return redirect("menu:login")
	return render(request, 'login.html', context)

def userlogout(request):
    logout(request)
    return redirect("menu:list")



def bean_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	form = BeanForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.author = request.user
		form.save()
		messages.success(request, "Bean created")
		return redirect("menu:beancreate")
	context = {
		"form": form,
	}

	return render(request, 'bean_create.html', context)


def bean_update(request, bean_id):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	bean_object = get_object_or_404(Bean, id=bean_id)
	form = BeanForm(request.POST or None, request.FILES or None, instance=bean_object)
	if form.is_valid():
		form.save()
		messages.success(request, "Bean updated")
		return redirect("menu:beanupdate")
	context = {
		"form": form,
		"bean_object": bean_object,
	}

	return render(request, 'bean_update.html', context)

def bean_delete(request, bean_id):
	if not (request.user.is_superuser):
		raise Http404
	Bean.objects.get(id=bean_id).delete()
	messages.warning(request, "Bean deleted")

	return redirect("menu:beandelete")

def bean_list(request):
	obj_list = Bean.objects.all()

	context = {
	"bean_list": obj_list,
	
	}

	return render(request, 'bean_list.html', context)

def bean_detail(request, bean_id):
	obj = get_object_or_404(Bean, id=bean_id)
	

	context = {
		"instance": obj,
		
	}
	return render(request, 'bean_detail.html', context)






