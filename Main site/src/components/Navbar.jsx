import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Menu, X, Home, Brain, MessageCircle, Users, Info, Phone } from 'lucide-react';
import './Navbar.css';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const location = useLocation();

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navItems = [
    { path: '/', name: 'Home', icon: Home },
    { path: '/career-predictor', name: 'Career Predictor', icon: Brain },
    { path: '/forum', name: 'Forum', icon: MessageCircle },
    { path: '/expert', name: 'Expert', icon: Users },
    { path: '/about', name: 'About', icon: Info },
    { path: '/contact', name: 'Contact', icon: Phone },
  ];

  return (
    <motion.nav
      className={`navbar ${scrolled ? 'scrolled' : ''}`}
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          <motion.div
            className="logo-container"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            <span className="logo-icon">🚀</span>
            <span className="logo-text">Future Foundry</span>
          </motion.div>
        </Link>

        <div className="navbar-menu">
          {navItems.map((item) => {
            const Icon = item.icon;
            return (
              <Link
                key={item.path}
                to={item.path}
                className={`navbar-item ${location.pathname === item.path ? 'active' : ''}`}
              >
                <Icon size={18} />
                <span>{item.name}</span>
              </Link>
            );
          })}
        </div>

        <div className="navbar-actions">
          <button className="btn btn-ghost">Sign In</button>
          <button className="btn btn-primary">Get Started</button>
        </div>

        <button
          className="navbar-toggle"
          onClick={() => setIsOpen(!isOpen)}
          aria-label="Toggle navigation"
        >
          {isOpen ? <X size={24} /> : <Menu size={24} />}
        </button>
      </div>

      <motion.div
        className={`navbar-mobile ${isOpen ? 'open' : ''}`}
        initial={{ opacity: 0, height: 0 }}
        animate={{ 
          opacity: isOpen ? 1 : 0, 
          height: isOpen ? 'auto' : 0 
        }}
        transition={{ duration: 0.3 }}
      >
        {navItems.map((item) => {
          const Icon = item.icon;
          return (
            <Link
              key={item.path}
              to={item.path}
              className={`navbar-mobile-item ${location.pathname === item.path ? 'active' : ''}`}
              onClick={() => setIsOpen(false)}
            >
              <Icon size={18} />
              <span>{item.name}</span>
            </Link>
          );
        })}
        <div className="navbar-mobile-actions">
          <button className="btn btn-ghost">Sign In</button>
          <button className="btn btn-primary">Get Started</button>
        </div>
      </motion.div>
    </motion.nav>
  );
};

export default Navbar;
