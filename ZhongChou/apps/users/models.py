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

	name = models.CharField(max_length=30, verbose_name='姓名',blank=True,null=True)
	is_activation = models.BooleanField(default=False,verbose_name="是否认证")
	accounttype = models.IntegerField(choices=ACCOUNT_TYPE,default=3,verbose_name='账户类型')
	phonenum = models.IntegerField(verbose_name='手机号',blank=True,null=True)
	idcard = models.CharField(max_length=18,verbose_name='身份证',blank=True,null=True)
	add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

	class Meta:
		verbose_name = '用户信息'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.username