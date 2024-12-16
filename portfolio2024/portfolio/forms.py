from django.forms import ModelForm
from .models import System,Student

class SystemForm(ModelForm):
    class Meta:
        model = System
        
class StudentForm(ModelForm):
    class Meta:
        model = Student
