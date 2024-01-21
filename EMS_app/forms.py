from django import forms
from .models import Employee,Department,EmployeeSalary

class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
    
class DeptForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class ESalaryForm(forms.ModelForm):
    class Meta:
        model = EmployeeSalary
        fields = '__all__'