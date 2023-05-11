# To inform django that its a model, we import the model from the models 

from django.db import models

class Users(models.Models):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    contact = models.BigIntegerField
    Password = models.CharField(max_length=20)