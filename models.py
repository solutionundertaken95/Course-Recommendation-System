from django.db import models


class userregistartion(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
