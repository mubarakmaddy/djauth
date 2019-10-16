from django.db import models
from django.contrib.auth.models import AbstractUser

class DjUser(AbstractUser):
    auth_type = models.IntegerField(blank=True, null=True) 