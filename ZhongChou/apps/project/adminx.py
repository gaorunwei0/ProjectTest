from .models import ProjectProfile,MoneyReturnFile
import xadmin

class ProjectProfileAdmin(object):
    list_display = ['name','money','time']

    class MoneyReturnFileInline(object):
        model = MoneyReturnFile
        exclude = ["add_time"]
        extra = 1
        style = 'tab'
    inlines = [MoneyReturnFileInline]

xadmin.site.register(ProjectProfile,ProjectProfileAdmin)