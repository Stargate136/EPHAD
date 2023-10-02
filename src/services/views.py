# Create your views here.
from django.views.generic import TemplateView


class ServicesIndex(TemplateView):
    template_name = "services/index.html"


class ShortStayView(TemplateView):
    template_name = "services/short_stay.html"


class DayCareView(TemplateView):
    template_name = "services/day_care.html"


class PermanentStayView(TemplateView):
    template_name = "services/permanent_stay.html"


class EmergencyReceptionView(TemplateView):
    template_name = "services/emergency_reception.html"
