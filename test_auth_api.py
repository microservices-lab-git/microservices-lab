#!/usr/bin/env python3
"""
Script para probar los endpoints del microservicio de autenticación
"""
import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_register():
    """Prueba el endpoint de registro"""
    print("🔍 Probando registro de usuario...")
    
    data = {
        "email": "test@example.com",
        "password": "testpassword123",
        "password_confirm": "testpassword123",
        "first_name": "Test",
        "last_name": "User"
    }
    
    response = requests.post(f"{BASE_URL}/register/", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    
    if response.status_code == 201:
        print("✅ Registro exitoso")
        return True
    else:
        print("❌ Error en registro")
        return False

def test_login():
    """Prueba el endpoint de login"""
    print("\n🔍 Probando login...")
    
    data = {
        "email": "test@example.com",
        "password": "testpassword123"
    }
    
    response = requests.post(f"{BASE_URL}/token/", json=data)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        tokens = response.json()
        print("✅ Login exitoso")
        print(f"Access Token: {tokens['access'][:50]}...")
        print(f"Refresh Token: {tokens['refresh'][:50]}...")
        return tokens
    else:
        print("❌ Error en login")
        print(f"Response: {response.json()}")
        return None

def test_profile(access_token):
    """Prueba el endpoint de perfil"""
    print("\n🔍 Probando endpoint /me/...")
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    response = requests.get(f"{BASE_URL}/me/", headers=headers)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        print("✅ Perfil obtenido exitosamente")
        print(f"Response: {response.json()}")
        return True
    else:
        print("❌ Error obteniendo perfil")
        print(f"Response: {response.json()}")
        return False

def test_token_refresh(refresh_token):
    """Prueba el endpoint de refresh token"""
    print("\n🔍 Probando refresh token...")
    
    data = {
        "refresh": refresh_token
    }
    
    response = requests.post(f"{BASE_URL}/token/refresh/", json=data)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        new_tokens = response.json()
        print("✅ Token refresh exitoso")
        print(f"New Access Token: {new_tokens['access'][:50]}...")
        return new_tokens
    else:
        print("❌ Error en token refresh")
        print(f"Response: {response.json()}")
        return None

def main():
    """Función principal"""
    print("🚀 Iniciando pruebas del microservicio de autenticación...\n")
    
    try:
        # Probar registro
        register_success = test_register()
        
        if not register_success:
            print("⚠️ Registro falló, intentando con usuario existente...")
        
        # Probar login
        tokens = test_login()
        
        if tokens:
            # Probar perfil
            test_profile(tokens['access'])
            
            # Probar refresh token
            test_token_refresh(tokens['refresh'])
        
        print("\n📊 Resumen de pruebas completado")
        
    except requests.exceptions.ConnectionError:
        print("❌ Error de conexión. ¿Está el servicio corriendo en http://localhost:8000?")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()