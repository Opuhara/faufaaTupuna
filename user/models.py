from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
	bio = models.TextField(max_length=500, blank=True, null=True)
	birth_date = models.DateField(null=True, blank=True)
