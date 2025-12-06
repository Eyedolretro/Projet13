from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    SENTRY_DSN = os.getenv("SENTRY_DSN", "")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()

