from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from ZhongChou import settings
from trade.models import OrderInfo
from users.forms import UserLoginForm, UserRegForm, UserapplyDataForm, Userapply_1_DataForm, Userapply_2_DataForm
from users.models import UserProfile, UserProfile_tem
import random
from django.core.mail import send_mail
from datetime import datetime, timedelta
from project.models import ProjectProfile

def get_code():
	data = '0123456789'
	email_codes = []
	for i in range(4):
		email_codes.append(random.choice(data))
	email_code = ''.join(email_codes)
	return email_code

def index(request):
	allproject = ProjectProfile.objects.all()

	#轮播图
	head_pro = allproject.order_by('favnums')
	head_pro_1 = head_pro[0]
	head_pro_2 = head_pro[1]
	head_pro_3 = head_pro[2]

	#广告位
	add_pro = allproject.order_by('-add_level')[:3]

	#分类

	cat1 = allproject.filter(category=1)[:4]
	cat2 = allproject.filter(category=2)[:4]
	cat3 = allproject.filter(category=4)[:4]
	cat_other = allproject.filter(category=3)[:4]

	time_now = datetime.now()


	return render(request, 'index.html',{
		'head_pro_1':head_pro_1,
		'head_pro_2':head_pro_2,
		'head_pro_3':head_pro_3,
		'add_pro':add_pro,
		'cat1':cat1,
		'cat2':cat2,
		'cat3':cat3,
		'cat_other':cat_other,
		'time_now':time_now,
	})


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
			print(request.user.username)
			try:
				a=UserProfile_tem.objects.get(user=request.user.username)
				if a:
					a.accounttype = a_choice
					a.save()
			except:
				a = UserProfile_tem()
				a.user = request.user.username
				a.accounttype = a_choice
				a.save()
		return render(request,'users/apply.html')
	else:
		apply_zero = UserapplyDataForm(request.POST)
		if apply_zero.is_valid():
			print(11111111111111)
			name = apply_zero.cleaned_data['name']
			idcard = apply_zero.cleaned_data['idcard']
			phonenum = apply_zero.cleaned_data['phonenum']
			# a=UserProfile.objects.get(username=request.user)
			a = UserProfile_tem.objects.get(user=request.user.username)
			a.name=name
			a.idcard=idcard
			a.phonenum=phonenum
			a.save()
			return redirect(reverse('users:apply_1'))
		else:
			return render(request, 'users/apply.html', {
				'user_error': apply_zero
			})



def user_apply_1(request):
	if request.method=='GET':
		return render(request, 'users/apply-1.html')
	else:
		a = UserProfile_tem.objects.get(user=request.user.username)
		a.user_image = request.FILES.get('user_image','')
		print('22222222222222')
		a.save()
		if a.user_image!='':
			return redirect(reverse('users:apply_2'))
		else:
			return render(request, 'users/apply-1.html', {
				'user_error': '请上传身份证照片'
			})



def user_apply_2(request):
	if request.method=='GET':
		return render(request, 'users/apply-2.html')
	else:
		apply_two = Userapply_2_DataForm(request.POST)
		if apply_two.is_valid():


			email_code =get_code()

			email_yanzheng = apply_two.cleaned_data['email_yanzheng']
			a = UserProfile_tem.objects.get(user=request.user.username)
			a.email_yanzheng = email_yanzheng
			a.email_code = email_code
			a.time_last = datetime.now()
			a.save()
			msg = "验证码是:" + str(email_code)
			send_mail('Your Code', msg , settings.EMAIL_HOST_USER,
			          [email_yanzheng], fail_silently=False)
			return redirect(reverse('users:apply_3'))
		else:
			return render(request, 'users/apply-2.html', {
				'user_error': apply_two
			})


def user_apply_3(request):
	if request.method=='GET':
		return render(request, 'users/apply-3.html')
	else:
		code = request.POST.get('email_code', '')
		a = UserProfile_tem.objects.get(user=request.user.username)
		if a.email_code==code:
			b = UserProfile.objects.get(username=request.user.username)
			b.is_activation=True
			b.accounttype = a.accounttype
			b.name = a.name
			b.phonenum = a.phonenum
			b.idcard = a.id
			b.user_image = a.user_image
			b.email_yanzheng = a.email_yanzheng
			b.save()
			a.delete()
			return redirect(reverse('users:member'))
		else:
			return render(request, 'users/apply-3.html', {
				'user_error': '验证码错误'
			})

def code_rest(request):
	a = UserProfile_tem.objects.get(user=request.user.username)
	time_now = datetime.now()
	time_last = a.time_last
	print(time_now)
	print(time_last)
	if time_now-time_last>timedelta(seconds=60):

		email_code = get_code()
		a.email_code = email_code
		a.time_last=time_now
		a.save()
		email_yanzheng = a.email_yanzheng
		msg = "验证码是:" + str(email_code)
		send_mail('Your Code', msg, settings.EMAIL_HOST_USER,
		          [email_yanzheng], fail_silently=False)
		return render(request, 'users/apply-3.html')
	else:
		print('11111')
		return render(request, 'users/apply-3.html',{
			'user_errors': '操作频繁,请稍后再试'
		})

def owner_pro(request):
	if request.method=="GET":
		myobj = ProjectProfile.objects.filter(owner=request.user)
		myorder_list = OrderInfo.objects.filter(Q(user=request.user) & Q(is_del=False))

		time_now = datetime.now()
		return render(request, 'users/minecrowdfunding.html',{
			'myobj':myobj,
			'time_now':time_now,
			'myorder_list':myorder_list,
		})

def del_order(request,order_id):
	order = OrderInfo.objects.get(id=order_id)
	order.is_del = True
	order.save()
	return redirect(reverse('users:owner_pro'))