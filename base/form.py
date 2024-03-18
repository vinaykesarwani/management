from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

class DeleteForm(ModelForm):
    class Meta:
        model=Employee
        fields=['first_name', 'last_name', 'department_name', 'role']

class ModifyForm(ModelForm):
    class Meta:
        model=Employee
        fields=['first_name', 'last_name', 'content', 'image', 'salary']