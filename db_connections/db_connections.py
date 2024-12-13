import os
import sys
from sqlalchemy import create_engine
from loggers.logger_setup import LoggerSetup


class DataScientists:

    logger_setup = LoggerSetup()
    DB_URI = os.getenv('')

    def __init__(self):
        try:
            self.engine = create_engine(self.DB_URI)
        except Exception as err:
            message = f"Failed to connect to DB: {err}"
            self.logger_setup.logger.critical(message)
            sys.exit(1)

    def __enter__(self):
        return self
