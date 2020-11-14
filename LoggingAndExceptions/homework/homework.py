import logging.handlers


class Error(Exception):
    pass


class TooManyVisitors(Error):
    pass


class TooFewVisitors(Error):
    pass


class Concert:
    MAX_VISITORS = 200
    MIN_VISITOR = 10

    # add 2 class attributes - max_visitors (200) and min_visitors (10)
    def __init__(self, visitors_num):
        self.visitors_num = visitors_num
        if self.visitors_num > Concert.MAX_VISITORS:
            raise TooManyVisitors
        elif self.visitors_num < Concert.MIN_VISITOR:
            raise TooFewVisitors

        # """
        # if visitors num is bigger than max_visitors - raise TooManyVisitors error
        # if visitors num is less than min_visitors - raise TooFewVisitors error
        # """


# created Concert instance
# ins_consert = Concert(9)


def make_concert(visitors_num):
    try:
        Concert(visitors_num)
    except TooFewVisitors as err:
        log_message(err, 30)
        return False
    except TooManyVisitors as error:
        log_message(error, 20)
        return False
    else:
        return True


# print(make_concert(ins_consert.visitors_num))


# """
# create Concert instance - handle TooManyVisitors and TooFewVisitors errors here:
# in case if caught - log error to console and return False, in case of successful initialization - return True
# """

# create Logger object
logger = logging.getLogger(__name__)
# set level to debug
logger.setLevel(logging.INFO)

logger_handler = logging.FileHandler('test.log')
logger_handler.setLevel(logging.DEBUG)
logger_formatter = logging.Formatter('%(message)s - %(levelname)s')
# add handler to write logs to file "test.log"
logger_handler.setFormatter(logger_formatter)
logger.addHandler(logger_handler)


def log_message(message, level):
    if level == 10:
        return logger.debug(message)
    if level == 20:
        return logger.info(message)
    if level == 30:
        return logger.warning(message)
    if level == 40:
        return logger.error(message)
    if level == 50:
        return logger.critical(message)

#     """
#     this function should use the logger defined above and log messages.
#     level is the numeric representation of log level the message should refer to.
#     :param message:
#     :param level:
#     """
