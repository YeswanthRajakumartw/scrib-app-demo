from django.urls import path
from .views import list_exams, create_exam, home, list_scrib, book_scribe

urlpatterns = [path('', home, name='home'), path('events/', list_exams, name='exam-list'),
               path('create-exam/', create_exam, name='create_exam'),
               path('scrib-list/<str:exam_id>', list_scrib, name='scribe-list'),
               path('book-scrib/<str:exam_id>/<str:volunteer_id>', book_scribe, name='book-scribe'),

               ]
