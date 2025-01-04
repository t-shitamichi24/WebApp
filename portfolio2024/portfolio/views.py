from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import System


# Create your views here.
class IndexView(ListView):
    template_name = "index.html"
    model = System

class DetailView(DetailView):
    template_name = "detail.html"
    model = System