import uuid
from django.db import models

# Create your models here.
class AppLogs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1)
    app_name = models.CharField(max_length=100)
    first_timestamp = models.DateTimeField(null=True, default=None)#install
    last_timestamp = models.DateTimeField(null=True, default=None)
    last_time_used = models.DateTimeField(null=True, default=None)
    total_foreground_time = models.DateTimeField()
    created_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1)
    device_id = models.CharField(unique=True, max_length=100)
    unique_id = models.CharField(max_length=32)

class InternetLogs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1)
    url = models.CharField(max_length=40, default=None)
    logs = models.CharField(max_length=40, default=None)
    added_on = models.DateTimeField(auto_now=True)