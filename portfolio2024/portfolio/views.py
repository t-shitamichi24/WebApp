from django.shortcuts import render
from django.views.generic import ListView,DetailView, UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import System
from .forms import Post

# Create your views here.
class IndexView(ListView):
    template_name = "index.html"
    model = System

class DetailView(DetailView):
    template_name = "detail.html"
    model = System

@method_decorator(login_required, name='dispatch')
class PostView(UpdateView):
    model = System
    form_class = Post
    template_name = "post.html"

    success_url = reverse_lazy('portfolio:index')
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)