from django.db import models

# Create your models here.

class Department(models.Model):
    Floors = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4')
    ]
    D_Name = models.CharField(max_length=50)
    Floor = models.CharField(max_length=1,choices=Floors, blank=False)

    def __str__(self):
        return self.D_Name

class Employee(models.Model):
    Designations = [
        ('Associate', 'Associate'),
        ('TL', 'Team Lead'),
        ('Manager', 'Manager'),
    ]
    First_Name = models.CharField(max_length=100, null=True)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Address = models.TextField()
    Designation = models.CharField(max_length=20,choices=Designations)
    Reporting_manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"
    
class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def save(self, *args, **kwargs):
        if self.end_date is not None:
            overlaps = EmployeeSalary.objects.filter(
                employee=self.employee,
                end_date__gt=self.start_date,
                start_date__lt=self.end_date,
            ).exclude(pk=self.pk)
            for entry in overlaps:
                entry.end_date = self.start_date
                entry.save()

        super().save(*args, **kwargs)

    def __str__(self):
       return f"{self.employee.First_Name} - {self.salary} ({self.start_date} to {self.end_date})"