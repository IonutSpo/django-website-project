from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


id_regex = RegexValidator(r"^[0-9]{13}$")

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    personal_number = models.IntegerField(validators=[id_regex])
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
