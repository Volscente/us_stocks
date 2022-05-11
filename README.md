# Introduction
Analysis of hundreds of financial indicators for US stocks.

[Dataset](https://www.kaggle.com/datasets/cnic92/200-financial-indicators-of-us-stocks-20142018)

# Installation

## Environment Variable
Setup an environment variable called "us_stocks_path" with the 
absolute path to the project directory.

## Python version
- For some packages, e.g. `zenml`, we need to have a python version between 3.6 to 3.8
- i'm working on 3.7.10
- We can install that via `pyenv`
```bash
# install xcode command line tools
xcode-select --install

# install pyenv using homebrew
brew update
brew install openssl readline sqlite3 xz zlib openssl@1.0
brew install pyenv

# install new python dist using pyenv
pyenv install 3.7.10

# set it as global usage version
pyenv global 3.7.10

# create virtual environment
pyenv virtualenv 3.7.10 venv-us-stocks

# set the virtual environment in your IDE using the path of newly installed python
python_interpreter_path="~/.pyenv/versions/venv-us-stocks/lib/python3.7/bin/python"
```

## Create Wheel Package
Create wheel file:
```
python setup.py bdist_wheel
```
Check the created wheel file through the following command:
```
check-wheel-contents dist
```

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