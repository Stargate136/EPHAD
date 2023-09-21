from django.views.generic import TemplateView, ListView

from .models import Section


class HomeView(ListView):
    model = Section
    template_name = 'core/home.html'
    context_object_name = 'sections'

    def get_queryset(self):
        return self.model.objects.filter(page="HOME").order_by("display_order")


class AboutView(ListView):
    model = Section
    template_name = 'core/about.html'
    context_object_name = 'sections'

    def get_queryset(self):
        return self.model.objects.filter(page="ABOUT").order_by("display_order")


class UnderConstructionView(TemplateView):
    template_name = 'core/under_construction.html'


class PrivacyPolicyView(TemplateView):
    template_name = "core/privacy_policy.html"
