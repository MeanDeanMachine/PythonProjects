import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { moviesAPI } from '../services/api';

const MovieDetail = () => {
  const { id } = useParams();
  const [movie, setMovie] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [isWatching, setIsWatching] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchMovie = async () => {
      try {
        const response = await moviesAPI.getMovie(id);
        setMovie(response.data.movie);
        setLoading(false);
      } catch (error) {
        setError('Movie not found');
        setLoading(false);
      }
    };

    fetchMovie();
  }, [id]);

  const handlePlay = async () => {
    try {
      await moviesAPI.watchMovie(id);
      setIsWatching(true);
    } catch (error) {
      console.error('Error playing movie:', error);
    }
  };

  const handleAddToWatchlist = async () => {
    try {
      await moviesAPI.addToWatchlist(id);
      alert('Added to watchlist!');
    } catch (error) {
      console.error('Error adding to watchlist:', error);
    }
  };

  if (loading) {
    return <div className="loading"><div className="spinner"></div></div>;
  }

  if (error) {
    return (
      <div className="movie-detail">
        <div className="error-message">{error}</div>
        <button onClick={() => navigate('/')} className="btn btn-primary">
          Go Back Home
        </button>
      </div>
    );
  }

  return (
    <div className="movie-detail">
      <div 
        className="movie-hero"
        style={{
          backgroundImage: `linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.8)), url(${movie.thumbnail_url})`
        }}
      >
        <div className="movie-detail-content">
          <h1 className="movie-detail-title">{movie.title}</h1>
          <div className="movie-detail-meta">
            <span>{movie.year}</span>
            <span>{movie.duration} min</span>
            <span>★ {movie.rating}/10</span>
          </div>
          <p className="movie-detail-description">{movie.description}</p>
          <div className="movie-actions">
            <button className="btn btn-primary" onClick={handlePlay}>
              ▶ Play
            </button>
            <button className="btn btn-secondary" onClick={handleAddToWatchlist}>
              + My List
            </button>
          </div>
        </div>
      </div>

      {isWatching && (
        <div className="video-player">
          <video controls autoPlay>
            <source src={movie.video_url} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
      )}

      <div style={{ padding: '40px 60px' }}>
        <h3>About {movie.title}</h3>
        <p style={{ marginTop: '20px', lineHeight: '1.6' }}>
          <strong>Genre:</strong> {movie.genre}<br />
          <strong>Year:</strong> {movie.year}<br />
          <strong>Duration:</strong> {movie.duration} minutes<br />
          <strong>Views:</strong> {movie.views || 0}
        </p>
      </div>
    </div>
  );
};

export default MovieDetail;
