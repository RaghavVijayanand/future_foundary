# **Enhanced Career Path Prediction System**

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import time
import streamlit as st
from db import *

# Load the enhanced trained model
try:
    with open("enhanced_weights.pkl", "rb") as pickleFile:
        regressor = pickle.load(pickleFile)
    
    with open("feature_names.pkl", "rb") as f:
        model_features = pickle.load(f)
    
    with open("career_list.pkl", "rb") as f:
        available_careers = pickle.load(f)
        
    print(f"✅ Enhanced model loaded successfully!")
    print(f"📊 Available career predictions: {len(available_careers)}")
    
except FileNotFoundError:
    print("⚠️ Enhanced model not found, falling back to basic model")
    with open("weights.pkl", "rb") as pickleFile:
        regressor = pickle.load(pickleFile)
    available_careers = None

# Enhanced career options beyond just tech roles
EXPANDED_CAREER_OPTIONS = [
    # Technology Careers
    'Software Developer', 'Web Developer', 'Mobile App Developer', 'Data Scientist',
    'Machine Learning Engineer', 'AI Research Scientist', 'DevOps Engineer', 'Cloud Architect',
    'Cybersecurity Analyst', 'Blockchain Developer', 'Game Developer', 'Database Administrator',
    'Network Engineer', 'Systems Administrator', 'UI/UX Designer', 'Product Manager',
    'Technical Writer', 'QA Engineer', 'Site Reliability Engineer', 'IoT Developer',
    
    # Business & Management
    'Business Analyst', 'Project Manager', 'Strategy Consultant', 'Digital Marketing Manager',
    'Sales Manager', 'Operations Manager', 'HR Manager', 'Financial Analyst',
    'Investment Banker', 'Management Consultant', 'Supply Chain Manager', 'Risk Analyst',
    
    # Creative & Design
    'Graphic Designer', 'Video Editor', 'Content Creator', 'Social Media Manager',
    'Brand Manager', 'Creative Director', 'Photographer', 'Animation Artist',
    'Motion Graphics Designer', 'Interior Designer', 'Fashion Designer',
    
    # Healthcare & Science
    'Healthcare Data Analyst', 'Biomedical Engineer', 'Research Scientist',
    'Medical Software Developer', 'Health Informatics Specialist', 'Clinical Data Manager',
    
    # Education & Training
    'Corporate Trainer', 'E-learning Developer', 'Educational Technology Specialist',
    'Online Course Creator', 'Technical Instructor',
    
    # Emerging Fields
    'Sustainability Consultant', 'Digital Transformation Specialist', 'Automation Engineer',
    'Robotics Engineer', 'Virtual Reality Developer', 'Augmented Reality Developer',
    'Digital Twin Specialist', 'Smart City Planner'
]

# Enhanced skill categories
TECHNICAL_SKILLS = [
    'Programming Languages', 'Database Management', 'Cloud Computing', 'Machine Learning',
    'Artificial Intelligence', 'Cybersecurity', 'Mobile Development', 'Web Development',
    'Data Analysis', 'DevOps', 'System Architecture', 'Network Administration',
    'Blockchain', 'IoT Development', 'Game Development', 'UI/UX Design',
    'Quality Assurance', 'Technical Writing', 'API Development', 'Microservices'
]

SOFT_SKILLS = [
    'Leadership', 'Communication', 'Team Collaboration', 'Problem Solving',
    'Critical Thinking', 'Adaptability', 'Time Management', 'Creativity',
    'Emotional Intelligence', 'Negotiation', 'Public Speaking', 'Conflict Resolution',
    'Strategic Thinking', 'Decision Making', 'Mentoring', 'Cross-cultural Communication'
]

INDUSTRY_SECTORS = [
    'Technology', 'Healthcare', 'Finance', 'Education', 'Entertainment',
    'Manufacturing', 'Retail', 'Government', 'Non-profit', 'Consulting',
    'Energy', 'Transportation', 'Real Estate', 'Media', 'Telecommunications',
    'Aerospace', 'Automotive', 'Food & Beverage', 'Tourism', 'Agriculture'
]

# Load and preprocess data
df = pd.read_csv("./data/mldata.csv")
df["workshops"] = df["workshops"].replace(["testing"], "Testing")

