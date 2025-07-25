# Movie Recommender System

A content-based movie recommendation system built using Python, Streamlit, and machine learning techniques. This application recommends similar movies based on user selection using cosine similarity.

## Features

- **Interactive Web Interface**: Clean and user-friendly Streamlit interface
- **Content-Based Filtering**: Recommends movies based on similarity scores
- **Fast Recommendations**: Pre-computed similarity matrix for instant results
- **Top 5 Recommendations**: Returns the 5 most similar movies for any selected movie

## Dataset

This application uses **The Movie Database (TMDB)** dataset, which provides comprehensive movie information including:
- Movie titles and IDs
- Genres, keywords, and cast information
- Movie overviews and metadata
- Release dates and ratings

## How It Works

The system uses a pre-trained similarity matrix built from TMDB data to find movies that are most similar to the user's selection. When a user selects a movie:

1. The system finds the index of the selected movie in the TMDB dataset
2. Retrieves similarity scores for all other movies
3. Sorts movies by similarity score in descending order
4. Returns the top 5 most similar movies (excluding the selected movie itself)

## Prerequisites

- Python 3.7 or higher
- Required Python packages (see requirements.txt)

## Installation

1. **Clone or download the project files**
   ```bash
   git clone <repository-url>
   cd movie-recommender-system
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure you have the required data files**
   - `movie_dict.pkl`: Contains movie data (titles, IDs, etc.)
   - `similarity.pkl`: Pre-computed similarity matrix

## Usage

1. **Run the Streamlit application**
   ```bash
   streamlit run app.py
   ```

2. **Open your web browser**
   - The application will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, navigate to the URL manually

3. **Use the application**
   - Select a movie from the dropdown menu
   - Click the "Recommend" button
   - View the 5 recommended movies displayed below

## File Structure

```
movie-recommender-system/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── movie_dict.pkl        # Movie data (required)
├── similarity.pkl        # Similarity matrix (required)
└── README.md            # Project documentation
```

## Key Dependencies

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Pickle**: For loading pre-trained models and data
- **NumPy**: Numerical computing (dependency of pandas)

## Data Requirements

The application requires two pickle files generated from TMDB data:

1. **movie_dict.pkl**: Contains processed TMDB movie data including:
   - Movie titles
   - Movie IDs (for potential poster fetching)
   - Other metadata from TMDB dataset

2. **similarity.pkl**: Pre-computed cosine similarity matrix between movies based on TMDB features such as:
   - Genres
   - Keywords
   - Cast and crew
   - Movie overviews
   - Other relevant features

*Note: These pickle files need to be generated from the TMDB dataset using feature extraction and similarity computation. The raw TMDB dataset can be obtained from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) or [TMDB API](https://www.themoviedb.org/documentation/api).*

## Features to Add (Future Enhancements)

- **Movie poster integration**: Use TMDB API to fetch and display movie posters (commented code available)
- **Movie details**: Display additional TMDB information like ratings, release dates, and overviews
- **Genre-based filtering**: Allow users to filter recommendations by genre
- **Multiple recommendation algorithms**: Implement collaborative filtering alongside content-based
- **User rating system**: Allow users to rate movies and improve recommendations
- **Search functionality**: Add search capability for movie titles
- **TMDB API integration**: Real-time data fetching for updated movie information

## Troubleshooting

**Common Issues:**

1. **Missing pickle files**: Ensure `movie_dict.pkl` and `similarity.pkl` are in the same directory as `app.py`

2. **Import errors**: Install all requirements using `pip install -r requirements.txt`

3. **Streamlit not opening**: Check if port 8501 is available or specify a different port:
   ```bash
   streamlit run app.py --server.port 8502
   ```

4. **Empty recommendations**: Verify that your movie dataset contains the selected movie title

## Technical Details

- **Dataset**: TMDB (The Movie Database) movie dataset
- **Algorithm**: Content-based filtering using cosine similarity
- **Features Used**: Movie genres, keywords, cast, crew, and overviews from TMDB
- **Framework**: Streamlit for web interface
- **Data Processing**: Pandas for data manipulation
- **Model Storage**: Pickle for serialized model and data storage

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the repository for specific license information.

## Support

For issues and questions:
- Check the troubleshooting section above
- Review the code comments in `app.py`
- Ensure all dependencies are properly installed

---

**Note**: This is a basic implementation. For production use, consider adding error handling, input validation, and performance optimizations.
