# Import Package Modules
from modules.data_preparation.data_preparation import DataPreparation


def run():

    # Instantiate the class
    data_preparation = DataPreparation()

    # Run the job
    data_preparation.run()


# TODO - Testing purposes
run()
