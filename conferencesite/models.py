from django.db import models


class Workshop(models.Model):
    Name = models.CharField(max_length=200, default="empty")
    Session = models.CharField(max_length=200, default="empty")
    Room_Number = models.CharField(max_length=200, default="empty")
    Start_Time = models.TimeField()
    End_Time = models.TimeField()
