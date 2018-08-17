from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from .models import ProjectProfile, MoneyReturnFile, FavFile
from datetime import datetime


# Create your views here.
def project(request):
	if request.method=='GET':
		allproject = ProjectProfile.objects.all()
		keywords = request.GET.get('keywords', '')
		#搜索
		if keywords:
			allproject = ProjectProfile.objects.filter(Q(name__icontains=keywords)|Q(text__icontains=keywords))
		#排序
		sort = request.GET.get('sort','')
		if sort=='add_time':
			allproject = allproject.order_by('-add_time')
		if sort=='money':
			allproject = allproject.order_by('-money')
		if sort=='favnums':
			allproject = allproject.order_by('-favnums')
		#分类
		category = request.GET.get('category','')
		if category=="1":
			allproject=allproject.filter(category=1)
		if category=="2":
			allproject=allproject.filter(category=2)
		if category=="3":
			allproject=allproject.filter(category=3)
		if category=="4":
			allproject=allproject.filter(category=4)
		#按众筹状态
		state = request.GET.get('state','')
		if state=="1":
			allproject = allproject.filter(state=1)
		if state=="2":
			allproject = allproject.filter(state=2)
		if state=="3":
			allproject = allproject.filter(state=3)

		#分页
		pagenum = int(request.GET.get('pagenum',1))
		pa = Paginator(allproject,4)
		try:
			page_list = pa.page(pagenum)
		except PageNotAnInteger:
			page_list = pa.page(1)
		except EmptyPage:
			page_list = pa.page(pa.num_pages)

		return render(request, 'project/projects.html',{
			"allproject":allproject,
			'sort':sort,
			'category':category,
			'state':state,
			'page_list':page_list,
			'keywords':keywords,
		})

# 跳转列表详情
def project_item_where(request,foo_id):
	if id:
		pro = ProjectProfile.objects.filter(id = int(foo_id))[0]
		time_now = datetime.now()
		add_time = pro.add_time
		time_last = (time_now - add_time).days
		time_last = int(pro.time) - int(time_last)

		try:
			fav = FavFile.objects.filter(pro=pro)
			is_fav = fav.get(user=request.user)
			if is_fav:
				is_fav = 1
		except:
			is_fav = 0
		# 热门产品推荐
		fav_project = ProjectProfile.objects.all().order_by('-favnums')
		fav_project_1 = fav_project[0]
		fav_project_2 = fav_project[1]

		#支持推荐
		pro_re_all = MoneyReturnFile.objects.filter(pro=pro)
		pro_re = pro_re_all[:2]



		return render(request,'project/project.html',{
			'pro_item':pro,
			'time':time_last,
			'fav_project':fav_project,
			'pro_re':pro_re,
			'pro_re_all':pro_re_all,
			'fav_project_1':fav_project_1,
			'fav_project_2':fav_project_2,
			'is_fav':is_fav,
		})



def fav(request):
	is_fav = request.GET.get('is_fav')
	pro = request.GET.get('pro_id')
	pro = ProjectProfile.objects.get(id = pro)

	if int(is_fav) != 0:
		print(111111111)
		fav = FavFile.objects.get(Q(pro=pro) & Q(user=request.user))
		fav.delete()
		pro.fav_p -=1
		pro.save()
	else:
		fav = FavFile()
		fav.pro = pro
		fav.user=request.user
		fav.save()
		pro.fav_p += 1
		pro.save()
	url = '/project/project_item/' + str(pro.id)
	return HttpResponse(url)


def start_pro(request):
	return render(request,'project/start.html')

def start_step_one(request):
	if request.method=="GET":
		return render(request,'project/start-step-1.html')
	else:
		name = request.POST.get('name','')
		if ProjectProfile.objects.filter(Q(name__icontains=name)):
			return render(request, 'project/start-step-1.html',{
				"error":'项目名已存在',
			})
		else:
			obj = ProjectProfile()
			obj.owner = request.user
			obj.category = int(request.POST.get('inlineRadioOptions','1'))
			obj.name = request.POST.get('name','')
			obj.text = request.POST.get('text','')
			obj.money = float(request.POST.get('money',5000))
			obj.time = int(request.POST.get('time','30'))
			obj.headerimage = request.FILES.get('headimage','')
			obj.helpimage = request.FILES.get('helpimage','')
			obj.usertext = request.POST.get('usertext','')
			obj.usertext_long = request.POST.get('usertextlong','')
			obj.phone = request.POST.get("phone",'')
			obj.phone_help = request.POST.get('phonehelp','')
			obj.save()

			return render(request, 'project/start-step-2.html',{
				"obj_id":obj.id
			})

def start_step_two(request):
	if request.method == 'GET':
		return render(request,'project/start-step-2.html')
	else:
		print(request.POST.get('obj_id'))
		obj = ProjectProfile.objects.get(id=request.POST.get('obj_id'))
		obj_re = MoneyReturnFile()
		obj_re.pro = obj
		obj_re.money = float(request.POST.get('money',2000))
		obj_re.re_text = request.POST.get('re_text','')
		obj_re.re_image = request.FILES.get('re_image','')
		obj_re.re_num = int(request.POST.get('re_num',0))
		obj_re.limit = request.POST.get('limit',False)
		obj_re.num_limit = int(request.POST.get('num_limit',1))
		obj_re.freight = int(request.POST.get('freight',0))
		obj_re.invoice = request.POST.get('invoice',False)
		obj_re.re_time = int(request.POST.get('re_time',30))
		obj_re.save()
		return redirect(reverse('project:start_step_three'))

def start_step_three(request):
	return render(request,'project/start-step-3.html')

def start_step_four(request):
	return render(request,'project/start-step-4.html')
