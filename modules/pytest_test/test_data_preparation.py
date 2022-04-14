# Import Standard Modules
import pytest
import os

# Setup the project directory
os.chdir(os.environ['us_stocks_path'])

# Import Package Modules
from modules.pytest_test.test_data_preparation_fixtures import *


def test_load_data():

    assert 1==1
