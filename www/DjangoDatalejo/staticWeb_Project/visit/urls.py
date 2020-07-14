from rest_framework import routers

from .views import VisitViewSet

router = routers.SimpleRouter()
router.register('visits', VisitViewSet)

urlpatterns = router.urls