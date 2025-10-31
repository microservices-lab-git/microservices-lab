from django.db import connection
from django.core.cache import cache
from django.http import JsonResponse


def healthz(request):
    db_ok = True
    try:
        with connection.cursor() as cur:
            cur.execute("SELECT 1")
    except Exception:
        db_ok = False
    cache_ok = True
    try:
        cache.set("healthz", "ok", timeout=10)
        cache_ok = cache.get("healthz") == "ok"
    except Exception:
        cache_ok = False
    return JsonResponse({"db": db_ok, "redis": cache_ok})