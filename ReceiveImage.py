import redis  # pip install redis
import io
import base64

ip = "34.130.168.47"
r = redis.Redis(host=ip, port=6379, db=0, password="sofe4630u")

value = r.get("image")
if value is None:
    print("Failed to get image from redis")
    exit(1)

value = value.decode("utf-8")
decoded_value = base64.b64decode(value)

with open("./received.jpg", "wb") as f:
    f.write(decoded_value)

print("Image received, check ./received.jpg")
