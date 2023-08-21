# Movies Data Processor

## Overview
Python tool to clean and analyze key columns in [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)

## Setup
1. Ensure Python 3.10 is installed.
2. Set up venv
```
python -m venv venv
source venv/bin/activate  
```
3. unzip data.zip. Alternatively, download the full dataset from [Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)


4. Poetry
`poetry install`

if RunTimeError, regenerate the poetry lock
```
rm poetry.lock
poetry lock
poetry install
```

## Running Tests
To ensure the functionality of the tool, a suite of tests has been provided. Run the tests using pytest:
`pytest`
