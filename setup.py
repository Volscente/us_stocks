import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="us_stocks",
    version="0.0.1",
    author="Volscente & Ali",
    description="Pipeline to analyse us stocks indicators",
    long_description=long_description,
    long_description_content_type="./README.md",
    packages=(
        setuptools.find_packages() +
        setuptools.find_packages(where='./pipelines/model_training') +
        setuptools.find_packages(where='./pipelines/logging_module')
    ),
    entry_points={
        'console_scripts': [
            'model_training = pipelines.model_training.model_training:run'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)