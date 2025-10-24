#!/usr/bin/env python3
"""
Script para probar conexiones a PostgreSQL y Redis
"""
import os
import sys

def test_postgres_connection():
    """Prueba la conexión a PostgreSQL"""
    try:
        import psycopg2
        
        # Variables de entorno
        db_config = {
            'host': 'localhost',
            'port': 5432,
            'database': os.getenv('POSTGRES_DB', 'main_db'),
            'user': os.getenv('POSTGRES_USER', 'devuser'),
            'password': os.getenv('POSTGRES_PASSWORD', 'devpass')
        }
        
        print("🔍 Probando conexión a PostgreSQL...")
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('SELECT version();')
        version = cursor.fetchone()
        
        print(f"✅ PostgreSQL conectado: {version[0]}")
        cursor.close()
        conn.close()
        return True
        
    except ImportError:
        print("❌ psycopg2 no instalado. Instalar con: pip install psycopg2-binary")
        return False
    except Exception as e:
        print(f"❌ Error conectando a PostgreSQL: {e}")
        return False

def test_redis_connection():
    """Prueba la conexión a Redis"""
    try:
        import redis
        
        # Variables de entorno
        redis_host = os.getenv('REDIS_HOST', 'localhost')
        redis_port = int(os.getenv('REDIS_PORT', 6379))
        
        print("🔍 Probando conexión a Redis...")
        r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
        
        # Test ping
        r.ping()
        
        # Test set/get
        r.set('test_key', 'test_value')
        value = r.get('test_key')
        
        if value == 'test_value':
            print("✅ Redis conectado y funcionando")
            r.delete('test_key')
            return True
        else:
            print("❌ Redis conectado pero no funciona correctamente")
            return False
            
    except ImportError:
        print("❌ redis no instalado. Instalar con: pip install redis")
        return False
    except Exception as e:
        print(f"❌ Error conectando a Redis: {e}")
        return False

def main():
    """Función principal"""
    print("🚀 Iniciando pruebas de conexión...\n")
    
    # Mostrar variables de entorno
    print("📋 Variables de entorno:")
    print(f"   POSTGRES_DB: {os.getenv('POSTGRES_DB', 'main_db')}")
    print(f"   POSTGRES_USER: {os.getenv('POSTGRES_USER', 'devuser')}")
    print(f"   REDIS_HOST: {os.getenv('REDIS_HOST', 'localhost')}")
    print(f"   REDIS_PORT: {os.getenv('REDIS_PORT', '6379')}\n")
    
    # Ejecutar pruebas
    postgres_ok = test_postgres_connection()
    redis_ok = test_redis_connection()
    
    print("\n📊 Resumen:")
    print(f"   PostgreSQL: {'✅' if postgres_ok else '❌'}")
    print(f"   Redis: {'✅' if redis_ok else '❌'}")
    
    if postgres_ok and redis_ok:
        print("\n🎉 ¡Todas las conexiones funcionan correctamente!")
        sys.exit(0)
    else:
        print("\n⚠️  Algunas conexiones fallaron. Revisar configuración.")
        sys.exit(1)

if __name__ == "__main__":
    main()