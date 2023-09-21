from django.urls import path

from .views import HomeView, AboutView, UnderConstructionView, PrivacyPolicyView

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("a-propos/", AboutView.as_view(), name="about"),
    path('bientot/', UnderConstructionView.as_view(), name='under_construction'),
    path('politique-de-confidentialite/', PrivacyPolicyView.as_view(), name='privacy_policygit'),
]
