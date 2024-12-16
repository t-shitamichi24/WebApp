from django.contrib import admin
from .models import Student,System

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_no","username")
    list_display_links = ("student_no","username")
admin.site.register(Student,StudentAdmin)

class SystemAdmin(admin.ModelAdmin):
    list_display = ("student","system_name")
    list_display_links = ("student","system_name")
admin.site.register(System,SystemAdmin)