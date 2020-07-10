from django.db import models
from visitor.models import Visitor

# Create your models here.
class Visit(models.Model):
    entry_hour = models.TimeField()
    exit_hour = models.TimeField()
    allowed = models.BooleanField()
    is_active = models.BooleanField()
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now = False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True)
    user_resgister = models.IntegerField(default=0)