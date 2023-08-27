# Movies Data Processor 🎬

## Overview 📖
This Python tool is designed to clean and analyze key columns in [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset). It's a robust solution for anyone looking to gain insights into the world of movies.

## Prerequisites 🛠
Python 3.10
Virtual Environment
Poetry Package Manager

## Setup 🚀

### Step 1: Virtual Environment
Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate  
```

### Step 2: Data Setup
Unzip the data.zip file to get the dataset. Alternatively, you can download the full dataset from Kaggle.
```
unzip data.zip

rm data.zip
```

### Step 3: Install Dependencies with Poetry
Install the project dependencies using Poetry:

```
poetry install
```

## Running Tests 🧪
To ensure the functionality of the tool, a suite of tests has been provided. Run the tests using pytest:

```
pytest
```