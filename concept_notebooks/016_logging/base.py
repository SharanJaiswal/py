import logging

# logging.basicConfig(filename='base0.log', level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# adding formatting to the filehandler, not the logger
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('base0.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Employee:
    def __init__(self, name):
        self.name = name

        logger.info(f'Name is {self.name}.')

Employee('sharan')