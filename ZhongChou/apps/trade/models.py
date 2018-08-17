from datetime import datetime

from django.db import models
from project.models import MoneyReturnFile
from users.models import UserProfile


# Create your models here.

class OrderInfo(models.Model):
	PAY_STATUS = (
		('PAYING', '待支付'),
		('TRADE_SUCCESS', '支付成功'),
		('FAIL', '支付失败')
	)
	user = models.ForeignKey(UserProfile, verbose_name='用户')
	return_info = models.ForeignKey(MoneyReturnFile, verbose_name='回报信息')
	order_sn = models.CharField(max_length=50, unique=True, verbose_name='订单号', null=True, blank=True)
	trade_no = models.CharField(max_length=100, unique=True, verbose_name='交易号', null=True, blank=True)
	order_mount = models.FloatField(default=0.0, verbose_name='交易总金额')
	pay_status = models.CharField(default='PAYING', choices=PAY_STATUS, verbose_name='订单状态', max_length=20)
	pay_time = models.DateTimeField(verbose_name='支付时间', null=True, blank=True)
	post_script = models.CharField(max_length=200, verbose_name='订单留言', blank=True, null=True)
	invoice = models.IntegerField(choices=((1,'无需发票'),(2,'需要发票')),default=1,verbose_name='是否打印发票')
	invoice_text = models.CharField(max_length=50,verbose_name='发票信息',blank=True,null=True)
	signer_name = models.CharField(max_length=20, verbose_name='签收人')
	signer_mobile = models.CharField(max_length=11, verbose_name='签收电话')
	address = models.CharField(max_length=200, verbose_name='签收地址')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
	return_num = models.IntegerField(default=1,verbose_name='回报数量')
	is_del = models.BooleanField(default=False,verbose_name='是否被删除')

	class Meta:
		verbose_name = '订单'
		verbose_name_plural = verbose_name
	def __str__(self):
		return str(self.order_sn)



class UserAddress(models.Model):
	user = models.ForeignKey(UserProfile, verbose_name="用户")
	address = models.CharField(max_length=200, verbose_name="地址")
	signer_name = models.CharField(max_length=30, verbose_name="签收人")
	signer_mobile = models.CharField(max_length=11, verbose_name="联系电话")
	add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

	class Meta:
		verbose_name = "收货地址"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.address
