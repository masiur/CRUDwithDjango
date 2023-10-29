from django.db import models

# Create your models here.

# // create a model of Employee with name, email, age, salary, designation
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    salary = models.IntegerField()
    designation = models.CharField(max_length=100)
    
class Student(models.Model):  
    first_name = models.CharField(max_length=20)  
    last_name  = models.CharField(max_length=30)  
    contact    = models.IntegerField()  
    email      = models.EmailField(max_length=50)  
    age        = models.IntegerField()  