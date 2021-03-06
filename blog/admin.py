from django.contrib import admin

from .models import  Article

# 引入已经定义好的数据库表
class ArticleAdmin(admin.ModelAdmin):
   list_display = ('title', 'name', 'pub_time')
   list_filter = ('pub_time',)

admin.site.register(Article,ArticleAdmin)