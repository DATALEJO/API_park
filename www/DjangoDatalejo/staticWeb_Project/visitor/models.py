from django.db import models
import datetime

# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=250)
    read_type = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    covid_contact = models.BooleanField(null=True)
    birthdate = models.DateTimeField(null=True)
    gender = models.BooleanField(null=True)
    address = models.TextField(null=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now = False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True)
    user_register = models.IntegerField(default=0)