import unittest
from src.movie_data_processor import MoviesData
import pandas as pd
import os

class TestMoviesData(unittest.TestCase):

    def setUp(self):
    
        self.movies = MoviesData('data/movies_metadata.csv')

        self.movies.clean_data()

    def test_num_movies(self):
        # Test the num_movies method
        result = self.movies.get_total_movies()
        self.assertEqual(result, 45430)
        # Add more assertions as needed

    def test_average_rating(self):
        # Test the average_rating method
        result = self.movies.get_average_rating()
        self.assertAlmostEqual(result, 5.62, places = 2)

    def test_top_5(self):
        # Test the top_5 method
        result = self.movies.get_top_5()
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 5)
        self.assertTrue('title' in result.columns and 'vote_average' in result.columns)
    def test_movies_per_year(self):
        # Test the movies_per_year method
        result = self.movies.get_movies_per_year()
        expected_years = self.movies.data['year'].value_counts().sort_index()
        self.assertTrue(all(result == expected_years))
        
    def test_movies_per_genre(self):
        # Test the movies_per_genre method
        result = self.movies.get_movies_per_genre()
        
        self.assertIsInstance(result, pd.Series)
        
    def test_save_to_json(self):
        # Test the save_to_json method
        test_path = "path_to_test_output.json"
        self.movies.export_to_json(test_path)
        # Check if the file was already created
        with open(test_path, 'r') as f:
            content = f.read()
            self.assertTrue(content)

if __name__ == '__main__':
    unittest.main()