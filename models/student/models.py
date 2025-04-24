from django.db import models

#Create your models here.

class BaseField(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=250)
    contact=models.IntegerField()
    class Meta:
        abstract=True
        
class Student(BaseField):
 
    course=models.CharField(max_length=70)
    roll_no=models.IntegerField()
    
class Employee(BaseField):

    department=models.CharField(max_length=70)
    emp_id=models.IntegerField()
    salary=models.IntegerField()
    def __str__(self):
        return self.department
    
class Client(BaseField):

    project=models.CharField(max_length=70)
    billing_status=models.CharField(max_length=70)
    





    
    
    
    
    