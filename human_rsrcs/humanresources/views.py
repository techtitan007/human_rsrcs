from django.shortcuts import render

from .models import Department, Employee

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'human_rsrcs/department_list.html', {'departments': departments})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'human_rsrcs/employee_list.html', {'employees': employees})

        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'human_rsrcs/create_department.html', {'form': form})

def update_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

from django.contrib.auth.decorators import login_required

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'humanrsrcs/employee_list.html', {'employees': employees})

from django.shortcuts import render, redirect, get_object_or_404
from .forms import DepartmentForm, EmployeeForm
from .models import Department, Employee

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

from django.contrib.auth.decorators import login_required

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'human_rsrcs/employee_list.html', {'employees': employees})

from django.shortcuts import render, redirect, get_object_or_404
from .forms import DepartmentForm, EmployeeForm
from .models import Department, Employee

def create_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'human_rsrcs/create_department.html', {'form': form})

def update_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'human_rsrcs/update_department.html', {'form': form, 'department': department})

def delete_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    department.delete()
    return redirect('department_list')

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'human_rsrcs/create_employee.html', {'form': form})

def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'human_rsrcs/update_employee.html', {'form': form, 'employee': employee})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect('employee_list')
