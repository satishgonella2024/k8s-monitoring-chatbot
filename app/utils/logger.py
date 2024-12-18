# app/utils/logger.py

import logging

def setup_logger():
    """
    Set up a logger with predefined settings.
    """
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    return logging.getLogger(__name__)
