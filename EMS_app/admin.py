from django.contrib import admin
from .models import Department,Employee,EmployeeSalary

# Register your models here.

# @admin.register(Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     list_display = ('D_Name', 'Floor')
#     search_fields = ('name',)

# @admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('First_Name','Last_Name', 'Email', 'Designation', 'Department', 'Reporting_manager')
    search_fields = ('First_Name', 'Email')
    list_filter = ('Designation', 'Department')

# @admin.register(EmployeeSalary)
# class EmployeeSalaryAdmin(admin.ModelAdmin):
#     list_display = ('employee', 'salary', 'start_date', 'end_date')
#     search_fields = ('employee__name',)
#     list_filter = ('employee__Department',)


class EmployeeInline(admin.StackedInline):
    model = Employee
    extra = 1

class DepartmentAdmin(admin.ModelAdmin):
    inlines = [EmployeeInline]

class EmployeeSalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'salary', 'start_date', 'end_date')
    list_filter = ('employee__Department', 'start_date', 'end_date')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeSalary, EmployeeSalaryAdmin)