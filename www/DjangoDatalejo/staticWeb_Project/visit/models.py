from django.db import models
from visitor.models import Visitor

# Create your models here.
class Visit(models.Model):
    date_visit = models.DateTimeField(auto_now = False, auto_now_add=True, blank=True, null=True)
    entry_hour = models.TimeField()
    exit_hour = models.TimeField(null=True)
    allowed = models.BooleanField()
    is_active = models.BooleanField()
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now = False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True)
    user_register = models.IntegerField(default=0, null=True)