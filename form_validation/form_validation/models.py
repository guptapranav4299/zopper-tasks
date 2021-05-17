from django.db import models

class UserModel(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=128)
    re_password = models.CharField(max_length=128)


    
