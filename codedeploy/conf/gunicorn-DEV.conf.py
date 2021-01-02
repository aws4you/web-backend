import os

#bind = f"127.0.0.1:{os.getenv('APP_PORT', 8001)}"

bind = f"unix:{os.environ['GUNICORN_SOCKET_PATH']}"
workers = 1
