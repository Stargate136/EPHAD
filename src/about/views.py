from django.views.generic import ListView
from .models import Section


class AboutView(ListView):
    model = Section
    template_name = 'about/about.html'
    context_object_name = 'sections'
    ordering = ['display_order']