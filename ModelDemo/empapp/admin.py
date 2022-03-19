from django.contrib import admin
from empapp.models import Employee

'''Ezzel a Class-el lehet beállítani, hogy az Admin felületen, mikor az Employee menüben vagyunk,
milyen lista alapján jelenítse meg az Employee tagokna ka listáját.'''
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['firstName','lastName','salary','email']

admin.site.register(Employee, EmployeeAdmin)