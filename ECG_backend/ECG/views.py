from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from ECG.models import Patient, Report
from ECG.serializers import ReportSerializer
from django.conf import settings
import telegram
import requests

# Create your views here.

# telegram_settings = settings.TELEGRAM
# bot = telegram.Bot(token=telegram_settings['bot_token'])
API_KEY = "5181733554:AAFDEJlQpcZWVGDjvX28NTelwqSgVeNEB9U"

class GetPatientReport(viewsets.ModelViewSet):
    def post(self, request):
        data = request.data
        patient_number = data.pop('patient_number')
        patient = Patient.objects.get(patient_number= patient_number)
        data['patient'] = patient.pk
        serializer = ReportSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if data['alarm']:
            CHAT_NAME = patient.sectionTelegramId
            out = "check patient number: " + str(patient.patient_number)
            url = "https://api.telegram.org/bot"+API_KEY+"/sendMessage?chat_id=@"+CHAT_NAME+"&text=" + out
            requests.get(url)
                

        return Response({"status" : "OK"})
