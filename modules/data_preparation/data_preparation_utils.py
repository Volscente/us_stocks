# Import Standard Modules
import os
import sys
import pandas as pd
import numpy as np
from typing import Union

# Import Package Modules
from modules.logging_module.logging_module import get_logger

# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0])


def load_data(year_start: int,
              year_end: int,
              data_path: str,
              data_filename: str) -> pd.DataFrame:
    """
    Load all the required data in the given year interval
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
        year_range = np.arange(year_start, year_end + 1, 1, dtype=np.int32)

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
                                      sep=',',
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


def feature_label_split(data: pd.DataFrame,
                        y_column: list,
                        x_drop_columns: list) -> Union[pd.DataFrame, pd.DataFrame]:
    """
    Split the data into features and label
    :param data: Pandas DataFrame of data
    :param y_column: List of y columns
    :param x_drop_columns: List of columns to drop for x
    :return: Pandas DataFrame of x and y
    """

    logger.info('feature_label_split - Start')

    try:

        logger.info('feature_label_split - Define the label')

        # Define label
        y = data[y_column]

    except Exception as e:

        logger.error('feature_label_split - Unable to define the label')
        logger.error(e)
        sys.exit(1)

    try:

        logger.info('feature_label_split - Define features')

        # Define features
        # NOTE: Drop '2015 PRICE VAR [%]' because it is directly related to the Class and it is only valid a posteriori
        x = data.drop(x_drop_columns, axis=1)

    except Exception as e:

        logger.error('feature_label_split - Unable to define features')
        logger.error(e)
        sys.exit(1)

    logger.info('feature_label_split - End')

    return x, y


def fill_nan(x: pd.DataFrame,
             fill_nan_method: str,
             valid_fill_nan_methods: list) -> pd.DataFrame:
    """
    Fill NaN values in the features
    :param x: Pandas DataFrame of features
    :param fill_nan_method: String identifies the Fill NaN method
    :param valid_fill_nan_methods: List of valid Fill NaN methods
    :return: Pandas DataFrame of  features filled
    """

    logger.info('fill_nan - Start')

    try:

        logger.info('fill_nan - Check Fill NaN method validity')

        # Check if the fill_nan_method is in valid_fill_nan_methods
        if fill_nan_method not in valid_fill_nan_methods:

            logger.error('fill_nan - Invalid Fill NaN method')
            sys.exit(1)

    except Exception as e:

        logger.error('fill_nan - Unable to check the Fill NaN method validity')
        logger.error(e)
        sys.exit(1)

    try:

        # Switch the fill_nan_method
        if fill_nan_method == 'mean':

            logger.info('fill_nan - Fill NaN values with the Mean')

            # Fill NaN values with the mean
            x_filled = x.fillna(x.mean())

    except Exception as e:

        logger.error('fill_nan - Unable to Fill NaN values')
        logger.error(e)
        sys.exit(1)

    logger.info('fill_nan - End')

    return x_filled


