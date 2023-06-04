# Create your models here.


from django.db import models
from accounts.models import User


class Exam(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    tickets_available = models.IntegerField()

    # Add any additional fields related to exams

    def __str__(self):
        return f'{self.name} on {self.date} '


class Bookings(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='volunteer_events')
    exam_attendee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exam_attendee_events')
