import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS = [os.path.join(BASE_DIR, "templates")]

SECRET_KEY = "super secret"