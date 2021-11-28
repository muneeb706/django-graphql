from django.db import models


class Clinic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=100)


class Purpose(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,
                            choices=(("appointment", "appointment"),
                                     ("treatment", "treatment")),
                            unique=True)


class Visit(models.Model):
    id = models.AutoField(primary_key=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    purpose = models.ForeignKey(Purpose, null=True, on_delete=models.SET_NULL)
