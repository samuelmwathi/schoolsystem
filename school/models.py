from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    is_admin = models.BooleanField('Is admin', default=False)
    is_staff = models.BooleanField('Is staff', default=False)
    is_student = models.BooleanField('Is student', default=False)

class Unit(models.Model):
    name = models.CharField(max_length=50, null=True)    
    code = models.CharField(max_length=50, null=True)  

    def __str__(self):
        return self.name

class AcadYear(models.Model):
    start_date = models.DateTimeField(null=True)          
    end_date = models.DateTimeField(null=True)  

    def __str__(self):
        return self.name    

class StudyYear(models.Model):
    acad_year = models.ForeignKey(AcadYear, on_delete=models.CASCADE)  
    YEARS = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),        
    )      
    year = models.CharField(choices=YEARS, null=True, max_length=50)
    SEM = (
        ("1","1"),
        ("2","2"),
    )      
    semester = models.CharField(choices=SEM, max_length=50) 
    units = models.ManyToManyField(Unit)

class Mark(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    study_year = models.ForeignKey(StudyYear, on_delete=models.CASCADE)     
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE) 
    cat = models.IntegerField(null=True)
    exam = models.IntegerField(null=True)

class Invoice(models.Model):
    acad_year = models.ForeignKey(AcadYear, on_delete=models.CASCADE) 
    study_year = models.ForeignKey(StudyYear, on_delete=models.CASCADE) 
    amount = models.FloatField(null=True, max_length=10)

class Fee(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE) 
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE) 
    paid = models.FloatField(null=True, max_length=10)
    balance = models.FloatField(null=True, max_length=10)
       

    