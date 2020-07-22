from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .serializers import VisitorSerializer
from rest_framework.views import APIView
from .models import Visitor 
from visit.models import Visit
import json
from django.core.serializers.json import DjangoJSONEncoder



class VisitorView(APIView):
    #permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        data_insert = request.data
        # Inserta el visitante
        name_r = data_insert['name']
        read_type_r = data_insert['read_type']
        cedula_r = data_insert['cedula']
        email_r = data_insert['email']
        covid_contact_r = data_insert['covid_contact']
        birthdate_r = data_insert['birthdate']
        gender_r = data_insert['gender']
        address_r = data_insert['address']
        is_active_r = data_insert['is_active']
        visitor = Visitor.objects.create(
            name = name_r,
            read_type = read_type_r,
            cedula = cedula_r,
            email = email_r,
            covid_contact = covid_contact_r,
            birthdate = birthdate_r,
            gender = gender_r,
            address = address_r,
            is_active = is_active_r
        )

        # Inserta la visita
        data_insert_visit = data_insert['visit']
        visitor_id = visitor.id
        entry_hour_r = data_insert_visit['entry_hour']
        exit_hour_r = data_insert_visit['exit_hour']
        allowed_r = data_insert_visit['allowed']
        is_active_v_r = data_insert_visit['is_active']
        date_visit_r = data_insert_visit['date_visit']
        visit = Visit.objects.create(
            entry_hour = entry_hour_r,
            exit_hour = exit_hour_r,
            allowed = allowed_r,
            is_active = is_active_v_r,
            date_visit = date_visit_r,
            visitor_id = visitor_id
        )
        visitor.save()
        return JsonResponse({'response':'El usuario fue insertado'}, safe=False, status=201)
    
class CountVisitorView(APIView):
    def get(self, request, format=None):
        visitors = Visitor.objects.all().count()
        # result = json.dumps(list(visitors), cls=DjangoJSONEncoder)
        return JsonResponse({'response':visitors}, safe=False, status=200)

class CountVisitorDeniedView(APIView):
    def get(self, request, format=None):
        visitors_d = Visit.objects.select_related('visitor').count()
        # result = json.dumps(list(visitors), cls=DjangoJSONEncoder)
        return JsonResponse({'response':visitors_d}, safe=False, status=200)

class CountVisitorPermitedView(APIView):
    def get(self, request, format=None):
        visitors_d = Visit.objects.select_related('visitor').count()
        # result = json.dumps(list(visitors), cls=DjangoJSONEncoder)
        return JsonResponse({'response':visitors_d}, safe=False, status=200)
        


class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = (IsAuthenticated,)