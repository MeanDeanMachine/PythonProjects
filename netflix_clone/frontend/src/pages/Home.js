import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { moviesAPI } from '../services/api';
import MovieRow from '../components/MovieRow';

const Home = () => {
  const [featuredMovie, setFeaturedMovie] = useState(null);
  const [trendingMovies, setTrendingMovies] = useState([]);
  const [actionMovies, setActionMovies] = useState([]);
  const [dramaMovies, setDramaMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        console.log('Fetching movies data...');
        
        // First try to get all movies to see if any exist
        const allMoviesResponse = await moviesAPI.getMovies({ limit: 50 });
        console.log('All movies response:', allMoviesResponse.data);
        
        const allMovies = allMoviesResponse.data.movies || [];
        
        if (allMovies.length === 0) {
          console.warn('No movies found in database');
          setLoading(false);
          return;
        }
        
        // Set featured movie
        setFeaturedMovie(allMovies[0]);
        
        // For now, use all movies for different categories
        setTrendingMovies(allMovies.slice(0, 10));
        setActionMovies(allMovies.filter(movie => movie.genre.toLowerCase().includes('action')));
        setDramaMovies(allMovies.filter(movie => movie.genre.toLowerCase().includes('drama')));
        
        console.log('Movies loaded successfully:', {
          total: allMovies.length,
          trending: allMovies.slice(0, 10).length,
          action: allMovies.filter(movie => movie.genre.toLowerCase().includes('action')).length,
          drama: allMovies.filter(movie => movie.genre.toLowerCase().includes('drama')).length
        });
        
        setLoading(false);
      } catch (error) {
        console.error('Error fetching data:', error);
        console.error('Error details:', error.response?.data || error.message);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const handlePlayMovie = () => {
    if (featuredMovie) {
      navigate(`/movie/${featuredMovie._id}`);
    }
  };

  const handleAddToWatchlist = async () => {
    if (featuredMovie) {
      try {
        await moviesAPI.addToWatchlist(featuredMovie._id);
        alert('Added to watchlist!');
      } catch (error) {
        console.error('Error adding to watchlist:', error);
      }
    }
  };

  if (loading) {
    return <div className="loading"><div className="spinner"></div></div>;
  }

  return (
    <div className="home">
      {/* Hero Section */}
      {featuredMovie && (
        <div 
          className="hero"
          style={{
            backgroundImage: `linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.8)), url(${featuredMovie.thumbnail_url})`
          }}
        >
          <div className="hero-content">
            <h1 className="hero-title">{featuredMovie.title}</h1>
            <p className="hero-description">{featuredMovie.description}</p>
            <div className="hero-buttons">
              <button className="btn btn-primary" onClick={handlePlayMovie}>
                ▶ Play
              </button>
              <button className="btn btn-secondary" onClick={handleAddToWatchlist}>
                + My List
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Movie Rows */}
      <div className="movie-rows">
        {!loading && trendingMovies.length === 0 && actionMovies.length === 0 && dramaMovies.length === 0 && (
          <div style={{ textAlign: 'center', padding: '60px 0' }}>
            <h2 style={{ color: '#b3b3b3', marginBottom: '20px' }}>No movies available</h2>
            <p style={{ color: '#b3b3b3', marginBottom: '30px' }}>
              Please ensure the backend is running and the database has been seeded with movies.
            </p>
            <p style={{ color: '#b3b3b3', fontSize: '14px' }}>
              Run: <code>python seed_data.py</code> in the backend directory
            </p>
          </div>
        )}
        
        {trendingMovies.length > 0 && (
          <MovieRow title="Trending Now" movies={trendingMovies} />
        )}
        {actionMovies.length > 0 && (
          <MovieRow title="Action Movies" movies={actionMovies} />
        )}
        {dramaMovies.length > 0 && (
          <MovieRow title="Drama Series" movies={dramaMovies} />
        )}
      </div>
    </div>
  );
};

export default Home;
