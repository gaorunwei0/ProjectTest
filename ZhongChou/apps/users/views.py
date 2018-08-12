from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from users.forms import UserLoginForm, UserRegForm, UserapplyDataForm
from users.models import UserProfile


def index(request):
	return render(request, 'index.html')


def user_reg(request):
	if request.method == "GET":
		return render(request, 'users/reg.html')
	else:
		user_register_form = UserRegForm(request.POST)
		if user_register_form.is_valid():
			username = user_register_form.cleaned_data['username']
			password = user_register_form.cleaned_data['password']
			email = user_register_form.cleaned_data['email']
			user = UserProfile.objects.filter(username=username)
			is_email = UserProfile.objects.filter(email=email)
			if user:
				return render(request, 'users/reg.html', {'msg': '用户名已存在'})
			elif is_email:
				return render(request, 'users/reg.html', {'msg': '此邮箱已注册'})
			else:
				a = UserProfile()
				a.username = username
				a.email = email
				a.password = password
				a.set_password(password)
				a.save()
				return redirect(reverse('users:login'))
		else:
			return render(request, 'users/reg.html', {
				'user_register_form': user_register_form
			})


def user_login(request):
	if request.method == 'GET':
		return render(request, "users/login.html")
	else:
		print("++++++++++++++++++++++++++++++++++++++")
		user_login_form = UserLoginForm(request.POST)
		if user_login_form.is_valid():
			print("LOG+++++++++++++++")
			username = user_login_form.cleaned_data['username']
			password = user_login_form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				return redirect(reverse('index'))

			else:
				return render(request, 'users/login.html', {"msg": "用户名或密码错误"})
		else:
			return render(request, 'users/login.html', {
				'user_login_form': user_login_form
			})


def user_logout(request):
	logout(request)
	return redirect(reverse('index'))


def user_member(request):
	return render(request,'users/member.html')


def user_accttype(request):
	return render(request,'users/accttype.html')


def user_apply(request):
	if request.method=="GET":
		data = request.get_full_path()
		if data.find('users/apply/?user_data=%23')>-1:
			a_choice = int(data[-1])
			print(a_choice)
			a=UserProfile.objects.get(username=request.user)
			a.accounttype = a_choice
			a.save()
		return render(request,'users/apply.html')
	else:
		apply_zero = UserapplyDataForm(request.POST)
		if apply_zero.is_valid():
			name = apply_zero.cleaned_data['name']
			idcard = apply_zero.cleaned_data['idcard']
			phonenum = apply_zero.cleaned_data['phonenum']
			a=UserProfile.objects.get(username=request.user)
			a.name=name
			a.idcard=idcard
			a.phonenum=phonenum
			return render(request, 'users/apply-1.html')
		else:
			return render(request, 'users/apply.html', {
				'user_': apply_zero
			})



def user_apply_1(request):
	return render(request, 'users/apply-1.html')