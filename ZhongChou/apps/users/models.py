from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):

	ACCOUNT_TYPE = (
		(1,'商业公司'),
		(2,'个体工商户'),
		(3,'个人经营'),
		(4,'政府及非营利组织')
	)

	is_activation = models.BooleanField(default=False,verbose_name="是否认证")
	is_activation_sure = models.BooleanField(default=False,verbose_name="是否通过审核")
	accounttype = models.IntegerField(choices=ACCOUNT_TYPE,default=3,verbose_name='账户类型')
	name = models.CharField(max_length=30, verbose_name='真实姓名',blank=True,null=True)
	phonenum = models.CharField(max_length=11,verbose_name='手机号',blank=True,null=True)
	idcard = models.CharField(max_length=18,verbose_name='身份证',blank=True,null=True)
	user_image = models.ImageField(max_length=200, upload_to='user_image', verbose_name='身份证照片', blank=True, null=True)
	email_yanzheng = models.CharField(max_length=50, verbose_name='验证邮箱', blank=True, null=True)
	add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

	class Meta:
		verbose_name = '用户信息'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.username

class UserProfile_tem(models.Model):

	ACCOUNT_TYPE = (
		(1,'商业公司'),
		(2,'个体工商户'),
		(3,'个人经营'),
		(4,'政府及非营利组织')
	)

	user = models.CharField(max_length=20,verbose_name='用户名')
	accounttype = models.IntegerField(choices=ACCOUNT_TYPE,default=3,verbose_name='账户类型')
	name = models.CharField(max_length=30, verbose_name='真实姓名',blank=True,null=True)
	phonenum = models.CharField(max_length=11,verbose_name='手机号',blank=True,null=True)
	idcard = models.CharField(max_length=18,verbose_name='身份证',blank=True,null=True)
	user_image = models.ImageField(max_length=200,upload_to='user_image',verbose_name='身份证照片',blank=True,null=True)
	email_yanzheng = models.CharField(max_length=50,verbose_name='验证邮箱',blank=True,null=True)
	email_code = models.CharField(max_length=4,verbose_name='验证码',blank=True,null=True)
	time_last = models.DateTimeField(verbose_name='重新发送时间',default=datetime.now)
	add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

	class Meta:
		verbose_name = '临时信息'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.user