# Create your models here.


from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    tickets_available = models.IntegerField()

    # Add any additional fields related to exams

    def __str__(self):
        return f'{self.name} on {self.date} '
