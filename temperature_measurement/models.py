from django.db import models
from visit.models import Visit

# Create your models here.
class TemperatureMeasurement(models.Model):
    value = models.FloatField()
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now = False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True)
    user_resgister = models.IntegerField(default=0)