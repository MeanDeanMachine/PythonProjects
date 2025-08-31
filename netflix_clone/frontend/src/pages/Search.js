import React, { useState, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import { moviesAPI } from '../services/api';
import MovieCard from '../components/MovieCard';

const Search = () => {
  const [searchParams] = useSearchParams();
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const query = searchParams.get('q') || '';

  useEffect(() => {
    if (query) {
      searchMovies(query);
    }
  }, [query]);

  const searchMovies = async (searchQuery) => {
    setLoading(true);
    setError('');
    
    try {
      const response = await moviesAPI.searchMovies(searchQuery);
      setMovies(response.data.movies);
    } catch (error) {
      setError('Error searching movies');
      console.error('Search error:', error);
    }
    
    setLoading(false);
  };

  return (
    <div style={{ paddingTop: '100px', padding: '100px 60px 40px' }}>
      <h1 style={{ marginBottom: '30px' }}>
        {query ? `Search results for "${query}"` : 'Search Movies'}
      </h1>
      
      {loading && <div className="loading"><div className="spinner"></div></div>}
      
      {error && <div className="error-message">{error}</div>}
      
      {!loading && movies.length === 0 && query && (
        <p style={{ textAlign: 'center', fontSize: '18px', color: '#b3b3b3' }}>
          No movies found for "{query}". Try a different search term.
        </p>
      )}
      
      {movies.length > 0 && (
        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', 
          gap: '20px',
          marginTop: '20px'
        }}>
          {movies.map((movie) => (
            <MovieCard key={movie._id} movie={movie} />
          ))}
        </div>
      )}
    </div>
  );
};

export default Search;
