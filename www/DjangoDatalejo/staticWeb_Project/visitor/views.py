from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import viewsets
from .serializers import VisitorSerializer
from .models import Visitor 

# Create your views here.
class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = (IsAuthenticated,)