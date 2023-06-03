from django.urls import path
from .views import list_exams, create_exam, home

urlpatterns = [
    path('', home, name='home'),
    path('events/', list_exams, name='exam-list'),
    path('create-exam/', create_exam, name='create_exam'),

]