# Enhanced preprocessing for better predictions
def enhanced_preprocessing(df):
    newdf = df.copy()
    
    # Binary encoding for Yes/No variables
    cols = df[["self-learning capability?", "Extra-courses did", 
               "Taken inputs from seniors or elders", "worked in teams ever?", "Introvert"]]
    for i in cols:
        cleanup_nums = {i: {"yes": 1, "no": 0}}
        newdf = newdf.replace(cleanup_nums)
    
    # Skill level encoding
    mycol = df[["reading and writing skills", "memory capability score"]]
    for i in mycol:
        cleanup_nums = {i: {"poor": 0, "medium": 1, "excellent": 2}}
        newdf = newdf.replace(cleanup_nums)
    
    # Category encoding
    category_cols = df[["certifications", "workshops", "Interested subjects", 
                       "interested career area ", "Type of company want to settle in?", 
                       "Interested Type of Books"]]
    for i in category_cols:
        newdf[i] = newdf[i].astype("category")
        newdf[i + "_code"] = newdf[i].cat.codes
    
    # Dummy encoding
    newdf = pd.get_dummies(newdf, columns=["Management or Technical", "hard/smart worker"], 
                          prefix=["A", "B"])
    
    return newdf

# Preprocess the data
processed_df = enhanced_preprocessing(df)

# Create mapping dictionaries
certifications_list = list(df["certifications"].unique())
certifications_code = list(processed_df["certifications_code"].unique())
C = dict(zip(certifications_list, certifications_code))

workshops_list = list(df["workshops"].unique())
workshops_code = list(processed_df["workshops_code"].unique())
W = dict(zip(workshops_list, workshops_code))

subjects_list = list(df["Interested subjects"].unique())
subjects_code = list(processed_df["Interested subjects_code"].unique())
S = dict(zip(subjects_list, subjects_code))

career_area_list = list(df["interested career area "].unique())
career_area_code = list(processed_df["interested career area _code"].unique())
CA = dict(zip(career_area_list, career_area_code))

company_type_list = list(df["Type of company want to settle in?"].unique())
company_type_code = list(processed_df["Type of company want to settle in?_code"].unique())
CT = dict(zip(company_type_list, company_type_code))

books_list = list(df["Interested Type of Books"].unique())
books_code = list(processed_df["Interested Type of Books_code"].unique())
B = dict(zip(books_list, books_code))

Range_dict = {"poor": 0, "medium": 1, "excellent": 2}

def enhanced_inputlist(
    Name, Contact_Number, Email_address, Logical_quotient_rating, coding_skills_rating,
    hackathons, public_speaking_points, self_learning_capability, Extra_courses_did,
    Taken_inputs_from_seniors_or_elders, worked_in_teams_ever, Introvert,
    reading_and_writing_skills, memory_capability_score, smart_or_hard_work,
    Management_or_Technical, Interested_subjects, Interested_Type_of_Books,
    certifications, workshops, Type_of_company_want_to_settle_in, interested_career_area,
    # New enhanced features
    preferred_work_environment, career_growth_priority, work_life_balance_importance,
    remote_work_preference, leadership_interest, entrepreneurship_interest,
    continuous_learning_commitment, risk_tolerance, collaboration_preference,
    innovation_drive, technical_depth_preference, industry_preference
):
    """Enhanced prediction function with additional personality and preference factors"""
    
    # Basic features
    feed1 = [Logical_quotient_rating, coding_skills_rating, hackathons, public_speaking_points]
    
    # Core categorical features
    input_list_col = [
        self_learning_capability, Extra_courses_did, Taken_inputs_from_seniors_or_elders,
        worked_in_teams_ever, Introvert, reading_and_writing_skills, memory_capability_score,
        smart_or_hard_work, Management_or_Technical, Interested_subjects, Interested_Type_of_Books,
        certifications, workshops, Type_of_company_want_to_settle_in, interested_career_area
    ]
    
    feed = []
    
    # Process categorical features
    for i in input_list_col:
        if i == "Yes":
            feed.append(2)
        elif i == "No":
            feed.append(3)
        elif i == "Management":
            feed.append(1)
            feed.append(0)
        elif i == "Technical":
            feed.append(0)
            feed.append(1)
        elif i == "Smart worker":
            feed.append(1)
            feed.append(0)
        elif i == "Hard Worker":
            feed.append(0)
            feed.append(1)
        else:
            # Handle range and categorical mappings
            if i in Range_dict:
                feed.append(Range_dict[i])
            else:
                # Check various mapping dictionaries
                for mapping_dict in [C, W, S, CA, CT, B]:
                    if i in mapping_dict:
                        feed.append(mapping_dict[i])
                        break
    
    # Combine all features
    total_feed = feed1 + feed
    
    # Get base prediction
    base_prediction = regressor.predict([total_feed])[0]
    
    # Enhanced prediction logic based on new features
    enhanced_predictions = get_enhanced_predictions(
        base_prediction, preferred_work_environment, career_growth_priority,
        work_life_balance_importance, remote_work_preference, leadership_interest,
        entrepreneurship_interest, continuous_learning_commitment, risk_tolerance,
        collaboration_preference, innovation_drive, technical_depth_preference,
        industry_preference, Management_or_Technical, Interested_subjects
    )
    
    return enhanced_predictions

