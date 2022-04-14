# Import Standard Modules
import pytest
import yaml


@pytest.fixture
def configuration():
    """
    Initiate the configuration object
    :return: Configuration object
    """

    # Read configuration file
    configuration = yaml.safe_load(open('./configuration/config.yaml'))

    return configuration
