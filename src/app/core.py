from src.config.logger import setup_logging

logger = setup_logging()

def run_application():
    logger.info("Démarrage du cœur de l’application.")
    # Exemple de logique métier
    result = 42  # placeholder
    logger.info(f"Résultat du traitement : {result}")
    return result
