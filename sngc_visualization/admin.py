from django.contrib import admin
from .models import AppLogs,User
# Register your models here.


class AppLogsAdmin(admin.ModelAdmin):
        list_display = ('app_name', 'first_timestamp', 'total_foreground_time')
admin.site.register(AppLogs, AppLogsAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'unique_id')
admin.site.register(User, UserAdmin)