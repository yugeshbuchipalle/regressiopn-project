from django.db import models
class RegisterdUser(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    phonenumber = models.CharField(blank=True,null=True,max_length=13)
    password = models.CharField(max_length=30)