from django.db import models

# Create your models here.


class Member(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(null=True, max_length=50)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
