import logging
logger = logging.getLogger("python_logging.python_logging_secondary")


def some_task():
    for x in range(10):
        logger.info('Some task in a different module')