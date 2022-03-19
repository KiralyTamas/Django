from django.contrib import admin
from empapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['firstName','lastName','salary','email']

admin.site.register(Employee, EmployeeAdmin)