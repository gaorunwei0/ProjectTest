from urllib.parse import urlparse, parse_qs
from django.http import HttpResponse, JsonResponse
from ZhongChou.settings import private_key_path, ali_public_path
from project.models import MoneyReturnFile, ProjectProfile
from trade.models import UserAddress, OrderInfo
from  datetime import datetime
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

# Create your views here.
from utils import alipay
from utils.alipay import AliPay


def pay_1(request,pro_id):
	re_pro = MoneyReturnFile.objects.get(id = pro_id)
	return render(request,'trade/pay-step-1.html',{
		're_pro':re_pro,
	})

def pay_2(request,pro_id):
	if request.method=='POST':
		name = request.POST.get('name','')
		address = request.POST.get('address','')
		number = request.POST.get('number','')
		if name and address and number:
			a = UserAddress()
			a.user = request.user
			a.signer_name = name
			a.signer_mobile = number
			a.address = address
			a.save()
			add_all = UserAddress.objects.filter(user=request.user).order_by('add_time')
			if len(add_all) > 2:
				add_all[0].delete()

		re_pro = MoneyReturnFile.objects.get(id=pro_id)
		num = request.POST.get('num')
		money_all = float(num)*float(re_pro.money) + float(re_pro.freight)
		try:
			add_all = UserAddress.objects.filter(user=request.user).order_by('add_time')
		except:
			add_all = ''
		return render(request, 'trade/pay-step-2.html',{
			're_pro': re_pro,
			'num':num,
			'money_all':money_all,
			'add_all':add_all
		})




def order_set(request):

	address_id = request.GET.get('address')
	invoice = request.GET.get('invoice')
	invoice_text = request.GET.get('invoice_text','')
	order_mount = request.GET.get('order_mount')
	post_script = request.GET.get('post_script')
	return_info_id = request.GET.get('return_info_id')
	return_num = request.GET.get('return_num',1)
	add_info = UserAddress.objects.get(id=address_id)
	return_info = MoneyReturnFile.objects.get(id = return_info_id)

	dt = datetime.now().strftime("%Y%m%d%H%M%S")
	order_sn = dt + str(return_info.id)

	order_info = OrderInfo()
	order_info.user = request.user

	order_info.return_info = return_info
	order_info.order_sn = order_sn
	order_info.order_mount = float(order_mount)
	order_info.post_script = post_script
	order_info.invoice = int(invoice)
	order_info.invoice_text = invoice_text
	order_info.signer_name = add_info.signer_name
	order_info.signer_mobile = add_info.signer_mobile
	order_info.address = add_info.address
	order_info.return_num = return_num
	order_info.save()

	pro = return_info.pro
	pro.money_now += order_info.order_mount
	pro.save()


	alipay = AliPay(
		appid="2016091800542427",
		app_notify_url="http://127.0.0.1:8000/trade/return/",
		app_private_key_path=private_key_path,
		alipay_public_key_path=ali_public_path,
		debug=True,
		return_url="http://127.0.0.1:8000/trade/return/"
	)

	url = alipay.direct_pay(
		subject=return_info.pro.name,
		out_trade_no=order_sn,
		total_amount=order_mount
	)

	re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)

	return HttpResponse(re_url)

def return_ali(request):
	order_sn = request.GET.get('out_trade_no')
	trade_no = request.GET.get('trade_no')
	pay_status = request.GET.get("pay_status", "TRADE_SUCCESS")
	order = OrderInfo.objects.get(order_sn=order_sn)
	order.pay_status = pay_status
	order.trade_no = trade_no
	order.save()
	return redirect(reverse("users:owner_pro"))

