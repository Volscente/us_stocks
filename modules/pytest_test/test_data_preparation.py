# Import Standard Modules
import pytest
import os

# Setup the project directory
os.chdir(os.environ['us_stocks_path'])

# Import Package Modules
from modules.pytest_test.test_data_preparation_fixtures import *
from modules.data_preparation.data_preparation_utils import *


@pytest.mark.parametrize("year_start, year_end, expected_length", [
    (2014, 2014, 3808),
    (2014, 2016, 12725),
    (2014, 2015, 7928)
])
def test_load_data(configuration, year_start, year_end, expected_length):
    """
    Test the function modules.data_preparation.data_preparation_utils.load_data
    :param configuration: Configuration object
    :param year_start: Integer start year of dataset
    :param year_end: Integer end year of dataset
    :param expected_length: Integer dataset length
    :return: Boolean
    """

    # Call the function 'load_data'
    dataset = load_data(year_start,
                        year_end,
                        configuration['data_path'],
                        configuration['data_filename'])

    # Verify the dataset length
    assert len(dataset) == expected_length

# TODO test_feature_label_split()


@pytest.mark.parametrize('input_fill_nan_method, expected_output', [
    ('mean', 0)
])
def test_fill_nan(test_data, configuration, input_fill_nan_method, expected_output):
    """
    Test the function modules.data_preparation.data_preparation_utils.fill_nan
    :param test_data: Pandas test dataset
    :param configuration: Configuration object
    :param input_fill_nan_method: String fill nan method to test
    :param expected_output: Integer count of remaining invalid rows
    :return: Boolean
    """

    # Call the function 'fill_nan'
    test_data_filled = fill_nan(test_data, input_fill_nan_method, configuration['valid_fill_nan_methods'])

    # Retrieve invalid rows
    invalid_rows = test_data_filled.isna().sum().sum()

    assert invalid_rows == expected_output





