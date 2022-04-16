# Import Standard Modules
import pytest
import os

# Setup the project directory
os.chdir(os.environ['us_stocks_path'])

# Import Package Modules
from modules.pytest_test.test_data_preparation_fixtures import *


def test_load_data():
    """
    Test the function modules.data_preparation.data_preparation_utils.load_data
    :return: Boolean
    """
    


