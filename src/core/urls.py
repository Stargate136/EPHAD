from django.urls import path

from .views import HomeView, AboutView, UnderConstructionView

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("a-propos/", AboutView.as_view(), name="about"),
    path('coming-soon/', UnderConstructionView.as_view(), name='under_construction'),
]
