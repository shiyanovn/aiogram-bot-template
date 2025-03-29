import os 
import logging
from .default import DefaultSettings
from dotenv import load_dotenv

load_dotenv()

def get_settings() -> DefaultSettings:
    env = os.environ.get("ENV", "local")
    if env == "local":
        return DefaultSettings()
    # ...
    # space for other settings
    # ...
    return DefaultSettings()  # fallback to default



def get_log_level():
    """Получает уровень логирования из .env или использует значение по умолчанию"""
    levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }
    return levels.get(os.getenv("LOGGING_LEVEL", "INFO").upper(), logging.INFO)
