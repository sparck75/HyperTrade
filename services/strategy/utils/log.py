import logging


class Logger:
    @staticmethod
    def get(name):
        logging.basicConfig(format='%(levelname)s %(message)s')
        log = logging.getLogger(name)
        log.setLevel(logging.DEBUG)

        return log
