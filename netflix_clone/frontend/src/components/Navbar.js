import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const Navbar = () => {
  const { user, logout, isAuthenticated } = useAuth();
  const [scrolled, setScrolled] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const handleScroll = () => {
      const isScrolled = window.scrollY > 100;
      setScrolled(isScrolled);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/search?q=${encodeURIComponent(searchQuery.trim())}`);
      setSearchQuery('');
    }
  };

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  if (!isAuthenticated) {
    return null;
  }

  return (
    <nav className={`navbar ${scrolled ? 'scrolled' : ''}`}>
      <div className="navbar-left">
        <Link to="/" className="navbar-brand">NETFLIX</Link>
        <ul className="navbar-nav">
          <li><Link to="/" className="nav-link">Home</Link></li>
          <li><Link to="/watchlist" className="nav-link">My List</Link></li>
        </ul>
      </div>
      
      <div className="navbar-right">
        <div className="search-container">
          <form onSubmit={handleSearch}>
            <input
              type="text"
              placeholder="Search movies..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="search-input"
            />
          </form>
        </div>
        
        <div className="user-menu">
          <span className="user-name">Hello, {user?.name}</span>
          <button onClick={handleLogout} className="btn btn-secondary">Logout</button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
