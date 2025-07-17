import os
import logging
import logging.config


def setup_logging(default_level: str = "INFO") -> None:
    """
    DOC-TODO: Docstring
    """

    level = os.getenv("LOG_LEVEL", default_level).upper()
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {"standard": {"format": "%(asctime)s:%(levelname)s: %(message)s"}},
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": level,
                "formatter": "standard",
                "stream": "ext://sys.stdout",
            }
        },
        "root": {"handlers": ["console"], "level": level},
    }
    logging.config.dictConfig(config)
