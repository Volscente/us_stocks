import os
import yaml
import pandas as pd
from zenml.steps import Output, step
from zenml.pipelines import pipeline
from modules.data_preparation.data_preparation_utils import load_data, feature_label_split, fill_nan


@step(enable_cache=False)
def load_configuration() -> dict:
    directory = os.path.abspath('../configuration/')
    config = yaml.safe_load(open(os.path.join(directory, 'config.yaml')))
    return config


@step(enable_cache=True)
def load_financial_data(config: dict) -> pd.DataFrame:
    financial_data = load_data(config['year_start'],
                               config['year_end'],
                               config['data_path'],
                               config['data_filename'])
    return financial_data


@step(enable_cache=True)
def train_test_split(config: dict, financial_data: pd.DataFrame) -> Output(x=pd.DataFrame, y=pd.DataFrame):
    x, y = feature_label_split(financial_data,
                               config['y_columns'],
                               config['x_drop_columns'])
    return x, y


@step(enable_cache=True)
def data_preprocessing(config: dict, x: pd.DataFrame) -> pd.DataFrame:
    x = fill_nan(x,
                 config['fill_nan_method'],
                 config['valid_fill_nan_methods'])
    return x


@pipeline(enable_cache=True)
def financial_prediction_pipeline(
    _load_configuration,
    _load_financial_data,
    _train_test_split,
    _data_preprocessing
):
    """Links all the steps together in a pipeline"""
    configuration = _load_configuration()
    data = _load_financial_data(config=configuration)
    x, y = _train_test_split(config=configuration, financial_data=data)
    x = _data_preprocessing(config=configuration, x=x)
    print(x)
    return x


if __name__ == "__main__":
    # Run the pipeline
    p = financial_prediction_pipeline(_load_configuration=load_configuration(),
                                      _load_financial_data=load_financial_data(),
                                      _train_test_split=train_test_split(),
                                      _data_preprocessing=data_preprocessing())
    p.run()
