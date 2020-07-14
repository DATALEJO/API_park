from rest_framework import routers

from .views import VisitorViewSet

router = routers.SimpleRouter()
router.register('visitors', VisitorViewSet)

urlpatterns = router.urls