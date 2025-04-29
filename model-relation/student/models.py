from django.db import models

# Create your models here.

class Aadhar(models.Model):
    aadhar=models.IntegerField()
    createdby=models.CharField(max_length=100)
    data=models.IntegerField()
    
class Citizen(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    contact=models.IntegerField()
    aadharno=models.OneToOneField(Aadhar,on_delete=models.PROTECT,to_field='aadhar',related_name='student')
    
    def __str__(self):
        