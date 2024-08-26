from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
 """
  Stores or adds information about an therapy appointment enquiry.
 """

patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        )

diagnosis = models.CharField(
        max_length=500
        )

created_on = models.DateTimeField(
        auto_now_add=True
    )

edited_on = models.DateTimeField(
        auto_now=True
    )

class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointmentss"
        ordering = ["-created_on"]

def __str__(self):
        return f"Appointment request of {self.patient} with {self.diagnosis}"    