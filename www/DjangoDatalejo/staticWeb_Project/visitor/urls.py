from django.urls import path
from rest_framework import routers
from . import views as viewsVisitors
from .views import VisitorViewSet

urlpatterns = [
    path('visitor/create/', viewsVisitors.VisitorView.as_view()),
    path('visitor/total/', viewsVisitors.CountVisitorView.as_view()),
    path('visitor/denied/', viewsVisitors.CountVisitorDeniedView.as_view()),
    path('visitor/permited/', viewsVisitors.CountVisitorPermitedView.as_view()),
    path('visitor/avg_age/', viewsVisitors.VisitorAverageAge.as_view()),
]

router = routers.SimpleRouter()
router.register('visitors', VisitorViewSet)

urlpatterns += router.urls