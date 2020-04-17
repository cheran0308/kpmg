from django.db import models
from django.utils.timezone import now

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    dob = models.CharField(max_length=255)
    status = models.CharField(max_length=10)
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.name

class Workflow(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    approver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approver')
    status = models.CharField(max_length=10, default='created') #created, recheck, rejected, approved
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.name

class WFLog(models.Model):
    wf_id = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    activity = models.CharField(max_length=50)
    remark = models.CharField(max_length=200)
    date = models.DateTimeField(default=now, editable=False)