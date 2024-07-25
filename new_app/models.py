from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    course=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=10)
    message=models.CharField(max_length=500)

    class Meta:
        db_table='contact_db'