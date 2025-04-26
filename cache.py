import pymysql
import redis
import json
import sys

# Redis config
redis_client = redis.Redis(
    host='test-e7umkx.serverless.aps1.cache.amazonaws.com',
    port=6379,
    ssl=True,  # Set to True for ElastiCache with TLS
    decode_responses=True,
    socket_timeout=5
)

# RDS config
RDS_HOST = 'database-1.cfukyi2mibhq.ap-south-1.rds.amazonaws.com'
RDS_USER = 'admin'
RDS_PASSWORD = 'Akash123'
RDS_DB_NAME = 'test'
TABLE_NAME = 'users'

def fetch_data_from_rds():
    try:
        connection = pymysql.connect(
            host=RDS_HOST,
            user=RDS_USER,
            password=RDS_PASSWORD,
            database=RDS_DB_NAME
        )
        print("🔗 Connected to RDS")

        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {TABLE_NAME} LIMIT 10;")
            rows = cursor.fetchall()
            return rows

    except Exception as e:
        print("❌ RDS Error:", e)
        return None

    finally:
        if 'connection' in locals():
            connection.close()

def main():
    cache_key = 'cached_table_data'
    bypass_cache = "--refresh" in sys.argv

    if not bypass_cache:
        cached_data = redis_client.get(cache_key)
        if cached_data:
            print("✅ Fetched from Redis cache:")
            print(json.loads(cached_data))
            return

    print("⚙️ No cache found or refresh requested. Fetching from RDS...")
    data = fetch_data_from_rds()
    if data:
        redis_client.set(cache_key, json.dumps(data), ex=90)
        print("📦 Cached in Redis:")
        print(data)
    else:
        print("⚠️ No data fetched from RDS.")

if __name__ == "__main__":
    main()
