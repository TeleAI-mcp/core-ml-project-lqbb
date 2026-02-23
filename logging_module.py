"""
Logging module for the ML project.
"""
import logging

def setup_logger(name):
    """Set up a logger with the given name."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
