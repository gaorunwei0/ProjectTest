from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.views import View
from django.core.urlresolvers import reverse


# Create your views here.
from users.forms import UserLoginForm


class IndexView(View):
	def get(self,request):
		return render(request, 'index.html')


def user_reg(request):
	if request.method=="GET":
		return render(request,'users/reg.html')



def user_login(request):
	if request.method == 'GET':
		return render(request,"users/login.html")
	else:
		print("++++++++++++++++++++++++++++++++++++++")
		user_login_form = UserLoginForm(request.POST)
		if user_login_form.is_valid():
			print("LOG+++++++++++++++")
			username = user_login_form.cleaned_data['username']
			password = user_login_form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			user_2 = authenticate(email=username, password=password)
			if user:
				login(request,user)
				return redirect(reverse('index'))
			else:
				return render(request,'users/login.html',{"msg":"用户名或密码错误"})
		else:
			return render(request, 'users/login.html', {
				'user_login_form': user_login_form
			})