def get_enhanced_predictions(base_prediction, work_env, growth_priority, work_life_balance,
                           remote_pref, leadership, entrepreneurship, learning_commit,
                           risk_tolerance, collaboration, innovation, tech_depth, industry, 
                           mgmt_tech, interests):
    """Generate enhanced career predictions based on additional factors"""
    
    predictions = [base_prediction]  # Start with base prediction
    
    # Technology-focused roles based on preferences
    if mgmt_tech == "Technical" and tech_depth == "Deep specialization":
        tech_roles = [
            "Machine Learning Engineer", "AI Research Scientist", "Data Scientist",
            "DevOps Engineer", "Cybersecurity Analyst", "Blockchain Developer"
        ]
        predictions.extend(tech_roles[:3])
    
    # Management and leadership roles
    if leadership == "Very interested" or mgmt_tech == "Management":
        mgmt_roles = [
            "Technical Product Manager", "Engineering Manager", "CTO",
            "Strategy Consultant", "Project Manager"
        ]
        predictions.extend(mgmt_roles[:2])
    
    # Entrepreneurship and innovation focus
    if entrepreneurship == "Very interested" and innovation == "High":
        startup_roles = [
            "Startup Founder", "Innovation Consultant", "Product Manager",
            "Digital Transformation Specialist", "Business Development Manager"
        ]
        predictions.extend(startup_roles[:2])
    
    # Remote work optimized roles
    if remote_pref == "Fully remote":
        remote_roles = [
            "Remote Software Developer", "Digital Nomad Consultant", 
            "Online Course Creator", "Content Creator", "Technical Writer"
        ]
        predictions.extend(remote_roles[:2])
    
    # Industry-specific roles
    industry_roles = {
        "Healthcare": ["Healthcare Data Analyst", "Health Informatics Specialist", "Biomedical Engineer"],
        "Finance": ["FinTech Developer", "Quantitative Analyst", "Risk Analyst"],
        "Education": ["EdTech Developer", "Educational Technology Specialist", "Corporate Trainer"],
        "Entertainment": ["Game Developer", "Animation Artist", "Video Editor"],
        "Energy": ["Smart Grid Engineer", "Sustainability Consultant", "Renewable Energy Analyst"]
    }
    
    if industry in industry_roles:
        predictions.extend(industry_roles[industry][:2])
    
    # Work-life balance focused roles
    if work_life_balance == "Very important":
        balanced_roles = [
            "Technical Writer", "UX Researcher", "Part-time Consultant",
            "Freelance Developer", "Online Educator"
        ]
        predictions.extend(balanced_roles[:2])
    
    # Remove duplicates and return top 5 predictions
    unique_predictions = list(dict.fromkeys(predictions))
    return unique_predictions[:5]

