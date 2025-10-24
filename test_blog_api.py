#!/usr/bin/env python3
"""
Script para probar los endpoints del microservicio de blog
"""
import requests
import json

BASE_URL = "http://localhost:8001"

def test_health_check():
    """Prueba el endpoint de health check"""
    print("🔍 Probando health check...")
    
    response = requests.get(f"{BASE_URL}/healthz/")
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        health_data = response.json()
        print("✅ Health check exitoso")
        print(f"Service: {health_data['service']}")
        print(f"Status: {health_data['status']}")
        print(f"Database: {health_data['checks']['database']}")
        print(f"Redis: {health_data['checks']['redis']}")
        return True
    else:
        print("❌ Health check falló")
        return False

def test_categories():
    """Prueba el endpoint de categorías"""
    print("\n🔍 Probando categorías...")
    
    response = requests.get(f"{BASE_URL}/api/categories/")
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Categorías obtenidas exitosamente")
        print(f"Total categorías: {data['count']}")
        
        if data['results']:
            print("Primeras categorías:")
            for cat in data['results'][:3]:
                print(f"  - {cat['name']} ({cat['slug']})")
        return True
    else:
        print("❌ Error obteniendo categorías")
        return False

def test_posts_list():
    """Prueba el endpoint de lista de posts"""
    print("\n🔍 Probando lista de posts...")
    
    response = requests.get(f"{BASE_URL}/api/posts/")
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Posts obtenidos exitosamente")
        print(f"Total posts: {data['count']}")
        print(f"Página actual: {len(data['results'])} posts")
        
        if data['results']:
            first_post = data['results'][0]
            print(f"Primer post: {first_post['title']}")
            return first_post['slug']
    else:
        print("❌ Error obteniendo posts")
        return None

def test_post_detail(slug):
    """Prueba el endpoint de detalle de post"""
    print(f"\n🔍 Probando detalle del post: {slug}")
    
    response = requests.get(f"{BASE_URL}/api/posts/{slug}/")
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        post = response.json()
        print("✅ Detalle del post obtenido exitosamente")
        print(f"Título: {post['title']}")
        print(f"Autor: {post['author']['display_name']}")
        print(f"Categoría: {post['category']['name']}")
        print(f"Views: {post['views']}")
        print(f"Contenido: {post['body'][:100]}...")
        return True
    else:
        print("❌ Error obteniendo detalle del post")
        return False

def test_search():
    """Prueba la funcionalidad de búsqueda"""
    print("\n🔍 Probando búsqueda...")
    
    search_term = "Django"
    response = requests.get(f"{BASE_URL}/api/posts/?search={search_term}")
    print(f"Status: {response.status_code}")
    print(f"Búsqueda: '{search_term}'")
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Búsqueda exitosa")
        print(f"Resultados encontrados: {data['count']}")
        
        if data['results']:
            for post in data['results'][:2]:
                print(f"  - {post['title']}")
        return True
    else:
        print("❌ Error en búsqueda")
        return False

def test_pagination():
    """Prueba la paginación"""
    print("\n🔍 Probando paginación...")
    
    response = requests.get(f"{BASE_URL}/api/posts/?page=2")
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Paginación funcionando")
        print(f"Página 2 - Posts: {len(data['results'])}")
        print(f"Siguiente página: {'Sí' if data['next'] else 'No'}")
        print(f"Página anterior: {'Sí' if data['previous'] else 'No'}")
        return True
    else:
        print("❌ Error en paginación")
        return False

def main():
    """Función principal"""
    print("🚀 Iniciando pruebas del microservicio de blog...\n")
    
    try:
        # Probar health check
        health_ok = test_health_check()
        
        if health_ok:
            # Probar categorías
            test_categories()
            
            # Probar lista de posts
            first_post_slug = test_posts_list()
            
            if first_post_slug:
                # Probar detalle de post
                test_post_detail(first_post_slug)
            
            # Probar búsqueda
            test_search()
            
            # Probar paginación
            test_pagination()
        
        print("\n📊 Resumen de pruebas completado")
        
    except requests.exceptions.ConnectionError:
        print("❌ Error de conexión. ¿Está el servicio corriendo en http://localhost:8001?")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()