from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import Temperature_MeasureSerializer
from .models import Temperature_Measure 

# Create your views here.
class Temperature_MeasureViewSet(viewsets.ModelViewSet):
    queryset = Temperature_Measure.objects.all()
    serializer_class = Temperature_MeasureSerializer
    permission_classes = (IsAuthenticated,)

class TemperatureLastMeasures(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        temp_measures = list(Temperature_Measure.objects.filter(is_active=True).order_by('-id')[:5].values())
        # result = json.dumps(list(visitors), cls=DjangoJSONEncoder)
        list_temp = [lt['value'] for lt in temp_measures]
        if len(list_temp) < 5:
            l_list = 5 - len(list_temp)
            listofzeroz = [0]*l_list
            list_temp+=listofzeroz
        return JsonResponse({'response':list_temp}, safe=False, status=200)