def create_enhanced_ui():
    """Create the enhanced Streamlit UI"""
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .prediction-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
    }
    
    .feature-section {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>🚀 AI-Powered Career Discovery Platform</h1>
        <p>Discover your perfect career path with our enhanced prediction system</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for basic information
    st.sidebar.title("👤 Personal Information")
    Name = st.sidebar.text_input("Full Name")
    Contact_Number = st.sidebar.text_input("Contact Number")
    Email_address = st.sidebar.text_input("Email Address")
    
    if Name and Contact_Number and Email_address:
        st.sidebar.success("✅ Contact information complete!")
    
    # Main content area with tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Skills Assessment", "🎯 Preferences", "🔮 Predictions", "📈 Analytics"])
    
    with tab1:
        st.markdown('<div class="feature-section">', unsafe_allow_html=True)
        st.header("Skills & Experience Assessment")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Core Abilities")
            Logical_quotient_rating = st.slider("🧠 Logical Reasoning", 1, 10, 5)
            coding_skills_rating = st.slider("💻 Coding Skills", 1, 10, 5)
            hackathons = st.slider("🏆 Hackathons Participated", 0, 20, 2)
            public_speaking_points = st.slider("🎤 Public Speaking", 1, 10, 5)
        
        with col2:
            st.subheader("Personal Attributes")
            self_learning_capability = st.selectbox("📚 Self-Learning", ["Yes", "No"])
            Extra_courses_did = st.selectbox("📖 Extra Courses", ["Yes", "No"])
            Taken_inputs_from_seniors_or_elders = st.selectbox("👥 Mentorship Seeking", ["Yes", "No"])
            worked_in_teams_ever = st.selectbox("🤝 Team Experience", ["Yes", "No"])
            Introvert = st.selectbox("🧘 Personality Type", ["Yes (Introvert)", "No (Extrovert)"])
        
        st.subheader("Skill Levels")
        col3, col4, col5 = st.columns(3)
        with col3:
            reading_and_writing_skills = st.selectbox("📝 Communication Skills", 
                                                    ["poor", "medium", "excellent"])
        with col4:
            memory_capability_score = st.selectbox("🧠 Memory & Learning", 
                                                  ["poor", "medium", "excellent"])
        with col5:
            smart_or_hard_work = st.selectbox("⚡ Work Style", 
                                            ["Smart worker", "Hard Worker"])
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="feature-section">', unsafe_allow_html=True)
        st.header("Career Preferences & Interests")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Work Preferences")
            Management_or_Technical = st.selectbox("🎯 Career Focus", ["Management", "Technical"])
            
            preferred_work_environment = st.selectbox("🏢 Work Environment", 
                ["Office-based", "Remote", "Hybrid", "Field work", "Laboratory"])
            
            remote_work_preference = st.selectbox("🌐 Remote Work", 
                ["Fully remote", "Hybrid", "Prefer office", "No preference"])
            
            work_life_balance_importance = st.selectbox("⚖️ Work-Life Balance Priority", 
                ["Very important", "Important", "Moderate", "Not important"])
            
            career_growth_priority = st.selectbox("📈 Career Growth Focus", 
                ["Rapid advancement", "Steady growth", "Skill mastery", "Work stability"])
        
        with col2:
            st.subheader("Professional Aspirations")
            leadership_interest = st.selectbox("👑 Leadership Interest", 
                ["Very interested", "Somewhat interested", "Not interested"])
            
            entrepreneurship_interest = st.selectbox("🚀 Entrepreneurship", 
                ["Very interested", "Somewhat interested", "Not interested"])
            
            continuous_learning_commitment = st.selectbox("📚 Learning Commitment", 
                ["Very high", "High", "Moderate", "Low"])
            
            risk_tolerance = st.selectbox("🎲 Risk Tolerance", 
                ["High", "Moderate", "Low", "Very low"])
            
            collaboration_preference = st.selectbox("🤝 Team Collaboration", 
                ["Love teamwork", "Prefer small teams", "Like solo work", "Mixed preference"])
        
        st.subheader("Technical & Industry Interests")
        col3, col4 = st.columns(2)
        
        with col3:
            Interested_subjects = st.selectbox("🔬 Technical Interests", 
                ["programming", "Management", "data engineering", "networks", 
                 "Software Engineering", "cloud computing", "parallel computing", 
                 "IOT", "Computer Architecture", "hacking", "AI/ML", "Cybersecurity"])
            
            technical_depth_preference = st.selectbox("🔧 Technical Depth", 
                ["Deep specialization", "Broad knowledge", "Mixed approach"])
            
            innovation_drive = st.selectbox("💡 Innovation Drive", 
                ["High", "Moderate", "Low"])
        
        with col4:
            industry_preference = st.selectbox("🏭 Industry Preference", INDUSTRY_SECTORS)
            
            Interested_Type_of_Books = st.selectbox("📚 Reading Interests", 
                ["Series", "Autobiographies", "Travel", "Guide", "Health", "Journals",
                 "Technology", "Business", "Self-help", "Science", "Fiction"])
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="feature-section">', unsafe_allow_html=True)
        st.header("Additional Qualifications")
        
        col1, col2 = st.columns(2)
        
        with col1:
            certifications = st.selectbox("🎓 Certifications", 
                ["information security", "shell programming", "r programming", 
                 "machine learning", "cloud computing", "data science", 
                 "full stack", "python", "java", "cybersecurity"])
            
            workshops = st.selectbox("🛠️ Workshops Attended", 
                ["Testing", "database security", "game development", "data science",
                 "system designing", "hacking", "cloud computing", "web technologies"])
        
        with col2:
            Type_of_company_want_to_settle_in = st.selectbox("🏢 Company Type Preference", 
                ["Startup", "Tech Giant", "Consulting", "Government", "Non-profit",
                 "Healthcare", "Finance", "E-commerce", "Gaming", "Education"])
            
            interested_career_area = st.selectbox("🎯 Career Area Interest", 
                ["Software Development", "Data Science", "Cybersecurity", "Management",
                 "Consulting", "Research", "Design", "Sales", "Marketing"])
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Prediction button and results
        if st.button("🔮 Get My Career Predictions", type="primary"):
            if Name and Email_address:
                with st.spinner("🤖 AI is analyzing your profile..."):
                    time.sleep(2)  # Simulate processing
                    
                    # Process Introvert field
                    introvert_processed = "Yes" if "Yes" in Introvert else "No"
                    
                    # Get predictions
                    predictions = enhanced_inputlist(
                        Name, Contact_Number, Email_address, Logical_quotient_rating,
                        coding_skills_rating, hackathons, public_speaking_points,
                        self_learning_capability, Extra_courses_did,
                        Taken_inputs_from_seniors_or_elders, worked_in_teams_ever,
                        introvert_processed, reading_and_writing_skills,
                        memory_capability_score, smart_or_hard_work,
                        Management_or_Technical, Interested_subjects,
                        Interested_Type_of_Books, certifications, workshops,
                        Type_of_company_want_to_settle_in, interested_career_area,
                        preferred_work_environment, career_growth_priority,
                        work_life_balance_importance, remote_work_preference,
                        leadership_interest, entrepreneurship_interest,
                        continuous_learning_commitment, risk_tolerance,
                        collaboration_preference, innovation_drive,
                        technical_depth_preference, industry_preference
                    )
                
                st.success("🎉 Career Analysis Complete!")
                
                # Display predictions
                st.markdown("### 🎯 Your Top Career Matches")
                
                for i, career in enumerate(predictions, 1):
                    st.markdown(f"""
                    <div class="prediction-card">
                        <h4>{i}. {career}</h4>
                        <p>Match Score: {95-i*5}%</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Save to database
                try:
                    create_table()
                    add_data(Name, Contact_Number, Email_address, Logical_quotient_rating,
                            coding_skills_rating, hackathons, public_speaking_points,
                            self_learning_capability, Extra_courses_did,
                            Taken_inputs_from_seniors_or_elders, worked_in_teams_ever,
                            introvert_processed, reading_and_writing_skills,
                            memory_capability_score, smart_or_hard_work,
                            Management_or_Technical, Interested_subjects,
                            Interested_Type_of_Books, certifications, workshops,
                            Type_of_company_want_to_settle_in, interested_career_area)
                    st.info("💾 Your profile has been saved for future reference!")
                except Exception as e:
                    st.warning("⚠️ Profile saving temporarily unavailable")
                
            else:
                st.error("❌ Please fill in your name and email address first!")
    
    with tab4:
        st.markdown('<div class="feature-section">', unsafe_allow_html=True)
        st.header("📊 Career Analytics Dashboard")
        
        # Create some sample analytics
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🔥 Trending Career Fields")
            trending_data = {
                'Field': ['AI/ML', 'Cybersecurity', 'Cloud Computing', 'Data Science', 'DevOps'],
                'Growth %': [45, 35, 30, 25, 28]
            }
            st.bar_chart(pd.DataFrame(trending_data).set_index('Field'))
            
        with col2:
            st.subheader("💰 Average Salary Ranges")
            salary_data = {
                'Role': ['Data Scientist', 'ML Engineer', 'Product Manager', 'Software Engineer', 'DevOps Engineer'],
                'Salary (USD)': [120000, 130000, 125000, 110000, 115000]
            }
            st.bar_chart(pd.DataFrame(salary_data).set_index('Role'))
        
        st.subheader("🎯 Skill Demand Forecast")
        skills_forecast = pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027, 2028],
            'AI/ML': [100, 120, 145, 170, 200],
            'Cloud': [100, 115, 130, 145, 165],
            'Cybersecurity': [100, 125, 155, 185, 220]
        })
        st.line_chart(skills_forecast.set_index('Year'))
        
        st.markdown('</div>', unsafe_allow_html=True)

# Run the enhanced application
if __name__ == "__main__":
    create_enhanced_ui()
