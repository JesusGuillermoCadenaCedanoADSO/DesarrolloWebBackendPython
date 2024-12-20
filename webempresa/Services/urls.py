from django.urls import path
from Services import views as service_views

urlpatterns = [
    path('', service_views.servicio, name="services"),
]

