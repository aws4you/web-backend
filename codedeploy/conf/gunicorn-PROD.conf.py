import multiprocessing
import os

#bind = f"127.0.0.1:{os.getenv('APP_PORT', 8000)}"
bind = f"unix:{os.environ['GUNICORN_SOCKET_PATH']}"

#workers = multiprocessing.cpu_count() * 2 + 1

# since we are not in "real" we use only one CPU
workers = 1
