from redis import Redis

rd = Redis(host="localhost", port=6379, encoding="utf-8", decode_responses=True)

print("Redis initialized")