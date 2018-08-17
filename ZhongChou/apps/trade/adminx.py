from .models import OrderInfo
import xadmin

class OrderProfileAdmin(object):
    list_display = ['order_sn','user','order_mount']



xadmin.site.register(OrderInfo,OrderProfileAdmin)