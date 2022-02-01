from ECG.views import GetPatientReport
from django.urls import path

urlpatterns = [
    path('report/', GetPatientReport.as_view({"post":"post"}), name='report')
]