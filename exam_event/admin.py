from django.contrib import admin

from .models import Exam, Bookings

# Register your models here.

admin.site.register(Exam)
admin.site.register(Bookings)
