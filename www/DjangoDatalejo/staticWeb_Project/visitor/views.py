from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .serializers import VisitorSerializer
from rest_framework.views import APIView
from .models import Visitor 
from visit.models import Visit
import json, datetime
from django.core.serializers.json import DjangoJSONEncoder
from functools import reduce



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
        visitors_d = Visit.objects.select_related('visitor').filter(is_active='False').filter(visitor__allowed='False').count()
        # result = json.dumps(list(visitors), cls=DjangoJSONEncoder)
        return JsonResponse({'response':visitors_d}, safe=False, status=200)

class CountVisitorPermitedView(APIView):
    def get(self, request, format=None):
        visitors_p = Visit.objects.select_related('visitor').filter(is_active='True').count()
        # result = json.dumps(list(visitors), cls=DjangoJSONEncoder)
        return JsonResponse({'response':visitors_d}, safe=False, status=200)
        
class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = (IsAuthenticated,)

class VisitorAverageAge(APIView):
    def get(self, request, format=None):
        visitors = list(Visitor.objects.filter(is_active=True).values('birthdate'))
        visitors_clean = [v['birthdate'] for v in visitors if v['birthdate'] != None]
        today = datetime.date.today()
        current_year = today.year
        current_month = today.month
        current_day = today.day
        list_years = [] 
        for date_i in visitors_clean:
            year_tmp = current_year-date_i.year
            if current_month >= date_i.month :
                if current_day < date_i.day:
                    year_tmp-=1
            else:
                year_tmp-=1
            if year_tmp > 0:
                list_years.append(year_tmp)
        promedio = reduce(lambda x, y: x + y, list_years) / len(list_years)
        return JsonResponse({'response':'%.2f'%(promedio)}, safe=False, status=200)

