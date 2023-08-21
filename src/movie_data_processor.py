import pandas as pd
import logging
from ast import literal_eval

# Setting up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MoviesData:
    def __init__(self, dataset_path):
        """ Initialize the MoviesData object and load the dataset. """
        self.data = None # Why do we initialize data here
        self.load_data(dataset_path)

    def load_data(self, dataset_path):
        """ Load the dataset from path """
        try:
            self.data = pd.read_csv(dataset_path) # and here
            logging.info(f"Dataset loaded from {dataset_path}. Num of records - {len(self.data)}")
        except Exception as e:
            logging.error(f"Error loading dataset: {e}")
            return None
    
    def clean_data(self):
        """ Clean and Transform the data for relevant columns. """
    
        # Handle missing values, duplicates and dtype transformations
        self.data['genres'] = self.data['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

        self.data['release_date'] = pd.to_datetime(self.data['release_date'], errors='coerce')
        self.data['year'] = self.data['release_date'].dt.year

        dropped_ids = self.data.duplicated(subset = 'id').sum() # for logging
        self.data.drop_duplicates(subset = 'id', inplace = True)

        nan_values = self.data['title'].isnull().sum() # for logging
        self.data.dropna(subset = ['title'], inplace = True)

        # Log the number of duplicates and missing values handled
        logging.info(f"Dropped {dropped_ids} duplicate entries based on id.")
        logging.info(f"Dropped {nan_values} entries with missing title.")

    def get_total_movies(self):
        """ Return the number of movies in the dataset. """
        return len(self.data)

    def get_average_rating(self):
        """ Return the average rating of all movies. """
        return self.data['vote_average'].mean()

    def get_top_5(self):
        """ Return the top 5 highest rated movies. """
        return self.data.nlargest(5, 'vote_average')[['title', 'vote_average']]


    def get_movies_per_year(self):
        """ Return the number of movies released each year, sorted by year. """
        return self.data['year'].value_counts().sort_index()
    
    def get_movies_per_genre(self):
        """ Returns the number of movies per genre. """
        genres = self.data['genres'].explode()
        return genres.value_counts()

    def export_to_json(self, json_path):
        """Export the dataset to a JSON file.
        
        Parameters:
        - json_path (str): Path to save the JSON file.
        """
        try:
            self.data.to_json(json_path, orient='records', lines=True)
            logging.info(f"Data exported to {json_path}.")
        except Exception as e:
            logging.error(f"Error exporting data: {e}")