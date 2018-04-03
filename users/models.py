from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    #define a name field for user,rather than a Firstname and Lastname
    name=models.CharField(blank=True,max_length=255)
    #retrun the email in string
    def __str__(self):
        return self.email
