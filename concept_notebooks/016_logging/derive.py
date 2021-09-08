import base
import logging

# The below config wont work because the imported class Base has already been run, and it set the root logger congiguration, which cant be overridden.
# Hence, the format is also of the Base file, and also, the new log file for this file is also not created. Rather the data from this file is logged into the Base log file.
# To have own logger dedicated to base file, we need to use certain operation, by creating the specific logger for base module.
# The below root logger config will work, but here we configured the root logger. Hence, from now on, this root config will overpower the other furthur possible root config. We can create custom logger for this file also.
# ROOT LOGGER CONFIG:
# logging.basicConfig(filename='derive.log', level=logging.WARNING, format='%(asctime)s:%(levelname)s:%(message)s')

# THIS FILE LOGGER CONFIG:
logger = logging.getLogger(__name__)    # can be any hardcoded name of the log
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('derive.log')
file_handler.setLevel(logging.ERROR)    # although logger level is set to INFO, but the fileHandler logging level is set to ERROR
file_handler.setFormatter(formatter)

# streamHandler, for loggin to the terminal
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)  # since logger level is set to INFO, hence DEBUG for stream_handler will not be shown
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class Sample:
    def __init__(self, num):
        self.num = num

        logger.debug(f'The number is {self.num}.')
        logger.info(f'The number is {self.num}.')
        logger.warning(f'The number is {self.num}.')
        logger.error(f'The number is {self.num}.')
        logger.critical(f'The number is {self.num}.')
        try:
            2/0
        except:
            logger.exception('Tried dividing by Zero. Also, traceback will also be logged.')

Sample(456123)