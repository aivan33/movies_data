import logging
from movie_data_processor import MoviesData

def main():
    logging.basicConfig(level = logging.INFO)

    # Initalize MoviesData class
    movies = MoviesData("./data/movies_metadata.csv")

    # Task Execution
    movies.clean_data()
    logging.info(f"Number of movies: {movies.get_total_movies()}")
    logging.info(f"Average rating: {movies.get_average_rating()}")
    logging.info(f"Top 5 rated movies: \n{movies.get_top_5()}")
    logging.info(f"Number of movies released each year: \n{movies.get_movies_per_year()}")
    logging.info(f"Numer of movies per genre: \n{movies.get_movies_per_genre()}")

    # Save to JSON
    movies.export_to_json("data/movies.json")
    logging.info(f"Dataset - movies.json - saved in the data folder.")


if __name__ == "__main__":
    main()
