import React from 'react';
import { motion } from 'framer-motion';
import { Users, Star, Calendar, Clock } from 'lucide-react';

const Expert = () => {
  const experts = [
    {
      id: 1,
      name: 'Dr. Emily Rodriguez',
      title: 'Senior Data Scientist at Google',
      specialties: ['Data Science', 'Machine Learning', 'Career Transition'],
      rating: 4.9,
      reviews: 156,
      experience: '10+ years',
      price: '$150/hour',
      image: '/api/placeholder/150/150',
      bio: 'PhD in Computer Science with extensive experience in AI and ML. Helped 200+ professionals transition to data science.',
    },
    {
      id: 2,
      name: 'Michael Chen',
      title: 'VP of Engineering at Microsoft',
      specialties: ['Software Engineering', 'Technical Leadership', 'System Design'],
      rating: 4.8,
      reviews: 203,
      experience: '15+ years',
      price: '$200/hour',
      image: '/api/placeholder/150/150',
      bio: 'Former startup founder turned tech executive. Expert in scaling engineering teams and technical strategy.',
    },
    {
      id: 3,
      name: 'Sarah Kim',
      title: 'Product Manager at Apple',
      specialties: ['Product Management', 'Strategy', 'User Experience'],
      rating: 4.9,
      reviews: 128,
      experience: '8+ years',
      price: '$120/hour',
      image: '/api/placeholder/150/150',
      bio: 'Led product development for consumer apps with millions of users. Passionate about mentoring aspiring PMs.',
    },
  ];

  return (
    <div className="expert">
      <div className="container">
        <motion.div
          className="page-header"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
        >
          <Users size={40} className="page-icon" />
          <h1>Expert Consultation</h1>
          <p>Get personalized guidance from industry experts and experienced professionals</p>
        </motion.div>

        <div className="experts-grid">
          {experts.map((expert, index) => (
            <motion.div
              key={expert.id}
              className="expert-card card"
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
            >
              <div className="expert-header">
                <div className="expert-avatar">
                  <img src={expert.image} alt={expert.name} />
                </div>
                <div className="expert-basic-info">
                  <h3 className="expert-name">{expert.name}</h3>
                  <p className="expert-title">{expert.title}</p>
                  <div className="expert-rating">
                    <Star size={16} fill="currentColor" />
                    <span>{expert.rating}</span>
                    <span className="reviews-count">({expert.reviews} reviews)</span>
                  </div>
                </div>
              </div>

              <div className="expert-details">
                <p className="expert-bio">{expert.bio}</p>
                
                <div className="expert-specialties">
                  <h4>Specialties</h4>
                  <div className="specialties-tags">
                    {expert.specialties.map((specialty, i) => (
                      <span key={i} className="specialty-tag">{specialty}</span>
                    ))}
                  </div>
                </div>

                <div className="expert-meta">
                  <div className="meta-item">
                    <Clock size={16} />
                    <span>{expert.experience}</span>
                  </div>
                  <div className="meta-item price">
                    <span className="price-label">Starting from</span>
                    <span className="price-value">{expert.price}</span>
                  </div>
                </div>
              </div>

              <div className="expert-actions">
                <button className="btn btn-secondary">
                  <Calendar size={20} />
                  View Schedule
                </button>
                <button className="btn btn-primary">
                  Book Session
                </button>
              </div>
            </motion.div>
          ))}
        </div>

        <motion.div
          className="cta-section"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.4 }}
        >
          <h2>Become an Expert</h2>
          <p>Share your expertise and help others while earning money</p>
          <button className="btn btn-primary">Apply as Expert</button>
        </motion.div>
      </div>
    </div>
  );
};

export default Expert;
