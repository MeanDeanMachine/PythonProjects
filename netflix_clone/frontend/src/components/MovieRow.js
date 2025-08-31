import React from 'react';
import MovieCard from './MovieCard';

const MovieRow = ({ title, movies }) => {
  return (
    <div className="movie-row">
      <h2 className="row-title">{title}</h2>
      <div className="movie-list">
        {movies.map((movie) => (
          <MovieCard key={movie._id} movie={movie} />
        ))}
      </div>
    </div>
  );
};

export default MovieRow;
