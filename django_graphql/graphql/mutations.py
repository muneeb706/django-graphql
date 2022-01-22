import graphene
from graphene import Mutation, ObjectType

from patient_visits.models import Clinic, Patient, Visit, Purpose
from .mutation_inputs import ClinicInput, PatientInput, VisitInput, UpdateVisitInput, DeleteVisitInput, \
    UpdateVisitInput
from .query_types import ClinicType, PatientType, VisitType


class AddClinic(Mutation):
    class Arguments:
        input = ClinicInput(required=True)

    clinic = graphene.Field(ClinicType)

    def mutate(self, info, input):
        new_clinic = Clinic.objects.create(**input)
        return AddClinic(clinic=new_clinic)


class AddPatient(Mutation):
    class Arguments:
        input = PatientInput(required=True)

    patient = graphene.Field(PatientType)

    def mutate(self, info, input):
        new_patient = Patient.objects.create(**input)
        return AddPatient(patient=new_patient)


class AddVisit(Mutation):
    class Arguments:
        input = VisitInput(required=True)

    visit = graphene.Field(VisitType)

    def mutate(self, info, input):
        new_visit = Visit.objects.create(
            clinic=Clinic.objects.get(name=input.clinic_name),
            patient=Patient.objects.get(name=input.patient_name),
            purpose=Purpose.objects.get(name=input.purpose))
        return AddVisit(visit=new_visit)


class UpdateVisitPurpose(Mutation):
    class Arguments:
        input = UpdateVisitInput(required=True)

    visit = graphene.Field(VisitType)

    def mutate(self, info, input):
        updated_visit = Visit.objects.get(id=input.id)
        updated_visit.purpose = Purpose.objects.get(
                                    name=input.purpose)
        updated_visit.save()
        return UpdateVisitPurpose(updated_visit)


class DeleteVisit(Mutation):
    class Arguments:
        input = DeleteVisitInput(required=True)

    message = graphene.String()

    def mutate(self, info, input):
        deleted_visit = Visit.objects.get(id=input.id)
        deleted_visit.delete()
        return DeleteVisit("Visit deleted successfully.")


class Mutation(ObjectType):
    add_clinic = AddClinic.Field()
    add_patient = AddPatient.Field()
    add_visit = AddVisit.Field()
    update_visit_purpose = UpdateVisitPurpose.Field()
    delete_visit = DeleteVisit.Field()
