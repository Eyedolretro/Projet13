import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)





from sentry import sentry_config  # noqa: F401

from src.app.core import run_application

if __name__ == "__main__":
    print("🚀 Application Projet13 démarrée")
    run_application()

