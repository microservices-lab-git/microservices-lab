#!/usr/bin/env python3
"""
Script para probar conexiones a PostgreSQL y Redis
"""
import os
import sys

def test_mysql_connection():
    """Prueba la conexión a MySQL"""
    try:
        import mysql.connector
        
        # Variables de entorno
        db_config = {
            'host': 'localhost',
            'port': 3307,
            'database': os.getenv('MYSQL_DATABASE', 'main_db'),
            'user': os.getenv('MYSQL_USER', 'devuser'),
            'password': os.getenv('MYSQL_PASSWORD', 'devpass')
        }
        
        print("🔍 Probando conexión a MySQL...")
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('SELECT VERSION();')
        version = cursor.fetchone()
        
        print(f"✅ MySQL conectado: {version[0]}")
        cursor.close()
        conn.close()
        return True
        
    except ImportError:
        print("❌ mysql-connector-python no instalado. Instalar con: pip install mysql-connector-python")
        return False
    except Exception as e:
        print(f"❌ Error conectando a MySQL: {e}")
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
    print(f"   MYSQL_DATABASE: {os.getenv('MYSQL_DATABASE', 'main_db')}")
    print(f"   MYSQL_USER: {os.getenv('MYSQL_USER', 'devuser')}")
    print(f"   REDIS_HOST: {os.getenv('REDIS_HOST', 'localhost')}")
    print(f"   REDIS_PORT: {os.getenv('REDIS_PORT', '6379')}\n")
    
    # Ejecutar pruebas
    mysql_ok = test_mysql_connection()
    redis_ok = test_redis_connection()
    
    print("\n📊 Resumen:")
    print(f"   MySQL: {'✅' if mysql_ok else '❌'}")
    print(f"   Redis: {'✅' if redis_ok else '❌'}")
    
    if mysql_ok and redis_ok:
        print("\n🎉 ¡Todas las conexiones funcionan correctamente!")
        sys.exit(0)
    else:
        print("\n⚠️  Algunas conexiones fallaron. Revisar configuración.")
        sys.exit(1)

if __name__ == "__main__":
    main()