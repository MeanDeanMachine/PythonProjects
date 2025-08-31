import React from 'react';
import { useNavigate } from 'react-router-dom';

const MovieCard = ({ movie }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/movie/${movie._id}`);
  };

  return (
    <div className="movie-card" onClick={handleClick}>
      <img 
        src={movie.thumbnail_url} 
        alt={movie.title}
        className="movie-poster"
        onError={(e) => {
          e.target.src = 'https://via.placeholder.com/250x375/333333/FFFFFF?text=No+Image';
        }}
      />
      <div className="movie-info">
        <h3 className="movie-title">{movie.title}</h3>
        <p className="movie-year">{movie.year} • {movie.genre}</p>
        <p className="movie-rating">★ {movie.rating}/10</p>
      </div>
    </div>
  );
};

export default MovieCard;
