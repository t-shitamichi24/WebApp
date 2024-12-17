from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import System


# Create your views here.
class IndexView2(TemplateView):
    template_name = "index.html"


class IndexView(ListView):
    template_name = "index.html"
    model = System