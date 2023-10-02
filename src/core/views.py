from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'core/home.html'


class AboutView(TemplateView):
    template_name = 'core/about.html'


class UnderConstructionView(TemplateView):
    template_name = 'core/under_construction.html'


class PrivacyPolicyView(TemplateView):
    template_name = "core/privacy_policy.html"
