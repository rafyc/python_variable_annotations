#!/usr/bin/env python3
"""
Main file
"""
import re
from typing import List, Tuple
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"
    PII_FIELDS = ("email",
                  "phone",
                  "address",
                  "credit_card",
                  "social_security")

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter values in incoming log records using filter_datum method
        """
        formated = filter_datum(self.fields,
                                RedactingFormatter.REDACTION,
                                super().format(record),
                                RedactingFormatter.SEPARATOR)
        return formated


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Return the log message obfuscated by 'redaction' argument
    """
    for i in fields:
        message = re.sub(i + '=.+?' + separator,
                         i + '=' + redaction + separator,
                         message)
    return message


def get_logger() -> logging.Logger:
    """This method get a logger with the 4 steps following :
    - Create a logger,
    - Create handler
    - Create formatters and add it to handler,
    - Aad handler to the logger
    Return the logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    redacting_formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(redacting_formatter)

    logger.addHandler(stream_handler)

    return logger
