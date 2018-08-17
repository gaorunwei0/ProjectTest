"""ZhongChou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import user_login, user_reg, user_logout, user_member, user_accttype, user_apply, user_apply_1, \
	user_apply_2, user_apply_3, code_rest, owner_pro, del_order

# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
	url(r'^reg/',user_reg,name='reg'),
	url(r'^login/',user_login,name='login'),
	url(r'^logout/',user_logout,name='logout'),
	url(r'^member/',user_member,name='member'),
	url(r'^accttype/',user_accttype,name='accttype'),
	url(r'^apply/$',user_apply,name='apply'),
	url(r'^apply_1/$',user_apply_1,name='apply_1'),
	url(r'^apply_2/$',user_apply_2,name='apply_2'),
	url(r'^apply_3/$',user_apply_3,name='apply_3'),
	url(r'^code_rest/$',code_rest,name='code_rest'),
	url(r'^owner_pro/$',owner_pro,name='owner_pro'),
	url(r'^del_order/(\d+)$',del_order,name='del_order'),
]
