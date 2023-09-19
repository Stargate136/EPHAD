from django.views.generic import TemplateView


class UnderConstructionView(TemplateView):
    template_name = 'core/under_construction.html'
