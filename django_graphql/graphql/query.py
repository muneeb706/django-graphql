import graphene
from graphene import ObjectType
from .query_types import ClinicType, PatientType, VisitType
from patient_visits.models import Visit, Clinic, Patient


class Query(ObjectType):
    clinics = graphene.List(ClinicType)
    patients = graphene.List(PatientType)
    visits_by_patient = graphene.List(VisitType,
                            patient_name=graphene.String(required=True))
    visits_by_patient_clinic = graphene.List(VisitType,
                                    patient_name=graphene.String(required=True),
                                    clinic_name=graphene.String(required=True))

    def resolve_clinics(self, info):
        return Clinic.objects.all()

    def resolve_patients(self, info):
        return Patient.objects.all()

    def resolve_visits_by_patient(self, info, patient_name):
        return Visit.objects.filter(patient__name=patient_name)

    def resolve_visits_by_patient_clinic(self, info, patient_name, clinic_name):
        return Visit.objects.filter(patient__name=patient_name,
                                    clinic__name=clinic_name)
