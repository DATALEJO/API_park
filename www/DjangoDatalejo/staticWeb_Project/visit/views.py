from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import viewsets
from .serializers import VisitSerializer
from .models import Visit 

# Create your views here.
class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = (IsAuthenticated,)