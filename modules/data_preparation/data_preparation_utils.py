# Import Standard Modules
import os
import sys

# Import Package Modules
import pandas as pd

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

        logger.info('load_data - Define time year range')

        # Year range
        # Case single year
        if year_start == year_end:
            year_range = [year_start]
        else:
            year_range = range(year_start, year_end, 1)  # Case multiple years

        logger.info('load_data - Year range: {}'.format(year_range))

    except Exception as e:

        logger.error('load_data - Unable to compute the time year range')
        logger.error(e)
        sys.exit(1)

    try:

        logger.info('load_data - Initialize the Pandas DataFrame')

        # Initialize empty dataframe
        data = pd.DataFrame()

        logger.info('load_data - Load and join datasets')

        # Fetch the dataset by year
        for year in year_range:
            logger.info('load_data - Load the data from {}'.format(year))

            # Define data path
            csv_data_path = data_path + str(year) + '_' + data_filename

            # Load the data from .CSV
            loaded_data = pd.read_csv(csv_data_path,
                                      sep=';',
                                      encoding='latin1',
                                      index_col=0)

            logger.info('load_data - Loaded data dimension: {}'.format(len(loaded_data)))

            # Concat the data
            data = pd.concat([data, loaded_data])

            logger.info('load_data - Data dimension: {}'.format(len(data)))

    except Exception as e:

        logger.error('load_data - Unable to load and join datasets')
        logger.error(e)
        sys.exit(1)

    logger.info('load_data - End')

    return data
