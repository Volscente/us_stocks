# Import Standard Modules
import logging.config
import yaml
import os

# Set root path
# os.chdir(os.environ['us_stocks'])


def get_logger(logger_name: str = None):
    """
    Set the configuration for the logging module and return the requested logger
    :return: Logger object
    """

    directory = os.path.abspath('../configuration/')

    # Read the log_configuration file
    with open(os.path.join(directory, 'log_configuration.yaml'), 'r') as file:
        log_config = yaml.safe_load(file.read())
        logging.config.dictConfig(log_config)

    # Retrieve the requested logger
    logger = logging.getLogger(logger_name)

    return logger


if __name__ == '__main__':
    get_logger()
