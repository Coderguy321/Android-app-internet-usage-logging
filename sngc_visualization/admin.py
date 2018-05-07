# from django.contrib import admin
# from .models import AppLogs,User
# # Register your models here.
#
#
# class AppLogsAdmin(admin.ModelAdmin):
#     ordering = ('-last_timestamp',)
#     list_display = ('app_name', 'first_timestamp','last_timestamp', 'total_foreground_time','username')
#     def username(self, obj):
#         return obj.user.unique_id
# admin.site.register(AppLogs, AppLogsAdmin)
#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('device_id', 'unique_id')
# admin.site.register(User, UserAdmin)