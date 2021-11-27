import graphene
from graphene import Mutation, ObjectType

from patient_visits.models import Clinic, Patient, Visit, Purpose
from .mutation_types import ClinicInput, PatientInput, VisitInput
from .query_types import ClinicType, PatientType, VisitType


class AddClinic(Mutation):
    class Arguments:
        input = ClinicInput(required=True)

    clinic = graphene.Field(ClinicType)

    def mutate(self, info, input=None):
        new_clinic = Clinic.objects.create(**input)
        return AddClinic(clinic=new_clinic)


class AddPatient(Mutation):
    class Arguments:
        input = PatientInput(required=True)

    patient = graphene.Field(PatientType)

    def mutate(self, info, input=None):
        new_patient = Patient.objects.create(**input)
        return AddPatient(patient=new_patient)


class AddVisit(Mutation):
    class Arguments:
        input = VisitInput(required=True)

    visit = graphene.Field(VisitType)

    def mutate(self, info, input=None):
        new_visit = Visit.objects.create(clinic=Clinic.objects.get(name=input.clinic_name),
                                         patient=Patient.objects.get(name=input.patient_name),
                                         purpose=Purpose.objects.get(input.purpose))
        return AddVisit(visit=new_visit)


class UpdateVisitPurpose(Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        purpose = graphene.String(required=True)

    visit = graphene.Field(VisitType)

    def mutate(self, info, id, purpose):
        updated_visit = Visit.objects.get(id=id)
        updated_visit.save(purpose=Purpose.objects.get(name=purpose))


class DeleteVisit(Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    message = graphene.String()

    def mutate(self, info, id):
        deleted_visit = Visit.objects.get(id=id)
        deleted_visit.delete()


class Mutation(ObjectType):
    add_clinic = AddClinic.Field()
    add_patient = AddPatient.Field()
    add_visit = AddVisit.Field()
