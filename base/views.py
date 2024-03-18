from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, Role, Department
from .form import EmployeeForm, DeleteForm, ModifyForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import os.path
# Create your views here.

def login_page(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        elif Employee.objects.get(user__username=username, user__password=password):
            emp=Employee.objects.filter(user__username=username, user__password=password)
            return render(request, 'base/view.html', {'employees': emp})
        else:
            return redirect('login')
    else:
        return render(request, 'base/login_page.html')

def logout_(request):
    logout(request)
    return HttpResponse("<h1>Successfully Logged Out</h1>")

def home(request):
    return render(request, 'base/home.html')

def view(request):
    employees=Employee.objects.all()
    context={'employees': employees}
    return render(request, 'base/view.html', context)

def add(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.create(username=username, password=password)
        first_name=request.POST['first_name']
        department_name=request.POST.get('department_name')
        department_name=Department.objects.get(department_name=department_name)
        role=request.POST.get('role')
        role=Role.objects.get(role=role)
        Employee.objects.create(user=user, first_name=first_name, department_name=department_name, role=role)
        return redirect('home')

    else:
        roles=Role.objects.all()
        departments=Department.objects.all()
        return render(request, 'base/add.html', {'roles': roles, 'departments': departments})

def delete(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        department_name=request.POST['department_name']
        role=request.POST['role']
        if request.POST['last_name']:
            last_name=request.POST['last_name']
            emp=Employee.objects.get(first_name=first_name, last_name=last_name, department_name=department_name, role=role)
        else:
            emp=Employee.objects.get(first_name=first_name, department_name=department_name, role=role)
        emp.delete()
        return redirect('home')
    else:
        form =DeleteForm()
        return render(request, 'base/delete.html', {'form': form})

def filter(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        department_name=request.POST['department_name']
        role=request.POST['role']
        employees=Employee.objects.all()
        if first_name:
            employees=Employee.objects.filter(first_name__icontains=first_name)
        if last_name:
            employees=Employee.objects.filter(last_name__icontains=last_name)
        if department_name!="None":
            employees=Employee.objects.filter(department_name__department_name=department_name)
        if role!="None":
            employees=Employee.objects.filter(role__role=role)
        context={'employees':employees}
        return render(request, 'base/view.html', context)
    else:
        departments=Department.objects.all()
        roles=Role.objects.all()
        context={'departments': departments, 'roles': roles}
        return render(request, 'base/filter.html', context)
    
def modify(request, pk):
    if request.method=='POST':
        emp=Employee.objects.get(id=pk)
        emp.content=request.POST['content']
        emp.first_name=content=request.POST['first_name']
        emp.last_name=request.POST['last_name']
        emp.image=os.path.join('base/files/images/', request.POST['image'])
        emp.salary=request.POST['salary']
        emp.save()
        emp=Employee.objects.filter(id=pk)
        return render(request, 'base/view.html', {'employees': emp})
    else:
        form=ModifyForm()
        return render(request, 'base/modify.html', {'form': form})
    