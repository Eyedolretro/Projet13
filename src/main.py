from sentry.sentry_config import *
import logging

print("Application démarrée 🚀")

# Exemple de log normal
logging.info("Ceci est un log d’information.")

# Exemple de log d’erreur envoyé automatiquement à Sentry
logging.error("Ceci est une erreur envoyée à Sentry.")

# Exemple d’exception non gérée (sera aussi envoyée à Sentry)
raise Exception("Erreur de test automatique pour Sentry")
