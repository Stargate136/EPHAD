from django.urls import path

from .views import IndexView, CVDetailView

app_name = "cv"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>/', CVDetailView.as_view(), name='detail'),
]