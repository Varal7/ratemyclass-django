from django.contrib import admin
from rate.models import Course, Department, Year, Period, Type, Student, Assessment

# Register your models here.
admin.site.register(Department)
admin.site.register(Year)
admin.site.register(Type)
admin.site.register(Period)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Assessment)
