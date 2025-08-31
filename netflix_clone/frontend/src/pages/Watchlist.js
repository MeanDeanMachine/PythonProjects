import React, { useState, useEffect } from 'react';
import { authAPI, moviesAPI } from '../services/api';
import MovieCard from '../components/MovieCard';

const Watchlist = () => {
  const [watchlistMovies, setWatchlistMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchWatchlist();
  }, []);

  const fetchWatchlist = async () => {
    try {
      const profileResponse = await authAPI.getProfile();
      const watchlistIds = profileResponse.data.user.watchlist;
      
      if (watchlistIds.length === 0) {
        setWatchlistMovies([]);
        setLoading(false);
        return;
      }

      // Fetch movie details for each ID in watchlist
      const moviePromises = watchlistIds.map(id => moviesAPI.getMovie(id));
      const movieResponses = await Promise.allSettled(moviePromises);
      
      const movies = movieResponses
        .filter(response => response.status === 'fulfilled')
        .map(response => response.value.data.movie);
      
      setWatchlistMovies(movies);
    } catch (error) {
      setError('Error loading watchlist');
      console.error('Watchlist error:', error);
    }
    
    setLoading(false);
  };

  if (loading) {
    return <div className="loading"><div className="spinner"></div></div>;
  }

  return (
    <div style={{ paddingTop: '100px', padding: '100px 60px 40px' }}>
      <h1 style={{ marginBottom: '30px' }}>My Watchlist</h1>
      
      {error && <div className="error-message">{error}</div>}
      
      {watchlistMovies.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '60px 0' }}>
          <h2 style={{ color: '#b3b3b3', marginBottom: '20px' }}>Your watchlist is empty</h2>
          <p style={{ color: '#b3b3b3', marginBottom: '30px' }}>
            Add movies and shows to your list so you can watch them later.
          </p>
          <button 
            onClick={() => window.location.href = '/'}
            className="btn btn-primary"
          >
            Browse Movies
          </button>
        </div>
      ) : (
        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', 
          gap: '20px'
        }}>
          {watchlistMovies.map((movie) => (
            <MovieCard key={movie._id} movie={movie} />
          ))}
        </div>
      )}
    </div>
  );
};

export default Watchlist;
