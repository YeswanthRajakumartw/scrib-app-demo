from django.urls import path
from .views import login_view, signup_view
urlpatterns = [
    path('login/', login_view, name='user-login'),
    path('register/', signup_view, name='user-register'),

]
