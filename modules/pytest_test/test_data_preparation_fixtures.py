# Import Standard Modules
import pytest
import yaml

# Import Package Modules
from modules.data_preparation.data_preparation_utils import load_data


@pytest.fixture
def configuration():
    """
    Initiate the configuration object
    :return: Configuration object
    """

    # Read configuration file
    configuration = yaml.safe_load(open('./configuration/config.yaml'))

    return configuration


@pytest.fixture
def test_data(configuration):
    """
    Initiate a Pandas test dataset
    :return: Pandas test dataset
    """

    # Read Pandas test dataset
    data = load_data(configuration['year_start'],
                     configuration['year_end'],
                     configuration['data_path'],
                     configuration['data_filename'])

    return data
