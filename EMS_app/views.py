from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,UpdateView,DeleteView,View
from .models import Department, Employee, EmployeeSalary
from .forms import EmpForm,DeptForm,ESalaryForm
from django.urls import reverse_lazy
from django.db.models import Sum

# Create your views here.
# Views for Employee Details
class HomeView(TemplateView):
    template_name = 'home.html'

class EmpView(ListView):
    model = Employee
    template_name = 'emp.html'
    context_object_name = 'employees'

class AddEmp(View):
    template_name = 'add_emp.html'

    def get(self, request):
        form = EmpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EmpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employees')
        return render(request, self.template_name, {'form': form})

class EmpUpdateView(UpdateView):
    model = Employee
    template_name = 'emp_update.html' 
    context_object_name = 'employees'  
    form_class = EmpForm
    success_url = reverse_lazy('employees')  

class EmpDeleteView(DeleteView):
    model = Employee
    template_name = 'emp_delete.html'
    context_object_name = 'employees' 
    success_url = reverse_lazy('employees')

# Views for Employee Details
    
class DeptView(ListView):
    model = Department
    template_name = 'department.html'
    context_object_name = 'departments'

class AddDept(View):
    template_name = 'add_dept.html'

    def get(self, request):
        form = DeptForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = DeptForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('departments')
        return render(request, self.template_name, {'form': form})

class DeptUpdateView(UpdateView):
    model = Department
    template_name = 'update_dept.html' 
    context_object_name = 'departments'  
    form_class = DeptForm
    success_url = reverse_lazy('departments')  

class DeptDeleteView(DeleteView):
    model = Department
    template_name = 'delete_dept.html'
    context_object_name = 'departments' 
    success_url = reverse_lazy('departments')

# Views for Employee Details
    
class SalaryView(ListView):
    model = EmployeeSalary
    template_name = 'salary.html'
    context_object_name = 'salary'

class AddSalary(View):
    template_name = 'add_salary.html'

    def get(self, request):
        form = ESalaryForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ESalaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('salary')
        return render(request, self.template_name, {'form': form})

class SalaryUpdateView(UpdateView):
    model = EmployeeSalary
    template_name = 'salary_update.html' 
    context_object_name = 'salary'  
    form_class = ESalaryForm
    success_url = reverse_lazy('salary') 

class SalaryDeleteView(DeleteView):
    model = EmployeeSalary
    template_name = 'delete_salary.html'
    context_object_name = 'salary' 
    success_url = reverse_lazy('salary')

# Department Vise-Cost table view
    
def Salary_report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        department_costs = Employee.objects.filter(
            employeesalary__start_date__lte=end_date,
            employeesalary__end_date__gte=start_date
        ).values('Department__D_Name').annotate(cost=Sum('employeesalary__salary'))

        return render(request, 'salary_report.html', {'department_costs': department_costs, 'start_date': start_date, 'end_date': end_date})
    else:
        return render(request, 'salary_report.html')