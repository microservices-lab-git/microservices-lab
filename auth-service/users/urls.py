# D:\Practicas\Multi-Servicios-Capacitacion\Fundamentos-Entorno-Docker-Git\auth-service\users\urls.py

from django.urls import path # <<< IMPORT path here!
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# You might need to import your custom views from . import views

urlpatterns = [
    # Define the token endpoint here:
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # ... any other URLs for the 'users' app
]