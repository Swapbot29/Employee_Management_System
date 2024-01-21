from django.urls import path
from .views import HomeView,EmpView,EmpUpdateView,EmpDeleteView,AddEmp,DeptView,DeptUpdateView,DeptDeleteView,AddDept,SalaryView,SalaryUpdateView,SalaryDeleteView,AddSalary,Salary_report

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('employees/', EmpView.as_view(), name='employees'),
    path('add-emp/', AddEmp.as_view(), name='add_emp'),
    path('emp-update/<int:pk>/',EmpUpdateView.as_view(), name='emp_update'),
    path('emp_delete/<int:pk>/', EmpDeleteView.as_view(), name='emp_delete'),
    path('department/', DeptView.as_view(), name='departments'),
    path('add-dept/', AddDept.as_view(), name='add_dept'),
    path('dept-update/<int:pk>/',DeptUpdateView.as_view(), name='dept_update'),
    path('dept_delete/<int:pk>/', DeptDeleteView.as_view(), name='dept_delete'),
    path('salary/', SalaryView.as_view(), name='salary'),
    path('add-salary/', AddSalary.as_view(), name='add_salary'),
    path('salary-update/<int:pk>/',SalaryUpdateView.as_view(), name='salary_update'),
    path('salary_delete/<int:pk>/', SalaryDeleteView.as_view(), name='salary_delete'),
    path('salary_report/', Salary_report, name='salary-report'),
]
