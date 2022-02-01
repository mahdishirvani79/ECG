from rest_framework import serializers
from ECG.models import Report, Patient, Doctor
from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model =Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    Doctor = PresentablePrimaryKeyRelatedField(
        queryset=Doctor.objects.all(),
        presentation_serializer=DoctorSerializer,
        read_source=None,
        required = False
    )

    class Meta:
        model = Patient
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    Patient = PresentablePrimaryKeyRelatedField(
        queryset=Patient.objects.all(),
        presentation_serializer=PatientSerializer,
        read_source=None,
        required = False
    )

    class Meta:
        model = Report
        fields = '__all__'

