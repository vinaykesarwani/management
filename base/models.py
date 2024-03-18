from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
    department_name=models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.department_name
    
class Role(models.Model):
    role=models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.role

class Employee(models.Model):
    user=models.ForeignKey(User, on_delete=CASCADE)
    image=models.ImageField(upload_to='base/files/images', null=True, blank=True)
    first_name=models.CharField(max_length=20, null=False, blank=False)
    last_name=models.CharField(max_length=20, null=True, blank=True)
    department_name=models.ForeignKey(Department, on_delete=CASCADE)
    role=models.ForeignKey(Role, on_delete=CASCADE)
    salary=models.IntegerField(null=True, blank=True)
    hired_at=models.DateTimeField(auto_now_add=True)
    content=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name