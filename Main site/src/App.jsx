import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { motion } from 'framer-motion';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import CareerPredictor from './pages/CareerPredictor';
import Forum from './pages/Forum';
import Expert from './pages/Expert';
import About from './pages/About';
import Contact from './pages/Contact';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <motion.main
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
        >
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/career-predictor" element={<CareerPredictor />} />
            <Route path="/forum" element={<Forum />} />
            <Route path="/expert" element={<Expert />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
          </Routes>
        </motion.main>
      </div>
    </Router>
  );
}

export default App;
