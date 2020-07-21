from django.urls import path
from rest_framework import routers
from . import views as viewsVisitors
from .views import VisitorViewSet

urlpatterns = [
    path('visitor/create/', viewsVisitors.VisitorView.as_view())
]

router = routers.SimpleRouter()
router.register('visitors', VisitorViewSet)

urlpatterns += router.urls