from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100,null=True)
    designation=models.CharField(max_length=100,null=True)
    department=models.CharField(max_length=100,null=True)

    def __str__(self):
       return self.name
  
class Family(models.Model):
    f_name = models.CharField(max_length=100,null=True)
    relationship=models.CharField(max_length=100,null=True)
    f_designation=models.CharField(max_length=100,null=True)
    def __str__(self):
       return self.f_name


class FamilyMember(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=100,null=True)
    relationship=models.CharField(max_length=100,null=True)
    f_designation=models.CharField(max_length=100,null=True)
    def __str__(self):
       return self.f_name       