import graphene
from graphene import InputObjectType


class ClinicInput(InputObjectType):
    name = graphene.String(required=True)
    city = graphene.String(required=True)
    state = graphene.String(required=True)


class PatientInput(InputObjectType):
    name = graphene.String(required=True)
    phone = graphene.String(required=True)


class VisitInput(InputObjectType):
    clinic_name = graphene.String(required=True)
    patient_name = graphene.String(required=True)
    purpose = graphene.String(required=True)


class UpdateVisitInput(InputObjectType):
    id = graphene.ID(required=True)
    purpose = graphene.String(required=True)


class DeleteVisitInput(InputObjectType):
    id = graphene.ID(required=True)
