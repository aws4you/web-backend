import os

#bind = f"127.0.0.1:{os.getenv('APP_PORT', 8001)}"

bind = f"unix:/tmp/web-backend-{os.getenv('DJANGO_ENV', 'NONE')}.sock"
workers = 1
