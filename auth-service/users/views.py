# D:\Practicas\Multi-Servicios-Capacitacion\Fundamentos-Entorno-Docker-Git\auth-service\users\views.py
# D:\Practicas\Multi-Servicios-Capacitacion\Fundamentos-Entorno-Docker-Git\auth-service\users\views.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# Remove the path(...) line here. Keep only your view logic.
# This line is the problem:
path('api/token/', TokenObtainPairView.as_view()), 
# ... other views
path('api/token/refresh/', TokenRefreshView.as_view()),
