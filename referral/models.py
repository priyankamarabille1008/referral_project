from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    referral_code=models.CharField(max_length=10, null=True, blank=True)

    
