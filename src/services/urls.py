from django.urls import path

from .views import ServicesIndex, ShortStayView, DayCareView, EmergencyReceptionView, PermanentStayView


app_name = "services"

urlpatterns = [
    path("", ServicesIndex.as_view(), name="index"),
    path("court-sejour/", ShortStayView.as_view(), name="short_stay"),
    path("accueil-de-jour", DayCareView.as_view(), name="day_care"),
    path("accueil-en-situation-d-urgence", EmergencyReceptionView.as_view(), name="emergency_reception"),
    path("sejour-permanent", PermanentStayView.as_view(), name="permanent_stay"),
]
