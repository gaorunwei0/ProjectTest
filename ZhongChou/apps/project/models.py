from datetime import datetime,timedelta

from django.db import models
from users.models import UserProfile

# Create your models here.

class ProjectProfile(models.Model):
	CATEGORY_TYPE = (
		(1,'科技'),
		(2,'设计'),
		(3,'公益'),
		(4,'农业'),
	)
	STATE_TYPE = (
		(1,'即将开始'),
		(2,'众筹中'),
		(3,'众筹成功'),
	)
	category = models.IntegerField(choices=CATEGORY_TYPE,default=1,verbose_name='分类')
	state = models.IntegerField(choices=STATE_TYPE,default=1,verbose_name='众筹状态')
	name = models.CharField(max_length=50,verbose_name='项目名称',blank=True,null=True)
	text = models.CharField(max_length=100,verbose_name='项目简介',blank=True,null=True)
	money = models.FloatField(default=0.0, verbose_name='筹资金额',blank=True,null=True)
	time = models.IntegerField(default=1,verbose_name="筹资天数",blank=True,null=True)
	headerimage = models.ImageField(upload_to='header_image',verbose_name="项目头图",blank=True,null=True)
	helpimage = models.ImageField(upload_to='help_image',verbose_name="项目详情",blank=True,null=True)
	favnums = models.IntegerField(verbose_name='支持人数',default=0)
	money_now = models.FloatField(default=0,verbose_name='当前金额')
	fav_p = models.IntegerField(verbose_name='关注人数',default=0)
	return_category = models.IntegerField(choices=((1,'实物回报'),(2,'虚拟物品回报')),verbose_name='回报类型',default=1)

	owner = models.ForeignKey(UserProfile,verbose_name='项目发起人',blank=True,null=True)
	usertext = models.CharField(max_length=40,verbose_name='自我介绍',blank=True,null=True)
	usertext_long = models.CharField(max_length=400,verbose_name='详细介绍',blank=True,null=True)
	phone = models.CharField(max_length=11,verbose_name="联系电话",blank=True,null=True)
	phone_help = models.CharField(max_length=11,verbose_name="客服电话",blank=True,null=True)

	add_level = models.IntegerField(default=0,verbose_name='广告级别')

	add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

	def get_time(self):
		time_r = (datetime.now()-self.add_time).days
		time_r = int(self.time) - int(time_r)
		return time_r

	def get_data(self):
		day = self.time
		data = self.add_time + timedelta(days=day)
		return data

	def get_num100(self):
		num = self.money_now / self.money *100
		return num


	class Meta:
		ordering = ['-name']
		verbose_name = '项目信息'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name

class MoneyReturnFile(models.Model):
	pro = models.ForeignKey(ProjectProfile,verbose_name='所属项目')
	money = models.FloatField(verbose_name='支付金额',default=0.0)
	re_text = models.CharField(max_length=200,verbose_name='回报内容',blank=True,null=True)
	re_image = models.ImageField(upload_to='re_image',verbose_name='说明图片')
	re_num = models.IntegerField(default=0,verbose_name='回报数量')
	limit = models.BooleanField(default=False,verbose_name='是否限购')
	num_limit = models.IntegerField(default=1,verbose_name='单笔限购')
	freight = models.IntegerField(default=0,verbose_name='运费')
	invoice = models.BooleanField(default=False,verbose_name='是否可开发票')
	re_time = models.IntegerField(default=10,verbose_name='回报时间')
	fav_num = models.IntegerField(default=0,verbose_name='支持人数')

	class Meta:
		verbose_name = '项目回报信息'
		verbose_name_plural = verbose_name

	def __str__(self):
		return str(self.money)

class FavFile(models.Model):
	pro = models.ForeignKey(ProjectProfile,verbose_name='关注项目')
	user = models.ForeignKey(UserProfile,verbose_name='关注者')

	class Meta:
		verbose_name = '关注'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.pro