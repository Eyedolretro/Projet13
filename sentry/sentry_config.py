import os
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
from dotenv import load_dotenv
import logging

# Charger les variables depuis .env
load_dotenv()

# Intégration pour capturer les logs Python
logging_integration = LoggingIntegration(
    level=logging.INFO,        # Capture les logs info et plus
    event_level=logging.ERROR  # Envoie à Sentry les logs d’erreur et plus
)

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    environment=os.getenv("ENVIRONMENT", "development"),
    integrations=[logging_integration],
    traces_sample_rate=1.0,  # pour capture des performances si besoin
)

print("✅ Sentry initialisé avec capture des exceptions et logs.")
