from django.db import models

# Create your models here.
class Users(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    mobile_no=models.CharField(max_length=11)
    email=models.EmailField()
    dob=models.DateField()
    role=models.CharField(max_length=25)
    property_name=models.CharField(max_length=255)
    property_management_company=models.CharField(max_length=255)