from django.db import models

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=99)
    email = models.CharField(max_length=99)
    phone_number = models.CharField(max_length=99)
    specialization = models.CharField(max_length=99)

    def __str__(self):
        return self.name
    
class Patient(models.Model):
    patients_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=99)
    email = models.CharField(max_length=99)
    phone_number = models.CharField(max_length=99)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    app_date = models.DateField()
    status = models.CharField(max_length=99)

    def __str__(self):
        return f"Appt: {self.patient.name} with {self.doctor.name}"

        
