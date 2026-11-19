from django.db import models

class Status(models.TextChoices):
        PENDING = "PENDING"
        CONFIRMED = "CONFIRMED"
        CANCELLED = "CANCELLED"

class Appointment(models.Model):
    
    
    reason = models.TextField()
    prescription = models.FileField(
    upload_to="prescriptions/", blank=True
    )
    duration_minutes = models.PositiveIntegerField(default=30)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=9, choices=Status.choices,
    default=Status.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    doctor = models.ForeignKey(
"AccountApp.Doctor", on_delete=models.CASCADE
)
patient = models.ForeignKey(
"AccountApp.Patient", on_delete=models.CASCADE
)