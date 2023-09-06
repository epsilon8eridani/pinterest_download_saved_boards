import logging


def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    fmt = '%(message)s'

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(CustomFormatter(fmt))
    logger.addHandler(ch)


class CustomFormatter(logging.Formatter):
    """Logging colored formatter, adapted from https://stackoverflow.com/a/56944256/3638629"""

    teal = '\x1b[38;43m'
    lavender = '\x1b[38;5;183m'
    yellow = '\x1b[38;5;220m'
    red = '\x1b[38;5;160m'
    bold_red = '\x1b[31;196m'
    reset = '\x1b[0m'

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.teal + self.fmt + self.reset,
            logging.INFO: self.lavender + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)