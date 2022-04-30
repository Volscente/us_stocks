# Introduction
Analysis of hundreds of financial indicators for US stocks.

[Dataset](https://www.kaggle.com/datasets/cnic92/200-financial-indicators-of-us-stocks-20142018)

# Installation

## Environment Variable
Setup an environment variable called "us_stocks_path" with the 
absolute path to the project directory.

# Modules

## Data Preparation
The module prepares the data for being ingested into the model.

### data_preparation
It contains the class to perform the data preparation.

### data_preparation_utils
It contains the function needed by the class in 'data_preparation'

## logging_module

### logging_module.py
If contains the function 'get_logger' to instantiate a logger reading from 
the file configuration/log_configuration.yaml.