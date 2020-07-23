from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path('temperature-measure/last_five/', views.TemperatureLastMeasures.as_view()),
]

router = routers.SimpleRouter()
router.register('temperature-measures', views.Temperature_MeasureViewSet)

urlpatterns += router.urls