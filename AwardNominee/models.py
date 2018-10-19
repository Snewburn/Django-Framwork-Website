from django.db import models


class AwardNominee(models.Model):
    Name = models.CharField(max_length=200, default="empty")
    Description = models.CharField(max_length=200, default="empty")
    Image_name = models.CharField(max_length=200, default="empty")
    Num_Votes = models.CharField(max_length=200, default="empty")
