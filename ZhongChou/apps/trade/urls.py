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
from django.conf.urls import url,include

from trade.views import pay_1, pay_2, order_set, return_ali

# from django.contrib import admin

urlpatterns = [

	url(r'^pay_1/(\d+)',pay_1,name='pay_1'),
	url(r'^pay_2/(\d+)',pay_2,name='pay_2'),
	url(r'^order_set/',order_set,name='order_set'),
	url(r'^return/',return_ali,name='return_ali'),

]
