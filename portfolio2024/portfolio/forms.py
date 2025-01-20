from django.forms import ModelForm
from .models import System

class Post(ModelForm):
    class Meta:
        model = System
        fields = ['system_name', 'system_summary', 'system_url', 'system_thumbnail', 'system_background']
