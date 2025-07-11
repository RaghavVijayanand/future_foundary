import React from 'react';
import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import { ArrowRight, Star, Users, TrendingUp, Brain, MessageCircle, Award } from 'lucide-react';
import './Home.css';

const Home = () => {
  const features = [
    {
      icon: Brain,
      title: 'AI-Powered Career Prediction',
      description: 'Get personalized career recommendations based on your skills, interests, and personality using advanced machine learning algorithms.',
    },
    {
      icon: MessageCircle,
      title: 'Community Forum',
      description: 'Connect with like-minded individuals, share experiences, and get advice from professionals in your field of interest.',
    },
    {
      icon: Users,
      title: 'Expert Consultation',
      description: 'Book one-on-one sessions with industry experts and career counselors to get personalized guidance.',
    },
    {
      icon: TrendingUp,
      title: 'Career Growth Tracking',
      description: 'Track your progress, set goals, and receive recommendations for skill development and career advancement.',
    },
  ];

  const testimonials = [
    {
      name: 'Sarah Johnson',
      role: 'Software Engineer',
      content: 'Future Foundry helped me transition from marketing to tech. The AI predictions were spot-on!',
      rating: 5,
    },
    {
      name: 'Michael Chen',
      role: 'Data Scientist',
      content: 'The expert consultations gave me the confidence to pursue my dream career in AI.',
      rating: 5,
    },
    {
      name: 'Emily Rodriguez',
      role: 'UX Designer',
      content: 'Amazing platform! The community support made all the difference in my career journey.',
      rating: 5,
    },
  ];

  const stats = [
    { number: '10,000+', label: 'Students Guided' },
    { number: '95%', label: 'Success Rate' },
    { number: '500+', label: 'Career Paths' },
    { number: '50+', label: 'Expert Mentors' },
  ];

  return (
    <div className="home">
      {/* Hero Section */}
      <section className="hero">
        <div className="container">
          <div className="hero-content">
            <motion.div
              className="hero-text"
              initial={{ opacity: 0, y: 50 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8 }}
            >
              <h1 className="hero-title">
                Discover Your Perfect
                <span className="text-gradient"> Career Path</span>
              </h1>
              <p className="hero-description">
                Unlock your potential with AI-powered career predictions, expert guidance, 
                and a supportive community. Start your journey to professional success today.
              </p>
              <div className="hero-actions">
                <Link to="/career-predictor" className="btn btn-primary">
                  Get Career Prediction
                  <ArrowRight size={20} />
                </Link>
                <Link to="/about" className="btn btn-secondary">
                  Learn More
                </Link>
              </div>
            </motion.div>
            
            <motion.div
              className="hero-visual"
              initial={{ opacity: 0, scale: 0.8 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.8, delay: 0.2 }}
            >
              <div className="hero-image">
                <div className="floating-element element-1">
                  <Brain size={40} />
                </div>
                <div className="floating-element element-2">
                  <TrendingUp size={32} />
                </div>
                <div className="floating-element element-3">
                  <Award size={36} />
                </div>
                <div className="hero-gradient-bg"></div>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="stats">
        <div className="container">
          <div className="stats-grid">
            {stats.map((stat, index) => (
              <motion.div
                key={index}
                className="stat-item"
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                viewport={{ once: true }}
              >
                <div className="stat-number">{stat.number}</div>
                <div className="stat-label">{stat.label}</div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="features">
        <div className="container">
          <motion.div
            className="section-header"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            viewport={{ once: true }}
          >
            <h2>Why Choose Future Foundry?</h2>
            <p>Comprehensive tools and expert guidance to shape your professional future</p>
          </motion.div>

          <div className="features-grid">
            {features.map((feature, index) => {
              const Icon = feature.icon;
              return (
                <motion.div
                  key={index}
                  className="feature-card card"
                  initial={{ opacity: 0, y: 30 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  viewport={{ once: true }}
                  whileHover={{ y: -8 }}
                >
                  <div className="feature-icon">
                    <Icon size={32} />
                  </div>
                  <h3 className="feature-title">{feature.title}</h3>
                  <p className="feature-description">{feature.description}</p>
                </motion.div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="testimonials">
        <div className="container">
          <motion.div
            className="section-header"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            viewport={{ once: true }}
          >
            <h2>Success Stories</h2>
            <p>Hear from professionals who transformed their careers with Future Foundry</p>
          </motion.div>

          <div className="testimonials-grid">
            {testimonials.map((testimonial, index) => (
              <motion.div
                key={index}
                className="testimonial-card card"
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                viewport={{ once: true }}
                whileHover={{ y: -4 }}
              >
                <div className="testimonial-rating">
                  {[...Array(testimonial.rating)].map((_, i) => (
                    <Star key={i} size={16} fill="currentColor" />
                  ))}
                </div>
                <p className="testimonial-content">"{testimonial.content}"</p>
                <div className="testimonial-author">
                  <div className="author-info">
                    <div className="author-name">{testimonial.name}</div>
                    <div className="author-role">{testimonial.role}</div>
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="cta">
        <div className="container">
          <motion.div
            className="cta-content"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            viewport={{ once: true }}
          >
            <h2 className="cta-title">Ready to Shape Your Future?</h2>
            <p className="cta-description">
              Join thousands of professionals who have discovered their ideal career path
            </p>
            <div className="cta-actions">
              <Link to="/career-predictor" className="btn btn-primary">
                Start Your Journey
                <ArrowRight size={20} />
              </Link>
            </div>
          </motion.div>
        </div>
      </section>
    </div>
  );
};

export default Home;
