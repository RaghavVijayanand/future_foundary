import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Brain, Send, RotateCcw, Download, TrendingUp } from 'lucide-react';

const CareerPredictor = () => {
  const [formData, setFormData] = useState({
    // Academic Performance
    logical_quotient_rating: 7,
    hackathons: 2,
    coding_skills_rating: 6,
    public_speaking_points: 5,
    
    // Skills & Interests
    self_learning_capability: 'yes',
    extra_courses: 'yes',
    taken_inputs_from_seniors: 'yes',
    worked_in_teams: 'yes',
    introvert: 'no',
    
    // Additional Information
    interested_subjects: '',
    interested_career_area: '',
    type_of_company_want_to_settle_in: '',
    
    // Ratings (1-10)
    reading_and_writing_skills: 7,
    memory_capability_score: 8,
    interested_type_of_books: '',
    management_or_technical: 'technical',
    hard_smart_worker: 'smart worker',
    salary_expectation: 'moderate',
  });

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSliderChange = (name, value) => {
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    // Simulate API call to your career prediction model
    try {
      // This would normally call your FastAPI/Flask backend
      // For now, we'll simulate the prediction
      setTimeout(() => {
        const mockPredictions = [
          {
            career: 'Data Scientist',
            probability: 0.85,
            description: 'High aptitude for analytical thinking and problem-solving',
            skills_needed: ['Python', 'Machine Learning', 'Statistics', 'SQL'],
            growth_rate: '22%'
          },
          {
            career: 'Software Engineer',
            probability: 0.78,
            description: 'Strong coding skills and logical reasoning abilities',
            skills_needed: ['Programming', 'Algorithms', 'System Design', 'Databases'],
            growth_rate: '18%'
          },
          {
            career: 'Product Manager',
            probability: 0.72,
            description: 'Good balance of technical and management skills',
            skills_needed: ['Leadership', 'Strategic Thinking', 'Communication', 'Analytics'],
            growth_rate: '15%'
          }
        ];
        
        setPrediction(mockPredictions);
        setLoading(false);
      }, 2000);
    } catch (error) {
      console.error('Error getting prediction:', error);
      setLoading(false);
    }
  };

  const resetForm = () => {
    setFormData({
      logical_quotient_rating: 7,
      hackathons: 2,
      coding_skills_rating: 6,
      public_speaking_points: 5,
      self_learning_capability: 'yes',
      extra_courses: 'yes',
      taken_inputs_from_seniors: 'yes',
      worked_in_teams: 'yes',
      introvert: 'no',
      interested_subjects: '',
      interested_career_area: '',
      type_of_company_want_to_settle_in: '',
      reading_and_writing_skills: 7,
      memory_capability_score: 8,
      interested_type_of_books: '',
      management_or_technical: 'technical',
      hard_smart_worker: 'smart worker',
      salary_expectation: 'moderate',
    });
    setPrediction(null);
  };

  return (
    <div className="career-predictor">
      <div className="container">
        <motion.div
          className="page-header"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
        >
          <Brain size={40} className="page-icon" />
          <h1>AI Career Predictor</h1>
          <p>
            Discover your ideal career path using our advanced machine learning algorithm.
            Fill out the form below to get personalized career recommendations.
          </p>
        </motion.div>

        <div className="predictor-content">
          <motion.div
            className="predictor-form-container"
            initial={{ opacity: 0, x: -30 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            <form onSubmit={handleSubmit} className="predictor-form">
              <div className="form-section">
                <h3>Academic Performance</h3>
                
                <div className="form-group">
                  <label className="form-label">
                    Logical Quotient Rating (1-10)
                    <span className="rating-value">{formData.logical_quotient_rating}</span>
                  </label>
                  <input
                    type="range"
                    name="logical_quotient_rating"
                    min="1"
                    max="10"
                    value={formData.logical_quotient_rating}
                    onChange={(e) => handleSliderChange('logical_quotient_rating', e.target.value)}
                    className="slider"
                  />
                </div>

                <div className="form-group">
                  <label className="form-label">Number of Hackathons Participated</label>
                  <input
                    type="number"
                    name="hackathons"
                    value={formData.hackathons}
                    onChange={handleInputChange}
                    className="form-input"
                    min="0"
                    max="20"
                  />
                </div>

                <div className="form-group">
                  <label className="form-label">
                    Coding Skills Rating (1-10)
                    <span className="rating-value">{formData.coding_skills_rating}</span>
                  </label>
                  <input
                    type="range"
                    name="coding_skills_rating"
                    min="1"
                    max="10"
                    value={formData.coding_skills_rating}
                    onChange={(e) => handleSliderChange('coding_skills_rating', e.target.value)}
                    className="slider"
                  />
                </div>

                <div className="form-group">
                  <label className="form-label">
                    Public Speaking Points (1-10)
                    <span className="rating-value">{formData.public_speaking_points}</span>
                  </label>
                  <input
                    type="range"
                    name="public_speaking_points"
                    min="1"
                    max="10"
                    value={formData.public_speaking_points}
                    onChange={(e) => handleSliderChange('public_speaking_points', e.target.value)}
                    className="slider"
                  />
                </div>
              </div>

              <div className="form-section">
                <h3>Skills & Personality</h3>
                
                <div className="form-group">
                  <label className="form-label">Self-learning Capability</label>
                  <select
                    name="self_learning_capability"
                    value={formData.self_learning_capability}
                    onChange={handleInputChange}
                    className="form-input"
                  >
                    <option value="yes">Yes</option>
                    <option value="no">No</option>
                  </select>
                </div>

                <div className="form-group">
                  <label className="form-label">Extra Courses Taken</label>
                  <select
                    name="extra_courses"
                    value={formData.extra_courses}
                    onChange={handleInputChange}
                    className="form-input"
                  >
                    <option value="yes">Yes</option>
                    <option value="no">No</option>
                  </select>
                </div>

                <div className="form-group">
                  <label className="form-label">Taken Inputs from Seniors</label>
                  <select
                    name="taken_inputs_from_seniors"
                    value={formData.taken_inputs_from_seniors}
                    onChange={handleInputChange}
                    className="form-input"
                  >
                    <option value="yes">Yes</option>
                    <option value="no">No</option>
                  </select>
                </div>

                <div className="form-group">
                  <label className="form-label">Worked in Teams</label>
                  <select
                    name="worked_in_teams"
                    value={formData.worked_in_teams}
                    onChange={handleInputChange}
                    className="form-input"
                  >
                    <option value="yes">Yes</option>
                    <option value="no">No</option>
                  </select>
                </div>

                <div className="form-group">
                  <label className="form-label">Are you an Introvert?</label>
                  <select
                    name="introvert"
                    value={formData.introvert}
                    onChange={handleInputChange}
                    className="form-input"
                  >
                    <option value="no">No</option>
                    <option value="yes">Yes</option>
                  </select>
                </div>
              </div>

              <div className="form-section">
                <h3>Preferences & Interests</h3>
                
                <div className="form-group">
                  <label className="form-label">Interested Subjects</label>
                  <input
                    type="text"
                    name="interested_subjects"
                    value={formData.interested_subjects}
                    onChange={handleInputChange}
                    className="form-input"
                    placeholder="e.g., Computer Science, Mathematics, Physics"
                  />
                </div>

                <div className="form-group">
                  <label className="form-label">Interested Career Area</label>
                  <input
                    type="text"
                    name="interested_career_area"
                    value={formData.interested_career_area}
                    onChange={handleInputChange}
                    className="form-input"
                    placeholder="e.g., Technology, Healthcare, Finance"
                  />
                </div>

                <div className="form-group">
                  <label className="form-label">Type of Company</label>
                  <select
                    name="type_of_company_want_to_settle_in"
                    value={formData.type_of_company_want_to_settle_in}
                    onChange={handleInputChange}
                    className="form-input"
                  >
                    <option value="">Select Company Type</option>
                    <option value="startup">Startup</option>
                    <option value="mid-size">Mid-size Company</option>
                    <option value="large">Large Corporation</option>
                    <option value="government">Government</option>
                    <option value="nonprofit">Non-profit</option>
                  </select>
                </div>

                <div className="form-group">
                  <label className="form-label">Management or Technical</label>
                  <select
                    name="management_or_technical"
                    value={formData.management_or_technical}
                    onChange={handleInputChange}
                    className="form-input"
                  >
                    <option value="technical">Technical</option>
                    <option value="management">Management</option>
                    <option value="both">Both</option>
                  </select>
                </div>
              </div>

              <div className="form-actions">
                <button
                  type="button"
                  onClick={resetForm}
                  className="btn btn-secondary"
                >
                  <RotateCcw size={20} />
                  Reset Form
                </button>
                <button
                  type="submit"
                  disabled={loading}
                  className="btn btn-primary"
                >
                  {loading ? (
                    <div className="loading-spinner"></div>
                  ) : (
                    <>
                      <Send size={20} />
                      Get Prediction
                    </>
                  )}
                </button>
              </div>
            </form>
          </motion.div>

          {/* Results Section */}
          {prediction && (
            <motion.div
              className="prediction-results"
              initial={{ opacity: 0, x: 30 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6 }}
            >
              <div className="results-header">
                <h3>Your Career Predictions</h3>
                <p>Based on your inputs, here are your top career matches:</p>
              </div>

              <div className="predictions-list">
                {prediction.map((pred, index) => (
                  <motion.div
                    key={index}
                    className="prediction-card card"
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.4, delay: index * 0.1 }}
                  >
                    <div className="prediction-header">
                      <h4 className="career-title">{pred.career}</h4>
                      <div className="probability-badge">
                        {Math.round(pred.probability * 100)}% Match
                      </div>
                    </div>
                    
                    <p className="career-description">{pred.description}</p>
                    
                    <div className="career-details">
                      <div className="growth-rate">
                        <TrendingUp size={16} />
                        <span>Growth Rate: {pred.growth_rate}</span>
                      </div>
                      
                      <div className="skills-needed">
                        <strong>Skills to Develop:</strong>
                        <div className="skills-tags">
                          {pred.skills_needed.map((skill, skillIndex) => (
                            <span key={skillIndex} className="skill-tag">
                              {skill}
                            </span>
                          ))}
                        </div>
                      </div>
                    </div>
                  </motion.div>
                ))}
              </div>

              <div className="results-actions">
                <button className="btn btn-primary">
                  <Download size={20} />
                  Download Report
                </button>
              </div>
            </motion.div>
          )}
        </div>
      </div>
    </div>
  );
};

export default CareerPredictor;
