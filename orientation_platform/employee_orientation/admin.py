from django.contrib import admin
from .models.employee import Employee
from .models.project import Project
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class EmployeeAdmin(UserAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Project)
