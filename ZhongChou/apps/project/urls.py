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
import xadmin
from project.views import project, project_item_where, start_pro, start_step_one, start_step_two, start_step_three, \
	start_step_four, fav
from users.views import index


# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
	url(r'^project/',project,name='project'),
	url(r'^project_item/(\d+)',project_item_where,name='project_item'),
	url(r'^start_pro/',start_pro,name='start_pro'),
	url(r'^start_step_one/',start_step_one,name='start_step_one'),
	url(r'^start_step_two/',start_step_two,name='start_step_two'),
	url(r'^start_step_three/',start_step_three,name='start_step_three'),
	url(r'^start_step_four/',start_step_four,name='start_step_four'),
	url(r'^fav/',fav,name='fav'),

]
