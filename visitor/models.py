from django.db import models

# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=250)
    read_type = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    covid_contact = models.BooleanField()
    birthdate = models.DateTimeField()
    gender = models.BooleanField()
    address = models.TextField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now = False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True)
    user_resgister = models.IntegerField(default=0)