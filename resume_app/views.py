from django.shortcuts import render, redirect
from .forms import basicForm
from django.http import HttpResponseRedirect

# Create your views here.
def basic(request):
	submitted = False
	if request.method == "POST":
		form = basicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/basic?submitted=True')
	else:
		form = basicForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'basic.html',{'form':form,'submitted':submitted})

def home(request):
	return render(request, 'home.html');

def login(request):
	return render(request, 'login.html')
	
def candidate(request):
	return render(request, 'candidate.html')

def basic_info(request):
	return render(request, 'basic_info.html')

def select_post(request):
	return render(request, 'select_post.html')

def upload_cv(request):
	return render(request, 'upload_cv.html')

def technical_info(request):
	return render(request, 'technical_info.html')

def success(request):
	return render(request, 'success.html')

