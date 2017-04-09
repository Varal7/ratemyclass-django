from django.contrib import admin
from rate.models import Class, Department, Year, Period, Type

# Register your models here.
admin.site.register(Department)
admin.site.register(Year)
admin.site.register(Type)
admin.site.register(Period)
admin.site.register(Class)

