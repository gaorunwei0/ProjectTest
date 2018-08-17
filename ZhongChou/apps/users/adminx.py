from .models import UserProfile,UserProfile_tem
import xadmin

class UserProfile_temAdmin(object):
    list_display = ['user','phonenum']


xadmin.site.register(UserProfile_tem,UserProfile_temAdmin)