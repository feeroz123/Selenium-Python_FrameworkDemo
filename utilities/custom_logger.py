import logging
import inspect


def custom_logging(logLevel=logging.DEBUG):

    # Logger name is derived form the method/class which calls the logger
    logger_name = inspect.stack()[1][3]

    # Create a logger with the derived logger name, and set the log level as received
    logger = logging.getLogger(logger_name)
    logger.setLevel(logLevel)

    # Create a File Handler with (OVER)WRITE Mode, and set the log level as received
    file_handler = logging.FileHandler("automation.log", mode='w')
    file_handler.setLevel(logLevel)

    # Create a Formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s : %(message)s",
                                  datefmt="%d-%m-%Y %I:%M:%S %p")

    # Assign the formatter to handler
    file_handler.setFormatter(formatter)

    # Assign the handler to the logger
    logger.addHandler(file_handler)

    # Return the Logger to the calling method
    return logger


