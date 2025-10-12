# logger_config.py

import logging
from datetime import datetime

def setup_logging():
    """Konfigurerar loggningen med ett dynamiskt filnamn."""
    log_filename = f"monitoring_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Logging configured successfully.")
