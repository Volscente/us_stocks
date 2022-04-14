# Import Standard Modules
import pytest
import os
import yaml

# Setup the project directory
os.chdir(os.environ['us_stocks_path'])

@pytest.fixture
def configuration():
    """
    Initiate the configuration object
    :return: Configuration object
    """

    # Read configuration file
    configuration = yaml.safe_load(open('./configuration/config.yaml'))

    return configuration
