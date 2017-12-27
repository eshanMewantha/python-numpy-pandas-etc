import logging.config
import os

import python_logging_secondary

logger = logging.getLogger("python_logging")
path = os.getcwd()
handler = logging.FileHandler(path + '/some.log')
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# 'application' code
logger.info('starting the main module')

python_logging_secondary.some_task()

logger.critical('Terminating !')