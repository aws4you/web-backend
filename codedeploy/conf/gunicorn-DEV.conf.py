import os

bind = f"127.0.0.1:{os.getenv('APP_PORT', 8001)}"
workers = 1
