import os
import django
from django.db import connections
from django.db.utils import OperationalError

# Configura las settings de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auth_service.settings')
django.setup()

def test_db_connection():
    db_conn = connections['default']
    try:
        db_conn.cursor()
        print("Conexión a la base de datos exitosa!")
    except OperationalError as e:
        print(f"Error al conectar a la base de datos: {e}")

if __name__ == '__main__':
    test_db_connection()