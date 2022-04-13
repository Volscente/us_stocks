# Import Standard Modules
import os
import yaml

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


    def run(self):

