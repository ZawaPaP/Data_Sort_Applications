from logging import config
import os

if not os.path.exists('./log'):
    os.makedirs('./log')
    
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s"
        }
    },
    "handlers": {
        "fileHandler": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": "./log/sort_app_application.log",
            "encoding": "utf-8"
        }
    },
    "loggers": {
        "DATA_SORT_APPLICATIONS": {
            "level": "DEBUG",
            "handlers": [
                "fileHandler"
            ],
            "propagate": False
        }
    },
}


def configure_logging():
    config.dictConfig(LOGGING)