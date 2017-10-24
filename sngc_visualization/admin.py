from django.contrib import admin
from .models import AppLogs
# Register your models here.


class AppLogsAdmin(admin.ModelAdmin):
        list_display = ('app_name', 'first_timestamp', 'total_foreground_time')
admin.site.register(AppLogs, AppLogsAdmin)