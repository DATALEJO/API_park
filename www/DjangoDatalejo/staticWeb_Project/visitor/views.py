from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .serializers import VisitorSerializer
from rest_framework.views import APIView
from .models import Visitor 
from visit.models import Visit
from temperature_measure.models import Temperature_Measure
import json, datetime, pytz
from datetime import date
from django.core.serializers.json import DjangoJSONEncoder
from functools import reduce



class VisitorView(APIView):
    permission_classes = (IsAuthenticated,)
    #today = date.today().strftime("%d/%m/%Y")
    
    def post(self, request, format=None):
        data_insert = request.data
        # Inserta el visitante
        data_insert_visitor = data_insert['visitor']
        name_r = data_insert_visitor['name']
        read_type_r = data_insert_visitor['read_type']
        cedula_r = data_insert_visitor['cedula']
        email_r = data_insert_visitor['email']
        covid_contact_r = data_insert_visitor['covid_contact']
        birthdate_r = data_insert_visitor['birthdate']
        gender_r = data_insert_visitor['gender']
        address_r = data_insert_visitor['address']
        visitor = Visitor.objects.create(
            name = name_r,
            read_type = read_type_r,
            cedula = cedula_r,
            email = email_r,
            covid_contact = covid_contact_r,
            birthdate = birthdate_r,
            gender = gender_r,
            address = address_r,
            is_active = True
        )
        visitor.save()
        tz = pytz.timezone('America/Bogota')
        now = datetime.datetime.now(tz=tz)
        date_now = now.strftime("%Y-%m-%d %H:%M:%S")
        hour_now = now.strftime("%H:%M:%S")
        #Inserta la visita
        data_insert_visit = data_insert['visit']
        visitor_id = visitor.id
        entry_hour_r = hour_now
        exit_hour_r = hour_now
        allowed_r = data_insert_visit['allowed']
        visit = Visit.objects.create(
            entry_hour = entry_hour_r,
            exit_hour = exit_hour_r,
            allowed = allowed_r,
            is_active = True,
            date_visit = date_now,
            visitor_id = visitor_id
        )
        visit.save()
        #Inserta la temperatura
        visit_id = visit.id
        data_insert_t_measure = data_insert['temperature_measure']
        tempereature_measure = Temperature_Measure.objects.create(
            value = data_insert_t_measure['value'],
            is_active = True,
            visit_id = visit_id,
            id_file = data_insert_t_measure['id_file']
        )
        tempereature_measure.save()
        return JsonResponse({'response':'La información fue registrada'}, safe=False, status=201)
        # return JsonResponse({'now':date_now}, safe=False, status=201)
    
class CountVisitorView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        visitors = Visitor.objects.all().count()
        # result = json.dumps(list(visitors), cls=DjangoJSONEncoder)
        return JsonResponse({'response':visitors}, safe=False, status=200)

class CountVisitorDeniedView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        visitors_d = Visit.objects.select_related('visitor').filter(is_active='False').count()
        # result = json.dumps(list(visitors), cls=DjangoJSONEncoder)
        return JsonResponse({'response':visitors_d}, safe=False, status=200)

class CountVisitorPermitedView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        visitors_p = Visit.objects.select_related('visitor').filter(is_active='True').count()
        # result = json.dumps(list(visitors), cls=DjangoJSONEncoder)
        return JsonResponse({'response':visitors_p}, safe=False, status=200)
        
class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = (IsAuthenticated,)

class VisitorAverageAge(APIView):
    permission_classes = (IsAuthenticated,)
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

