# Import Standard Modules
import logging.config
import yaml
import os

# Set root path
os.chdir(os.environ['us_stocks_path'])


def get_logger(logger_name):
    """
    Set the configuration for the logging module and return the requested logger
    :return: Logger object
    """

    # Read the log_configuration file
    with open('./configuration/log_configuration.yaml', 'r') as file:
        log_config = yaml.safe_load(file.read())
        logging.config.dictConfig(log_config)

    # Retrieve the requested logger
    logger = logging.getLogger(logger_name)

    return logger
