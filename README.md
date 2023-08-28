# Movies Data Processor 🎬

## Overview 📖
This Python tool is designed to clean and analyze key columns in [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset).

## Prerequisites 🛠
Python 3.10
Virtual Environment
Poetry Package Manager

## Setup 🚀

### Step 1: Virtual Environment
Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate  
```

### Step 2: Data Setup
Unzip the data.zip file to get the dataset. Alternatively, you can download the full dataset from Kaggle.
```
unzip data.zip

rm data.zip # optional
```

### Step 3: Install Dependencies with Poetry
Install the project dependencies using Poetry:

```
poetry install
```

## Execution ⚙️
```
cd ./movies_data

python3 src/main.py

```

## Running Tests 🧪
To ensure the functionality of the tool, a suite of tests has been provided. Run the tests using pytest:

```
pytest
```

## Notes 🗒️
I've added a download_data.py file which would be an implementation if I still had a gCloud free trial.

Instead of using a zip, the data could be pulled directly from gCloud with the script. 
