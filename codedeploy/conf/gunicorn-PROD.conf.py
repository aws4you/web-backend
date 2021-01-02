import multiprocessing
import os

bind = f"127.0.0.1:{os.getenv('APP_PORT', 8000)}"
workers = multiprocessing.cpu_count() * 2 + 1
