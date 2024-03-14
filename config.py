import os
from dotenv import load_dotenv

flask_env = os.getenv("FLASK_ENV", "development")

dotenv_path = ".env.production" if flask_env == "production" else ".env.development"
load_dotenv(dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
EMAIL_SMTP_HOST = os.getenv("EMAIL_SMTP_HOST")
EMAIL_SMTP_PORT = os.getenv("EMAIL_SMTP_PORT")
EMAIL_HTTP_HOST = os.getenv("EMAIL_HTTP_HOST")
EMAIL_HTTP_PORT = os.getenv("EMAIL_HTTP_PORT")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

print(f"Using {dotenv_path}")
