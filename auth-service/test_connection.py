import os
import psycopg2
import redis

DB_HOST = os.getenv('DB_HOST', 'postgres')
DB_NAME = os.getenv('DB_NAME', 'main_db')
DB_USER = os.getenv('DB_USER', 'devuser')
DB_PASS = os.getenv('DB_PASS', 'devpass')
DB_PORT = int(os.getenv('DB_PORT', '5432'))

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = int(os.getenv('REDIS_PORT', '6379'))


def test_postgres():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT,
    )
    cur = conn.cursor()
    cur.execute('SELECT 1;')
    result = cur.fetchone()
    print('PostgreSQL OK:', result[0] == 1)
    cur.close()
    conn.close()


def test_redis():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    pong = r.ping()
    print('Redis OK:', pong)


if __name__ == '__main__':
    test_postgres()
    test_redis()