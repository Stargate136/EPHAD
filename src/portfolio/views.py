from django.views.generic import ListView, DetailView

from .models import Project


class IndexView(ListView):
    model = Project
    template_name = 'portfolio/index.html'
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/detail.html"
    context_object_name = "project"
    slug_url_kwarg = 'slug'
