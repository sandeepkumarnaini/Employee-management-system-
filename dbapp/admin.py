from django.contrib import admin
from . models import Employee,Department,employeedup

class employeeadmin(admin.ModelAdmin):
    list_display=[field.name for field in Employee._meta.fields]+['grade']
    list_filter=['empname','empsal']
    list_editable=['empname']
    def grade(self,obj):
        
        if obj.empsal>299:
            return 'A'
        elif obj.empsal>199:
            return 'B'
        else:
            return 'C'

# Register your models here.
admin.site.register(Employee,employeeadmin)
admin.site.register(Department)
admin.site.register(employeedup)