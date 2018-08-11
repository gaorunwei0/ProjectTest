from .models import UserProfile
from django import forms
import re


class UserLoginForm(forms.Form):
	username = forms.CharField(max_length=20,min_length=4,required=True)
	password = forms.CharField(max_length=20, min_length=6, required=True)