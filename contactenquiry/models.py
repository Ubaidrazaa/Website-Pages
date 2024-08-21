from django.db import models

# Create your models here.
class contactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    websitename=models.CharField(max_length=70)
    message=models.TextField()