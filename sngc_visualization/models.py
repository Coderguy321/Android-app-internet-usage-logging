import uuid
from django.db import models

# class User(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid1)
#     device_id = models.CharField(unique=True, max_length=100, null=True)
#     unique_id = models.CharField(max_length=32)

class Alert(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1)
    label = models.CharField(max_length=100)
    timestamp = models.DateTimeField(null=True, default=None)#install
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

class XAlert(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1)
    label = models.CharField(max_length=100)
    timestamp = models.DateTimeField(null=True, default=None)#install
    # user = models.ForeignKey(User, on_delete=models.CASCADE)