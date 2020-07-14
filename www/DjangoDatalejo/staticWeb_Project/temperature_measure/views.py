from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import viewsets
from .serializers import Temperature_MeasureSerializer
from .models import Temperature_Measure 

# Create your views here.
class Temperature_MeasureViewSet(viewsets.ModelViewSet):
    queryset = Temperature_Measure.objects.all()
    serializer_class = Temperature_MeasureSerializer
    permission_classes = (IsAuthenticated,)