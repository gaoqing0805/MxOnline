# _*_ encoding:utf-8 _*_

from django.contrib import admin

# Register your models here.

from .models import UserProfile


# 为model添加管理器
# class UserProfileAdmin(admin.ModelAdmin):
#     pass


# 关联管理器和model,
# admin.site.register(UserProfile, UserProfileAdmin)