from graphene_django import DjangoObjectType
from patient_visits.models import Clinic, Patient, Visit, Purpose


class ClinicType(DjangoObjectType):
    class Meta:
        model = Clinic
        fields = ("name", "city", "state")


class PatientType(DjangoObjectType):
    class Meta:
        model = Patient
        fields = ("name", "phone")


class PurposeType(DjangoObjectType):
    class Meta:
        model = Purpose
        fields = ("name",)


class VisitType(DjangoObjectType):
    class Meta:
        model = Visit
        fields = ("clinic", "patient", "purpose")
