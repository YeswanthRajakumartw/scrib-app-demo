from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_volunteer = models.BooleanField(default=False)
    is_physically_challenged_user = models.BooleanField(default=False)
    availability = models.BooleanField(default=False)



