
from django.urls import path
from .views import home
from anomaly import views

urlpatterns = [
    path('', views.home, name='home'),
    path('download/', views.download_csv, name='download_csv'),
]