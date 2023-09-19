from django.urls import path

from .views import UnderConstructionView


app_name = "core"

urlpatterns = [
    # ... tes autres URL patterns ...
    path('coming-soon/', UnderConstructionView.as_view(), name='under_construction'),
]
