from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from . import views

urlpatterns = [
    # Autenticación JWT
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # Gestión de usuarios
    path('register/', views.register_user, name='register'),
    path('me/', views.get_user_profile, name='user_profile'),
    path('me/update/', views.update_user_profile, name='update_profile'),
]