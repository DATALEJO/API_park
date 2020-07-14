from rest_framework import routers

from .views import Temperature_MeasureViewSet

router = routers.SimpleRouter()
router.register('temperature-measures', Temperature_MeasureViewSet)

urlpatterns = router.urls