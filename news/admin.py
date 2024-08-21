from django.contrib import admin
from news.models import News
# Register your models here.
class newsAdmin(admin.ModelAdmin):
    list_display=('news_title','news_desc','news_image')
admin.site.register(News,newsAdmin)    