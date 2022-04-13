# Import Standard Modules
import os

# Import Package Modules
from modules.logging_module.logging_module import get_logger

# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0])


def load_data(year_start, year_end, data_path, data_filename):
    """
    Function that load all the required data in the given year interval
    :param year_start: Integer start year from which read the data
    :param year_end: Integer end year to which read the data
    :param data_path: String path to the data
    :param data_filename: String filename
    :return: Pandas DataFrame of the joined loaded .CSV files
    """

    logger.info('load_data - Start')

    try:

        logger.info('load_data - Read data')




