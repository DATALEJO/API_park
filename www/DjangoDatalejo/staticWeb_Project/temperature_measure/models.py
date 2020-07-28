from django.db import models
from visit.models import Visit
import datetime

# Create your models here.
class Temperature_Measure(models.Model):
    value = models.FloatField()
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    id_file = models.CharField(max_length=250, default='0')
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now = False, auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True, null=True)
    user_register = models.IntegerField(default=0, null=True)

    class Meta:
        db_table = 'temperature_measure'