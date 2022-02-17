from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
with open(BASE_DIR / "config\secret_key.txt") as f:
    SECRET_KEY = f.read().strip()

ALLOWED_HOSTS = []

