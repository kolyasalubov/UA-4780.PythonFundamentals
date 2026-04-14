import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DATA_DIR = BASE_DIR / "instance"


def _env_flag(name, default=False):
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


class DemoConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "archery-club-dev-key")
    DEBUG = _env_flag("FLASK_DEBUG", default=True)
    TESTING = False
    AUTO_SEED_ON_STARTUP = _env_flag("AUTO_SEED_ON_STARTUP", default=True)
    DATA_DIR = PROJECT_DATA_DIR
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{PROJECT_DATA_DIR / 'archery_club.db'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(DemoConfig):
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
    DEBUG = False
    TESTING = False
    AUTO_SEED_ON_STARTUP = False
