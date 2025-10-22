import os
import psycopg2
import redis

def test_postgres():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST", "db_postgres"),
            port=os.getenv("POSTGRES_PORT", "5432")
        )
        print("✅ Conexión a PostgreSQL exitosa")
        conn.close()
    except Exception as e:
        print("❌ Error conectando a PostgreSQL:", e)

def test_redis():
    try:
        client = redis.Redis(
            host=os.getenv("REDIS_HOST", "cache_redis"),
            port=os.getenv("REDIS_PORT", 6379),
            db=0
        )
        client.ping()
        print("✅ Conexión a Redis exitosa")
    except Exception as e:
        print("❌ Error conectando a Redis:", e)

if __name__ == "__main__":
    test_postgres()
    test_redis()
