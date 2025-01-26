from django.forms import ModelForm
from .models import System

class Post(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = System
        fields = ['system_name', 'system_summary', 'system_url', 'system_thumbnail', 'system_background']
