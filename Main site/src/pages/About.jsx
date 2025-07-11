import React from 'react';
import { motion } from 'framer-motion';
import { Info, Target, Users, Award, TrendingUp } from 'lucide-react';

const About = () => {
  const features = [
    {
      icon: Target,
      title: 'Our Mission',
      description: 'To empower individuals with AI-driven career guidance and connect them with expert mentors to achieve their professional goals.',
    },
    {
      icon: Users,
      title: 'Community Driven',
      description: 'Built by professionals for professionals, fostering a supportive community of career growth and knowledge sharing.',
    },
    {
      icon: Award,
      title: 'Proven Results',
      description: '95% of our users report increased clarity about their career path within 30 days of using our platform.',
    },
    {
      icon: TrendingUp,
      title: 'Continuous Growth',
      description: 'We constantly improve our AI models and expand our expert network to provide the best career guidance.',
    },
  ];

  const team = [
    {
      name: 'Alex Thompson',
      role: 'CEO & Co-founder',
      bio: 'Former Google PM with 10+ years in tech. Passionate about democratizing career guidance.',
    },
    {
      name: 'Dr. Priya Sharma',
      role: 'CTO & AI Lead',
      bio: 'PhD in Machine Learning from MIT. Expert in building AI systems for human-centered applications.',
    },
    {
      name: 'Marcus Johnson',
      role: 'Head of Community',
      bio: 'Career counselor turned community builder. Helped thousands find their ideal career paths.',
    },
  ];

  return (
    <div className="about">
      <div className="container">
        <motion.div
          className="page-header"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
        >
          <Info size={40} className="page-icon" />
          <h1>About Future Foundry</h1>
          <p>Revolutionizing career guidance through AI and human expertise</p>
        </motion.div>

        <motion.section
          className="about-story"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
        >
          <h2>Our Story</h2>
          <p>
            Future Foundry was born from a simple observation: too many talented individuals 
            struggle to find their ideal career path due to lack of personalized guidance and 
            access to industry experts. We combine cutting-edge AI technology with human wisdom 
            to solve this problem.
          </p>
          <p>
            Our platform uses machine learning algorithms trained on thousands of successful 
            career transitions to provide accurate predictions and recommendations. But we don't 
            stop at algorithms – we believe in the power of human connection and mentorship.
          </p>
        </motion.section>

        <section className="about-features">
          <h2>What Makes Us Different</h2>
          <div className="features-grid">
            {features.map((feature, index) => {
              const Icon = feature.icon;
              return (
                <motion.div
                  key={index}
                  className="feature-card card"
                  initial={{ opacity: 0, y: 30 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                >
                  <div className="feature-icon">
                    <Icon size={32} />
                  </div>
                  <h3>{feature.title}</h3>
                  <p>{feature.description}</p>
                </motion.div>
              );
            })}
          </div>
        </section>

        <section className="about-team">
          <h2>Meet Our Team</h2>
          <div className="team-grid">
            {team.map((member, index) => (
              <motion.div
                key={index}
                className="team-member card"
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
              >
                <div className="member-avatar">
                  <img src={`/api/placeholder/120/120`} alt={member.name} />
                </div>
                <h3 className="member-name">{member.name}</h3>
                <p className="member-role">{member.role}</p>
                <p className="member-bio">{member.bio}</p>
              </motion.div>
            ))}
          </div>
        </section>

        <motion.section
          className="about-cta"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.6 }}
        >
          <h2>Join Our Mission</h2>
          <p>
            Whether you're looking for career guidance or want to help others as an expert, 
            we'd love to have you be part of our community.
          </p>
          <div className="cta-actions">
            <button className="btn btn-primary">Get Started</button>
            <button className="btn btn-secondary">Become an Expert</button>
          </div>
        </motion.section>
      </div>
    </div>
  );
};

export default About;
