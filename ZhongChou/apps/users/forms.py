from .models import UserProfile
from django import forms
import re


class UserLoginForm(forms.Form):
	username = forms.CharField(max_length=20,min_length=4,required=True,error_messages={
		'required': '用户名必须填写',
        'min_length':'用户名至少4位',
        'max_length': '用户名最长20位',
	})
	password = forms.CharField(max_length=20, min_length=6, required=True ,error_messages={
		'required': '密码必须填写',
		'min_length': '密码最少得6个',
		'max_length': '密码最多20个',
	})


class UserRegForm(forms.Form):
	password = forms.CharField(max_length=20, min_length=6, required=True,error_messages={
		'required': '密码必须填写',
        'min_length':'密码最少得6个',
        'max_length': '密码最多20个',
	})
	username = forms.CharField(max_length=20, min_length=4, required=True, error_messages={
		'required': '用户名必须填写',
		'min_length': '用户名最少得4个',
		'max_length': '用户名最多20个',
	})
	email = forms.EmailField(required=True, error_messages={
		'required': '邮箱必须填写'
	})

class UserapplyDataForm(forms.Form):
	user_data = forms.CharField(max_length=10, min_length=1, required=True)
	name = forms.CharField(error_messages={'required':'真实姓名必须填写'})
	idcard = forms.CharField(error_messages={'required':'身份证必须填写'})
	phonenum = forms.IntegerField(error_messages={'required':'手机号必须填写'})