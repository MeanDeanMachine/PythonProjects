import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

// Create axios instance with default config
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
  timeout: 10000,
});

// Add token to requests if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle token expiration and CORS errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Handle CORS errors
    if (error.code === 'ERR_NETWORK' || error.message.includes('Network Error')) {
      console.error('Network/CORS Error: Make sure backend is running on http://localhost:5000');
    }
    
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Auth API calls
export const authAPI = {
  register: (userData) => api.post('/auth/register', userData),
  login: (credentials) => api.post('/auth/login', credentials),
  getProfile: () => api.get('/auth/profile'),
};

// Movies API calls
export const moviesAPI = {
  getMovies: (params = {}) => api.get('/movies', { params }),
  getMovie: (id) => api.get(`/movies/${id}`),
  searchMovies: (query, limit = 20) => api.get('/movies/search', { params: { q: query, limit } }),
  getMoviesByGenre: (genre, limit = 20) => api.get(`/movies/genre/${genre}`, { params: { limit } }),
  getTrendingMovies: (limit = 10) => api.get('/movies/trending', { params: { limit } }),
  watchMovie: (id) => api.post(`/movies/${id}/watch`),
  addToWatchlist: (id) => api.post(`/movies/${id}/watchlist`),
  removeFromWatchlist: (id) => api.delete(`/movies/${id}/watchlist`),
};

export default api;
