# Import Standard Modules
import os
import yaml

# Setup the project directory
os.chdir(os.environ['us_stocks_path'])

# Import Package Modules
from modules.logging_module.logging_module import get_logger
from modules.data_preparation.data_preparation_utils import *


class DataPreparation:

    def __init__(self):

        # Setup Logger
        self.logger = get_logger(__class__.__name__)
        self.logger.info('__init__ - Instancing the class')

        # Read configuration
        self.config = yaml.safe_load(open('./configuration/config.yaml'))

        # Init instance variables
        self.data = None
        self.x = None
        self.y = None

    def run(self):

        # Load the data
        self.data = load_data(self.config['year_start'],
                              self.config['year_end'],
                              self.config['data_path'],
                              self.config['data_filename'])

        # Split data into features and label
        self.x, self.y = feature_label_split(self.data,
                                             self.config['y_columns'],
                                             self.config['x_drop_columns'])

        # Fill NaN values
        # self.x = fill_nan(self.x, )

