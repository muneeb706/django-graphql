import graphene
from graphene import ObjectType
from .query_types import ClinicType, PatientType, VisitType
from patient_visits.models import Visit


class Query(ObjectType):
    clinics = graphene.List(ClinicType)
    patients = graphene.List(PatientType)
    visits_by_patient = graphene.List(VisitType, patient_name=graphene.String(required=True))
    visits_by_patient_clinic = graphene.List(VisitType,
                                             patientName=graphene.String(required=True),
                                             clinicName=graphene.String(required=True))

    def resolve_visits_by_patient(self, info, patient_name):
        return Visit.objects.get(patient__name=patient_name)


    def resolve_visits_by_patient_clinic(self, info, patientName, clinicName):
        return Visit.objects.get(patient__name=patientName, clinic_name=clinicName)