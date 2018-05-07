from django.contrib import admin
from .models import Alert
# # Register your models here.
#
#
class AlertAdmin(admin.ModelAdmin):
#     ordering = ('-last_timestamp',)
    list_display = ('label', 'timestamp')
admin.site.register(Alert, AlertAdmin)
#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('device_id', 'unique_id')
# admin.site.register(User, UserAdmin)