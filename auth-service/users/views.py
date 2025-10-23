from django.contrib.auth import get_user_model
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RegisterView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({"detail": "email y password son obligatorios"}, status=status.HTTP_400_BAD_REQUEST)
        User = get_user_model()
        try:
            user = User.objects.create_user(email=email, password=password)
        except IntegrityError:
            return Response({"detail": "email ya existe"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"id": user.id, "email": user.email}, status=status.HTTP_201_CREATED)
