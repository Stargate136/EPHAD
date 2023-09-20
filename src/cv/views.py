from django.views.generic import ListView, DetailView

from .models import CV


# Create your views here.
class IndexView(ListView):
    model = CV
    template_name = "cv/index.html"
    context_object_name = "cvs"


class CVDetailView(DetailView):
    model = CV
    template_name = 'cv/detail.html'
    context_object_name = 'cv'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'