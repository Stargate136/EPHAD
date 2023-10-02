from django.urls import path

from .views import HomeView, AboutView, UnderConstructionView, PersonalDataAndCookiesView

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("a-propos/", AboutView.as_view(), name="about"),
    path('bientot/', UnderConstructionView.as_view(), name='under_construction'),
    path('donnees-personnelles-et-cookies/', PersonalDataAndCookiesView.as_view(), name='personal_data_and_cookies'),
]
