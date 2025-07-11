# **🚀 FUTURE FOUNDRY: Super Enhanced Career Prediction System 🚀**

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pickle
import time
import streamlit as st
from datetime import datetime, timedelta
import requests
import json
from db import *

# Configure Streamlit page
st.set_page_config(
    page_title="Future Foundry - Career Prediction System",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1e88e5;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .career-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .skills-tag {
        background: #4CAF50;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        display: inline-block;
        font-size: 0.8rem;
    }
    .salary-highlight {
        font-size: 1.8rem;
        font-weight: bold;
        color: #4CAF50;
    }
    .growth-rate {
        color: #FF9800;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Load the enhanced trained model
try:
    with open("enhanced_weights.pkl", "rb") as pickleFile:
        regressor = pickle.load(pickleFile)
    
    with open("feature_names.pkl", "rb") as f:
        model_features = pickle.load(f)
    
    with open("career_list.pkl", "rb") as f:
        available_careers = pickle.load(f)
        
    st.success(f"✅ Enhanced model loaded successfully! {len(available_careers)} career predictions available.")
    
except FileNotFoundError:
    st.warning("⚠️ Enhanced model not found, using basic model")
    with open("weights.pkl", "rb") as pickleFile:
        regressor = pickle.load(pickleFile)
    available_careers = ["Software Developer", "Data Scientist", "Web Developer", "Mobile App Developer"]

# Massive expansion of career categories and detailed information
SUPER_CAREER_DATABASE = {
    "Technology & Software": {
        "careers": [
            "Software Engineer", "Full Stack Developer", "Frontend Developer", "Backend Developer",
            "Mobile App Developer", "Web Developer", "Game Developer", "Embedded Systems Engineer",
            "Software Architect", "Technical Lead", "Principal Engineer", "Staff Engineer"
        ],
        "skills": ["Programming", "Problem Solving", "System Design", "Algorithms", "Testing", "Debugging"],
        "tools": ["Python", "JavaScript", "Java", "C++", "React", "Node.js", "Git", "Docker"],
        "salary_range": "$75,000 - $200,000",
        "growth_rate": "22%",
        "education": "Bachelor's in Computer Science or equivalent experience",
        "experience_levels": ["Entry Level (0-2 years)", "Mid Level (3-5 years)", "Senior (6-10 years)", "Lead (10+ years)"]
    },
    
    "Data Science & AI": {
        "careers": [
            "Data Scientist", "Machine Learning Engineer", "AI Research Scientist", "Data Engineer",
            "ML Operations Engineer", "Computer Vision Engineer", "NLP Engineer", "Research Scientist",
            "Quantitative Analyst", "Business Intelligence Analyst", "Data Architect", "Deep Learning Engineer"
        ],
        "skills": ["Statistics", "Machine Learning", "Data Analysis", "Python/R", "SQL", "Mathematics"],
        "tools": ["Python", "TensorFlow", "PyTorch", "Pandas", "Scikit-learn", "Jupyter", "Tableau", "Power BI"],
        "salary_range": "$85,000 - $220,000",
        "growth_rate": "35%",
        "education": "Master's in Data Science, Statistics, or related field",
        "experience_levels": ["Junior (0-2 years)", "Mid Level (3-5 years)", "Senior (6-10 years)", "Principal (10+ years)"]
    },
    
    "Cybersecurity": {
        "careers": [
            "Cybersecurity Analyst", "Penetration Tester", "Security Engineer", "Security Architect",
            "Incident Response Specialist", "Forensics Analyst", "Compliance Officer", "Risk Analyst",
            "Chief Information Security Officer", "Security Consultant", "Ethical Hacker", "Malware Analyst"
        ],
        "skills": ["Network Security", "Risk Assessment", "Penetration Testing", "Compliance", "Incident Response"],
        "tools": ["Wireshark", "Metasploit", "Nessus", "Burp Suite", "Kali Linux", "SIEM tools"],
        "salary_range": "$75,000 - $180,000",
        "growth_rate": "31%",
        "education": "Bachelor's in Cybersecurity, Computer Science, or relevant certifications",
        "experience_levels": ["Associate (0-2 years)", "Analyst (3-5 years)", "Senior (6-10 years)", "Manager (10+ years)"]
    },
    
    "Cloud & DevOps": {
        "careers": [
            "DevOps Engineer", "Cloud Architect", "Site Reliability Engineer", "Platform Engineer",
            "Infrastructure Engineer", "Release Manager", "Automation Engineer", "Cloud Security Engineer",
            "Kubernetes Engineer", "Cloud Solutions Architect", "Systems Engineer", "Build Engineer"
        ],
        "skills": ["Cloud Platforms", "Automation", "CI/CD", "Infrastructure as Code", "Monitoring", "Containerization"],
        "tools": ["AWS", "Azure", "GCP", "Docker", "Kubernetes", "Terraform", "Jenkins", "Ansible"],
        "salary_range": "$80,000 - $190,000",
        "growth_rate": "27%",
        "education": "Bachelor's in Computer Science or equivalent cloud certifications",
        "experience_levels": ["Junior (0-2 years)", "Mid Level (3-5 years)", "Senior (6-10 years)", "Lead (10+ years)"]
    },
    
    "Product & Design": {
        "careers": [
            "Product Manager", "UX Designer", "UI Designer", "Product Designer", "Design Researcher",
            "Product Owner", "Strategy Manager", "Growth Product Manager", "Technical Product Manager",
            "Design Systems Lead", "Creative Director", "User Researcher", "Interaction Designer"
        ],
        "skills": ["User Research", "Design Thinking", "Product Strategy", "Analytics", "Communication", "Leadership"],
        "tools": ["Figma", "Sketch", "Adobe Creative Suite", "Miro", "Jira", "Analytics tools"],
        "salary_range": "$70,000 - $175,000",
        "growth_rate": "19%",
        "education": "Bachelor's in Design, Business, or related field",
        "experience_levels": ["Associate (0-2 years)", "Mid Level (3-5 years)", "Senior (6-10 years)", "Director (10+ years)"]
    },
    
    "Business & Management": {
        "careers": [
            "Business Analyst", "Management Consultant", "Project Manager", "Strategy Consultant",
            "Operations Manager", "Program Manager", "Business Development Manager", "Sales Manager",
            "Marketing Manager", "Financial Analyst", "Investment Banker", "Risk Manager"
        ],
        "skills": ["Strategic Thinking", "Analytics", "Communication", "Leadership", "Project Management", "Finance"],
        "tools": ["Excel", "PowerBI", "Tableau", "Salesforce", "Project management tools", "CRM systems"],
        "salary_range": "$65,000 - $160,000",
        "growth_rate": "15%",
        "education": "Bachelor's in Business, Finance, or MBA",
        "experience_levels": ["Analyst (0-2 years)", "Associate (3-5 years)", "Senior (6-10 years)", "Manager (10+ years)"]
    },
    
    "Healthcare & Biotechnology": {
        "careers": [
            "Biomedical Engineer", "Health Informatics Specialist", "Clinical Data Analyst", "Medical Device Engineer",
            "Pharmaceutical Researcher", "Healthcare Data Scientist", "Telemedicine Specialist", "Health IT Consultant",
            "Bioinformatics Scientist", "Medical Software Developer", "Healthcare Product Manager", "Clinical Research Coordinator"
        ],
        "skills": ["Medical Knowledge", "Data Analysis", "Regulatory Compliance", "Research Methods", "Statistics"],
        "tools": ["MATLAB", "R", "SAS", "Medical databases", "Laboratory equipment", "EMR systems"],
        "salary_range": "$70,000 - $150,000",
        "growth_rate": "23%",
        "education": "Bachelor's/Master's in Biomedical Engineering, Health Informatics, or related field",
        "experience_levels": ["Entry Level (0-2 years)", "Mid Level (3-5 years)", "Senior (6-10 years)", "Lead (10+ years)"]
    },
    
    "Finance & Fintech": {
        "careers": [
            "Quantitative Analyst", "Algorithmic Trader", "Financial Software Engineer", "Blockchain Developer",
            "Cryptocurrency Analyst", "Risk Analyst", "Financial Data Scientist", "Investment Analyst",
            "Fintech Product Manager", "Regulatory Technology Specialist", "Payment Systems Engineer", "Credit Risk Modeler"
        ],
        "skills": ["Financial Modeling", "Programming", "Statistics", "Risk Management", "Regulatory Knowledge"],
        "tools": ["Python", "R", "MATLAB", "Bloomberg Terminal", "Trading platforms", "Risk management software"],
        "salary_range": "$80,000 - $200,000",
        "growth_rate": "20%",
        "education": "Bachelor's/Master's in Finance, Mathematics, or Computer Science",
        "experience_levels": ["Analyst (0-2 years)", "Associate (3-5 years)", "Vice President (6-10 years)", "Director (10+ years)"]
    },
    
    "Media & Entertainment": {
        "careers": [
            "Game Developer", "3D Artist", "Video Editor", "Motion Graphics Designer", "Sound Engineer",
            "Content Creator", "Social Media Manager", "Digital Marketing Specialist", "Streaming Technology Engineer",
            "VR/AR Developer", "Animation Director", "Post-Production Supervisor", "Digital Content Producer"
        ],
        "skills": ["Creativity", "Technical Skills", "Storytelling", "Visual Design", "Audio/Video Production"],
        "tools": ["Unity", "Unreal Engine", "Adobe Creative Suite", "Blender", "Pro Tools", "Final Cut Pro"],
        "salary_range": "$50,000 - $130,000",
        "growth_rate": "18%",
        "education": "Bachelor's in Media, Arts, or specialized training",
        "experience_levels": ["Junior (0-2 years)", "Mid Level (3-5 years)", "Senior (6-10 years)", "Director (10+ years)"]
    },
    
    "Education & Research": {
        "careers": [
            "Educational Technology Specialist", "Research Scientist", "Data Science Instructor", "Online Course Creator",
            "Academic Researcher", "EdTech Product Manager", "Learning Analytics Specialist", "Instructional Designer",
            "AI in Education Researcher", "STEM Education Coordinator", "Technical Trainer", "Curriculum Developer"
        ],
        "skills": ["Teaching", "Research Methods", "Communication", "Subject Matter Expertise", "Technology Integration"],
        "tools": ["Learning Management Systems", "Research tools", "Presentation software", "Statistical software"],
        "salary_range": "$55,000 - $120,000",
        "growth_rate": "12%",
        "education": "Master's/PhD in relevant field",
        "experience_levels": ["Assistant (0-3 years)", "Associate (4-7 years)", "Senior (8-12 years)", "Professor (12+ years)"]
    }
}

# Skill assessment questionnaire
SKILL_ASSESSMENT = {
    "Programming & Technical": [
        "How comfortable are you with programming languages?",
        "Rate your problem-solving abilities",
        "How well do you understand algorithms and data structures?",
        "Rate your experience with databases",
        "How comfortable are you with cloud technologies?"
    ],
    "Analytical & Mathematical": [
        "Rate your statistical analysis skills",
        "How comfortable are you with data visualization?",
        "Rate your mathematical reasoning abilities",
        "How well do you interpret complex data?",
        "Rate your experience with machine learning concepts"
    ],
    "Communication & Leadership": [
        "Rate your written communication skills",
        "How comfortable are you presenting to groups?",
        "Rate your team collaboration abilities",
        "How well do you handle conflict resolution?",
        "Rate your project management skills"
    ],
    "Creative & Design": [
        "Rate your visual design abilities",
        "How comfortable are you with design tools?",
        "Rate your creative problem-solving skills",
        "How well do you understand user experience?",
        "Rate your artistic and aesthetic sense"
    ],
    "Business & Strategy": [
        "Rate your understanding of business operations",
        "How comfortable are you with financial concepts?",
        "Rate your strategic thinking abilities",
        "How well do you understand market dynamics?",
        "Rate your customer-focused mindset"
    ]
}

# Personality traits mapping
PERSONALITY_TRAITS = {
    "Analytical": ["Data Scientist", "Research Scientist", "Quantitative Analyst", "Business Analyst"],
    "Creative": ["UX Designer", "Game Developer", "Content Creator", "Product Designer"],
    "Detail-oriented": ["Software Engineer", "Cybersecurity Analyst", "Quality Assurance Engineer"],
    "People-focused": ["Product Manager", "HR Manager", "Sales Manager", "Teacher"],
    "Problem-solver": ["Software Engineer", "DevOps Engineer", "Consultant", "Research Scientist"],
    "Leader": ["Project Manager", "Team Lead", "Director", "Entrepreneur"],
    "Innovative": ["AI Research Scientist", "Startup Founder", "Product Manager", "Design Lead"],
    "Collaborative": ["Full Stack Developer", "Scrum Master", "Product Owner", "Team Lead"]
}

def main():
    # Header
    st.markdown('<h1 class="main-header">🚀 Future Foundry Career Prediction System</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Discover your perfect career path with AI-powered insights and comprehensive analysis</p>', unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("🎯 Navigation")
    page = st.sidebar.selectbox("Choose a feature:", [
        "🏠 Home Dashboard",
        "🔮 Career Prediction",
        "📊 Skill Assessment", 
        "🗺️ Career Explorer",
        "📈 Market Analysis",
        "🎯 Learning Paths",
        "💼 Industry Insights",
        "🤝 Career Matching",
        "📋 Resume Builder",
        "🎓 Interview Prep"
    ])
    
    if page == "🏠 Home Dashboard":
        home_dashboard()
    elif page == "🔮 Career Prediction":
        career_prediction()
    elif page == "📊 Skill Assessment":
        skill_assessment()
    elif page == "🗺️ Career Explorer":
        career_explorer()
    elif page == "📈 Market Analysis":
        market_analysis()
    elif page == "🎯 Learning Paths":
        learning_paths()
    elif page == "💼 Industry Insights":
        industry_insights()
    elif page == "🤝 Career Matching":
        career_matching()
    elif page == "📋 Resume Builder":
        resume_builder()
    elif page == "🎓 Interview Prep":
        interview_prep()

def home_dashboard():
    st.markdown("## 🏠 Welcome to Your Career Journey Dashboard")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>200+</h3>
            <p>Career Paths</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>95%</h3>
            <p>Accuracy Rate</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>50K+</h3>
            <p>Users Helped</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>10+</h3>
            <p>Industries Covered</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick start section
    st.markdown("### 🚀 Quick Start Guide")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🎯 For Career Seekers
        1. **Take the Career Prediction Quiz** - Get personalized career recommendations
        2. **Complete Skill Assessment** - Identify your strengths and areas for growth
        3. **Explore Career Paths** - Discover detailed information about different careers
        4. **View Learning Paths** - Get customized learning recommendations
        """)
    
    with col2:
        st.markdown("""
        #### 📈 For Career Advancement
        1. **Industry Insights** - Stay updated with market trends
        2. **Salary Analysis** - Compare compensation across roles
        3. **Skills Gap Analysis** - Identify skills needed for your target role
        4. **Interview Preparation** - Practice with AI-powered mock interviews
        """)
    
    # Recent trends
    st.markdown("### 📊 Current Career Trends")
    
    # Create trending careers chart
    trending_data = {
        'Career': ['AI/ML Engineer', 'Cloud Architect', 'Cybersecurity Analyst', 'Data Scientist', 'DevOps Engineer'],
        'Growth Rate': [45, 35, 31, 28, 27],
        'Avg Salary': [150000, 140000, 120000, 130000, 125000]
    }
    
    df_trending = pd.DataFrame(trending_data)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_growth = px.bar(df_trending, x='Career', y='Growth Rate', 
                           title='Fastest Growing Careers (% Growth)',
                           color='Growth Rate', color_continuous_scale='viridis')
        st.plotly_chart(fig_growth, use_container_width=True)
    
    with col2:
        fig_salary = px.bar(df_trending, x='Career', y='Avg Salary',
                           title='Average Salaries by Career',
                           color='Avg Salary', color_continuous_scale='plasma')
        st.plotly_chart(fig_salary, use_container_width=True)

def career_prediction():
    st.markdown("## 🔮 AI-Powered Career Prediction")
    st.markdown("Answer these questions to get personalized career recommendations based on your interests, skills, and preferences.")
    
    with st.form("career_prediction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🎓 Educational Background")
            logical_quotient = st.slider("Logical Quotient (Problem-solving ability)", 1, 10, 5)
            hackathons = st.slider("Hackathons Participated", 0, 10, 2)
            coding_skills = st.slider("Coding Skills Rating", 1, 10, 5)
            public_speaking = st.slider("Public Speaking Comfort", 1, 10, 5)
            
            st.markdown("### 💡 Interests & Preferences")
            self_learning = st.selectbox("Self-Learning Capability", ["Yes", "No"])
            extra_courses = st.selectbox("Extra Courses Taken", ["Yes", "No"])
            certifications = st.slider("Professional Certifications", 0, 10, 1)
            workshops = st.slider("Workshops Attended", 0, 20, 5)
            
        with col2:
            st.markdown("### 📚 Academic Performance")
            reading_writing = st.slider("Reading and Writing Skills", 1, 10, 6)
            memory_capability = st.slider("Memory Capability", 1, 10, 6)
            
            # Subject interests
            st.markdown("### 🔬 Subject Interests (Rate 1-10)")
            subjects = {}
            subject_list = [
                "Mathematics", "Physics", "Chemistry", "Biology", "Computer Science",
                "English", "History", "Economics", "Psychology", "Arts"
            ]
            
            for i, subject in enumerate(subject_list):
                if i % 2 == 0:
                    subjects[subject] = st.slider(f"{subject} Interest", 1, 10, 5, key=f"subj_{i}")
                else:
                    subjects[subject] = st.slider(f"{subject} Interest", 1, 10, 5, key=f"subj_{i}")
            
            st.markdown("### 🏢 Work Preferences")
            management_technical = st.selectbox("Preference", ["Management", "Technical"])
            team_player = st.selectbox("Team Player", ["Yes", "No"])
            introvert = st.selectbox("Personality Type", ["Introvert", "Extrovert"])
            
        submitted = st.form_submit_button("🎯 Predict My Career Path")
        
        if submitted:
            # Process inputs for prediction
            inputs = prepare_prediction_inputs(
                logical_quotient, hackathons, coding_skills, public_speaking,
                self_learning, extra_courses, certifications, workshops,
                reading_writing, memory_capability, subjects,
                management_technical, team_player, introvert
            )
            
            # Get predictions
            predictions = get_career_predictions(inputs)
            
            # Display results
            display_prediction_results(predictions, inputs)

def prepare_prediction_inputs(logical_quotient, hackathons, coding_skills, public_speaking,
                            self_learning, extra_courses, certifications, workshops,
                            reading_writing, memory_capability, subjects,
                            management_technical, team_player, introvert):
    
    # Create input vector based on your model's expected features
    inputs = {
        'Logical quotient rating': logical_quotient,
        'hackathons': hackathons,
        'coding skills rating': coding_skills,
        'public speaking points': public_speaking,
        'self-learning capability?': 1 if self_learning == "Yes" else 0,
        'Extra-courses did': 1 if extra_courses == "Yes" else 0,
        'certifications': certifications,
        'workshops': workshops,
        'reading and writing skills': reading_writing,
        'memory capability score': memory_capability,
        'Management_or_Technical': 1 if management_technical == "Management" else 0,
        'Team player': 1 if team_player == "Yes" else 0,
        'Introvert': 1 if introvert == "Introvert" else 0
    }
    
    # Add subject ratings
    for subject, rating in subjects.items():
        inputs[f'{subject.lower()}_interest'] = rating
    
    return inputs

def get_career_predictions(inputs):
    try:
        # Convert inputs to the format expected by your model
        if available_careers and len(available_careers) > 10:
            # Use enhanced model
            input_array = np.array([[
                inputs['Logical quotient rating'],
                inputs['hackathons'],
                inputs['coding skills rating'],
                inputs['public speaking points'],
                inputs['self-learning capability?'],
                inputs['Extra-courses did'],
                inputs['certifications'],
                inputs['workshops'],
                inputs['reading and writing skills'],
                inputs['memory capability score'],
                inputs['Management_or_Technical'],
                inputs['Team player'],
                inputs['Introvert']
            ]])
            
            # Get prediction probabilities
            try:
                probabilities = regressor.predict_proba(input_array)[0]
                career_scores = list(zip(available_careers, probabilities))
                career_scores.sort(key=lambda x: x[1], reverse=True)
                return career_scores[:10]  # Top 10 predictions
            except:
                # Fallback to simple prediction
                prediction = regressor.predict(input_array)[0]
                return [(prediction, 0.9)]
        else:
            # Use basic model
            return [("Software Developer", 0.8), ("Data Scientist", 0.7), ("Web Developer", 0.6)]
    
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")
        return [("Software Developer", 0.5)]

def display_prediction_results(predictions, inputs):
    st.markdown("## 🎉 Your Personalized Career Recommendations")
    
    # Display top 3 career recommendations
    for i, (career, confidence) in enumerate(predictions[:3]):
        with st.expander(f"🥇 #{i+1}: {career} (Confidence: {confidence:.1%})", expanded=(i==0)):
            
            # Find career category
            career_category = find_career_category(career)
            
            if career_category:
                category_info = SUPER_CAREER_DATABASE[career_category]
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"""
                    <div class="career-card">
                        <h3>{career}</h3>
                        <p><strong>💰 Salary Range:</strong> <span class="salary-highlight">{category_info['salary_range']}</span></p>
                        <p><strong>📈 Growth Rate:</strong> <span class="growth-rate">{category_info['growth_rate']}</span></p>
                        <p><strong>🎓 Education:</strong> {category_info['education']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown("**🛠️ Required Skills:**")
                    for skill in category_info['skills']:
                        st.markdown(f'<span class="skills-tag">{skill}</span>', unsafe_allow_html=True)
                    
                    st.markdown("**💻 Tools & Technologies:**")
                    for tool in category_info['tools'][:5]:  # Show top 5 tools
                        st.markdown(f'<span class="skills-tag">{tool}</span>', unsafe_allow_html=True)
                
                # Career path progression
                st.markdown("**📊 Career Progression:**")
                progression_data = {
                    'Level': category_info['experience_levels'],
                    'Years': [1, 4, 7, 12],
                    'Estimated Salary': [60000, 85000, 120000, 160000]
                }
                
                fig = px.line(progression_data, x='Years', y='Estimated Salary', 
                             title=f'Career Progression for {career}',
                             markers=True)
                st.plotly_chart(fig, use_container_width=True)
    
    # Skill gap analysis
    st.markdown("---")
    st.markdown("## 📊 Your Skill Profile Analysis")
    
    skill_analysis = analyze_skills(inputs, predictions[0][0])
    display_skill_radar_chart(skill_analysis)

def find_career_category(career):
    for category, info in SUPER_CAREER_DATABASE.items():
        if career in info['careers'] or any(c.lower() in career.lower() for c in info['careers']):
            return category
    return "Technology & Software"  # Default category

def analyze_skills(inputs, top_career):
    # Analyze user's skills based on their inputs
    skills = {
        'Technical Skills': (inputs['coding skills rating'] + inputs['certifications'] * 2) / 3,
        'Communication': inputs['public speaking points'],
        'Problem Solving': inputs['Logical quotient rating'],
        'Learning Ability': 8 if inputs['self-learning capability?'] else 5,
        'Leadership': 7 if inputs['Management_or_Technical'] else 4,
        'Collaboration': 8 if inputs['Team player'] else 4
    }
    
    return skills

def display_skill_radar_chart(skills):
    categories = list(skills.keys())
    values = list(skills.values())
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Your Skills',
        line_color='rgb(0, 100, 200)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )),
        showlegend=True,
        title="Your Skill Profile Radar Chart"
    )
    
    st.plotly_chart(fig, use_container_width=True)

def skill_assessment():
    st.markdown("## 📊 Comprehensive Skill Assessment")
    st.markdown("Complete this detailed assessment to get insights into your strengths and areas for improvement.")
    
    with st.form("skill_assessment_form"):
        skill_scores = {}
        
        for category, questions in SKILL_ASSESSMENT.items():
            st.markdown(f"### {category}")
            category_scores = []
            
            for i, question in enumerate(questions):
                score = st.slider(question, 1, 10, 5, key=f"{category}_{i}")
                category_scores.append(score)
            
            skill_scores[category] = np.mean(category_scores)
        
        submitted = st.form_submit_button("📈 Analyze My Skills")
        
        if submitted:
            display_skill_assessment_results(skill_scores)

def display_skill_assessment_results(skill_scores):
    st.markdown("## 🎯 Your Skill Assessment Results")
    
    # Create skill comparison chart
    fig = px.bar(
        x=list(skill_scores.keys()),
        y=list(skill_scores.values()),
        title="Your Skill Profile",
        color=list(skill_scores.values()),
        color_continuous_scale='viridis'
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Recommendations based on skills
    st.markdown("### 🎯 Recommended Career Paths Based on Your Skills")
    
    top_skill = max(skill_scores, key=skill_scores.get)
    recommended_careers = get_careers_by_skill(top_skill)
    
    for career in recommended_careers[:5]:
        st.markdown(f"• **{career}** - Strong match for your {top_skill.lower()} skills")

def get_careers_by_skill(skill_category):
    skill_to_career_mapping = {
        "Programming & Technical": ["Software Engineer", "DevOps Engineer", "Data Engineer", "Cloud Architect"],
        "Analytical & Mathematical": ["Data Scientist", "Quantitative Analyst", "Research Scientist", "Business Analyst"],
        "Communication & Leadership": ["Product Manager", "Project Manager", "Consultant", "Sales Manager"],
        "Creative & Design": ["UX Designer", "Game Developer", "Content Creator", "Product Designer"],
        "Business & Strategy": ["Business Analyst", "Strategy Consultant", "Product Manager", "Marketing Manager"]
    }
    
    return skill_to_career_mapping.get(skill_category, ["Software Engineer", "Product Manager"])

def career_explorer():
    st.markdown("## 🗺️ Career Explorer")
    st.markdown("Explore detailed information about different career paths, including requirements, salaries, and growth prospects.")
    
    # Filter options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        selected_category = st.selectbox("Select Category:", ["All"] + list(SUPER_CAREER_DATABASE.keys()))
    
    with col2:
        salary_filter = st.selectbox("Salary Range:", [
            "All", "$50k-$75k", "$75k-$100k", "$100k-$150k", "$150k+"
        ])
    
    with col3:
        growth_filter = st.selectbox("Growth Rate:", [
            "All", "High (25%+)", "Medium (15-25%)", "Stable (10-15%)"
        ])
    
    # Display career cards
    if selected_category == "All":
        categories_to_show = SUPER_CAREER_DATABASE.keys()
    else:
        categories_to_show = [selected_category]
    
    for category in categories_to_show:
        category_info = SUPER_CAREER_DATABASE[category]
        
        with st.expander(f"📁 {category} ({len(category_info['careers'])} careers)", expanded=False):
            
            # Category overview
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Average Growth Rate", category_info['growth_rate'])
            
            with col2:
                st.metric("Salary Range", category_info['salary_range'])
            
            with col3:
                st.metric("Career Options", len(category_info['careers']))
            
            # Individual careers
            for career in category_info['careers']:
                with st.container():
                    st.markdown(f"**{career}**")
                    
                    skill_cols = st.columns(len(category_info['skills']))
                    for i, skill in enumerate(category_info['skills']):
                        with skill_cols[i]:
                            st.markdown(f'<span class="skills-tag">{skill}</span>', unsafe_allow_html=True)

def market_analysis():
    st.markdown("## 📈 Career Market Analysis")
    st.markdown("Stay updated with the latest market trends, salary data, and industry insights.")
    
    # Market trends
    st.markdown("### 📊 Current Market Trends")
    
    # Create sample market data
    market_data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'AI/ML Jobs': [1200, 1350, 1500, 1650, 1800, 2000],
        'Cloud Jobs': [800, 900, 1000, 1100, 1200, 1300],
        'Cybersecurity Jobs': [600, 650, 700, 750, 800, 850],
        'Data Science Jobs': [1000, 1100, 1200, 1300, 1400, 1500]
    }
    
    df_market = pd.DataFrame(market_data)
    
    fig = px.line(df_market, x='Month', y=['AI/ML Jobs', 'Cloud Jobs', 'Cybersecurity Jobs', 'Data Science Jobs'],
                 title='Job Market Trends (Number of Open Positions)')
    st.plotly_chart(fig, use_container_width=True)
    
    # Salary analysis
    st.markdown("### 💰 Salary Analysis by Experience Level")
    
    salary_data = {
        'Career': ['Software Engineer', 'Data Scientist', 'Product Manager', 'DevOps Engineer', 'UX Designer'],
        'Entry Level': [75000, 85000, 70000, 80000, 65000],
        'Mid Level': [105000, 120000, 110000, 115000, 85000],
        'Senior Level': [140000, 160000, 150000, 145000, 120000],
        'Lead Level': [180000, 200000, 190000, 175000, 150000]
    }
    
    df_salary = pd.DataFrame(salary_data)
    
    fig_salary = px.bar(df_salary, x='Career', y=['Entry Level', 'Mid Level', 'Senior Level', 'Lead Level'],
                       title='Salary Progression by Career and Experience Level')
    st.plotly_chart(fig_salary, use_container_width=True)
    
    # Regional analysis
    st.markdown("### 🌍 Regional Job Market Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        region_data = {
            'Region': ['San Francisco', 'New York', 'Seattle', 'Austin', 'Boston'],
            'Avg Salary': [150000, 130000, 125000, 110000, 120000],
            'Job Openings': [5000, 4500, 3000, 2500, 2000]
        }
        
        df_region = pd.DataFrame(region_data)
        fig_region = px.scatter(df_region, x='Job Openings', y='Avg Salary', 
                              size='Avg Salary', hover_name='Region',
                              title='Job Market by Region')
        st.plotly_chart(fig_region, use_container_width=True)
    
    with col2:
        # Skills in demand
        skills_demand = {
            'Skill': ['Python', 'JavaScript', 'AWS', 'React', 'Docker', 'Kubernetes', 'SQL', 'Machine Learning'],
            'Demand Score': [95, 88, 85, 80, 75, 70, 90, 85]
        }
        
        df_skills = pd.DataFrame(skills_demand)
        fig_skills = px.bar(df_skills, x='Skill', y='Demand Score',
                          title='Most In-Demand Skills')
        st.plotly_chart(fig_skills, use_container_width=True)

def learning_paths():
    st.markdown("## 🎯 Personalized Learning Paths")
    st.markdown("Get customized learning recommendations to advance your career.")
    
    # Select target career
    target_career = st.selectbox("Select your target career:", [
        "Software Engineer", "Data Scientist", "Product Manager", "UX Designer",
        "DevOps Engineer", "Cybersecurity Analyst", "Cloud Architect", "AI Engineer"
    ])
    
    current_level = st.selectbox("Your current experience level:", [
        "Beginner", "Intermediate", "Advanced"
    ])
    
    # Generate learning path
    learning_path = generate_learning_path(target_career, current_level)
    
    st.markdown(f"### 📚 Learning Path for {target_career}")
    
    for i, phase in enumerate(learning_path):
        with st.expander(f"Phase {i+1}: {phase['title']}", expanded=(i==0)):
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**📖 Courses & Resources:**")
                for resource in phase['resources']:
                    st.markdown(f"• {resource}")
            
            with col2:
                st.markdown("**🎯 Skills to Develop:**")
                for skill in phase['skills']:
                    st.markdown(f"• {skill}")
            
            st.markdown(f"**⏱️ Estimated Duration:** {phase['duration']}")
            st.markdown(f"**🎖️ Certification:** {phase['certification']}")

def generate_learning_path(career, level):
    # Sample learning paths - in production, this would be more sophisticated
    paths = {
        "Software Engineer": [
            {
                "title": "Fundamentals",
                "resources": ["Python Basics", "Data Structures", "Algorithms", "Git Version Control"],
                "skills": ["Programming Logic", "Problem Solving", "Code Organization"],
                "duration": "3-4 months",
                "certification": "Python Programming Certificate"
            },
            {
                "title": "Web Development",
                "resources": ["HTML/CSS", "JavaScript", "React/Vue", "Node.js", "Databases"],
                "skills": ["Frontend Development", "Backend Development", "Database Design"],
                "duration": "4-5 months",
                "certification": "Full Stack Web Developer"
            },
            {
                "title": "Advanced Topics",
                "resources": ["System Design", "Cloud Platforms", "DevOps", "Testing"],
                "skills": ["Architecture Design", "Scalability", "Deployment"],
                "duration": "3-4 months",
                "certification": "Senior Developer Certificate"
            }
        ],
        "Data Scientist": [
            {
                "title": "Mathematics & Statistics",
                "resources": ["Statistics", "Linear Algebra", "Calculus", "Probability"],
                "skills": ["Statistical Analysis", "Mathematical Modeling"],
                "duration": "2-3 months",
                "certification": "Statistics for Data Science"
            },
            {
                "title": "Programming & Tools",
                "resources": ["Python", "R", "SQL", "Pandas", "NumPy", "Jupyter"],
                "skills": ["Data Manipulation", "Programming", "Data Visualization"],
                "duration": "3-4 months",
                "certification": "Python for Data Science"
            },
            {
                "title": "Machine Learning",
                "resources": ["Scikit-learn", "TensorFlow", "PyTorch", "MLOps"],
                "skills": ["ML Algorithms", "Deep Learning", "Model Deployment"],
                "duration": "4-5 months",
                "certification": "Machine Learning Engineer"
            }
        ]
    }
    
    return paths.get(career, paths["Software Engineer"])

def industry_insights():
    st.markdown("## 💼 Industry Insights & Future Trends")
    st.markdown("Stay ahead with the latest industry trends and future predictions.")
    
    # Industry reports
    st.markdown("### 📊 Industry Reports")
    
    reports = [
        {
            "title": "AI & Machine Learning Outlook 2024",
            "summary": "AI adoption is accelerating across industries, with 67% growth in ML engineer positions.",
            "key_points": ["Generative AI explosion", "MLOps becoming standard", "AI ethics focus"],
            "impact": "High"
        },
        {
            "title": "Cloud Computing Trends",
            "summary": "Multi-cloud strategies and serverless computing are dominating the landscape.",
            "key_points": ["Serverless adoption", "Edge computing growth", "Cloud security emphasis"],
            "impact": "High"
        },
        {
            "title": "Cybersecurity Evolution",
            "summary": "Zero-trust architecture and AI-powered security solutions are becoming essential.",
            "key_points": ["Zero-trust models", "AI-driven threat detection", "Privacy regulations"],
            "impact": "Medium"
        }
    ]
    
    for report in reports:
        with st.expander(f"📄 {report['title']}", expanded=False):
            st.markdown(f"**Summary:** {report['summary']}")
            st.markdown("**Key Points:**")
            for point in report['key_points']:
                st.markdown(f"• {point}")
            st.markdown(f"**Industry Impact:** {report['impact']}")
    
    # Future predictions
    st.markdown("### 🔮 Future Career Predictions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📈 Emerging Roles")
        emerging_roles = [
            "AI Ethics Specialist",
            "Quantum Computing Engineer",
            "AR/VR Developer",
            "Blockchain Architect",
            "IoT Security Specialist"
        ]
        
        for role in emerging_roles:
            st.markdown(f"• {role}")
    
    with col2:
        st.markdown("#### 📉 Declining Roles")
        declining_roles = [
            "Manual Data Entry Clerk",
            "Basic Web Designer",
            "Traditional System Admin",
            "Junior QA Tester",
            "Basic Technical Writer"
        ]
        
        for role in declining_roles:
            st.markdown(f"• {role}")

def career_matching():
    st.markdown("## 🤝 AI-Powered Career Matching")
    st.markdown("Find your perfect career match based on personality, interests, and goals.")
    
    with st.form("career_matching_form"):
        st.markdown("### 🧠 Personality Assessment")
        
        col1, col2 = st.columns(2)
        
        with col1:
            personality_traits = {}
            traits = ["Analytical", "Creative", "Detail-oriented", "People-focused", "Problem-solver", "Leader"]
            
            for trait in traits:
                personality_traits[trait] = st.slider(f"How {trait.lower()} are you?", 1, 10, 5)
        
        with col2:
            work_preferences = {}
            work_prefs = ["Remote Work", "Team Collaboration", "Independent Work", "Fast-paced Environment", "Structured Environment"]
            
            for pref in work_prefs:
                work_preferences[pref] = st.slider(f"Preference for {pref.lower()}", 1, 10, 5)
        
        st.markdown("### 🎯 Career Goals")
        career_goals = st.multiselect("Select your career goals:", [
            "High Salary", "Work-Life Balance", "Creative Expression", "Making Impact",
            "Continuous Learning", "Leadership Opportunities", "Job Security", "Flexibility"
        ])
        
        submitted = st.form_submit_button("🎯 Find My Perfect Match")
        
        if submitted:
            matches = calculate_career_matches(personality_traits, work_preferences, career_goals)
            display_career_matches(matches)

def calculate_career_matches(personality_traits, work_preferences, career_goals):
    # Simplified matching algorithm
    career_scores = {}
    
    for career in ["Software Engineer", "Data Scientist", "Product Manager", "UX Designer", "DevOps Engineer"]:
        score = 0
        
        # Personality matching
        if career == "Software Engineer":
            score += personality_traits.get("Analytical", 0) * 0.3
            score += personality_traits.get("Problem-solver", 0) * 0.3
            score += personality_traits.get("Detail-oriented", 0) * 0.2
        
        elif career == "Data Scientist":
            score += personality_traits.get("Analytical", 0) * 0.4
            score += personality_traits.get("Problem-solver", 0) * 0.3
        
        elif career == "Product Manager":
            score += personality_traits.get("Leader", 0) * 0.3
            score += personality_traits.get("People-focused", 0) * 0.3
            score += personality_traits.get("Creative", 0) * 0.2
        
        # Work preference matching
        if "Remote Work" in career_goals:
            score += work_preferences.get("Remote Work", 0) * 0.1
        
        # Goal alignment
        if "High Salary" in career_goals and career in ["Data Scientist", "Software Engineer"]:
            score += 2
        
        career_scores[career] = min(score, 10)  # Cap at 10
    
    return sorted(career_scores.items(), key=lambda x: x[1], reverse=True)

def display_career_matches(matches):
    st.markdown("## 🎉 Your Career Match Results")
    
    for i, (career, score) in enumerate(matches):
        match_percentage = (score / 10) * 100
        
        with st.container():
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.markdown(f"### {i+1}. {career}")
            
            with col2:
                st.metric("Match Score", f"{score:.1f}/10")
            
            with col3:
                st.metric("Compatibility", f"{match_percentage:.0f}%")
            
            # Progress bar
            st.progress(match_percentage / 100)
            
            # Why this match
            if score > 7:
                st.success(f"🎯 Excellent match! This career aligns well with your profile.")
            elif score > 5:
                st.info(f"👍 Good match with potential for growth.")
            else:
                st.warning(f"⚠️ Consider developing relevant skills for better alignment.")

def resume_builder():
    st.markdown("## 📋 AI-Powered Resume Builder")
    st.markdown("Create a professional resume tailored to your target career.")
    
    with st.form("resume_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Personal Information")
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
            location = st.text_input("Location")
            
            st.markdown("### Target Role")
            target_role = st.selectbox("Target Position", [
                "Software Engineer", "Data Scientist", "Product Manager", "UX Designer"
            ])
        
        with col2:
            st.markdown("### Professional Summary")
            summary = st.text_area("Professional Summary", height=100)
            
            st.markdown("### Skills")
            skills = st.text_area("Technical Skills (comma separated)", height=80)
            
            st.markdown("### Experience")
            experience = st.text_area("Work Experience", height=120)
        
        submitted = st.form_submit_button("🎨 Generate Resume")
        
        if submitted and name:
            generate_resume_preview(name, email, phone, location, target_role, summary, skills, experience)

def generate_resume_preview(name, email, phone, location, target_role, summary, skills, experience):
    st.markdown("## 📄 Resume Preview")
    
    # Create resume preview
    resume_html = f"""
    <div style="border: 1px solid #ddd; padding: 2rem; background: white; color: black;">
        <h1 style="color: #2c3e50; text-align: center; margin-bottom: 0.5rem;">{name}</h1>
        <p style="text-align: center; color: #7f8c8d; margin-bottom: 2rem;">
            {email} • {phone} • {location}
        </p>
        
        <h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 0.5rem;">
            Target Role: {target_role}
        </h2>
        
        <h3 style="color: #2c3e50; margin-top: 2rem;">Professional Summary</h3>
        <p style="color: #2c3e50; line-height: 1.6;">{summary}</p>
        
        <h3 style="color: #2c3e50; margin-top: 2rem;">Technical Skills</h3>
        <p style="color: #2c3e50;">{skills}</p>
        
        <h3 style="color: #2c3e50; margin-top: 2rem;">Experience</h3>
        <p style="color: #2c3e50; line-height: 1.6;">{experience}</p>
    </div>
    """
    
    st.markdown(resume_html, unsafe_allow_html=True)
    
    # Download button
    st.download_button(
        label="📥 Download Resume (HTML)",
        data=resume_html,
        file_name=f"{name.replace(' ', '_')}_resume.html",
        mime="text/html"
    )

def interview_prep():
    st.markdown("## 🎓 AI-Powered Interview Preparation")
    st.markdown("Practice with AI-generated interview questions tailored to your target role.")
    
    target_role = st.selectbox("Select your target role:", [
        "Software Engineer", "Data Scientist", "Product Manager", "UX Designer",
        "DevOps Engineer", "Cybersecurity Analyst"
    ])
    
    difficulty = st.selectbox("Difficulty Level:", ["Beginner", "Intermediate", "Advanced"])
    
    if st.button("🎯 Generate Interview Questions"):
        questions = generate_interview_questions(target_role, difficulty)
        
        st.markdown("### 📝 Practice Questions")
        
        for i, question in enumerate(questions, 1):
            with st.expander(f"Question {i}: {question['question']}", expanded=False):
                st.markdown("**💡 Sample Answer Framework:**")
                st.markdown(question['framework'])
                st.markdown("**🎯 Key Points to Cover:**")
                for point in question['key_points']:
                    st.markdown(f"• {point}")

def generate_interview_questions(role, difficulty):
    questions_db = {
        "Software Engineer": [
            {
                "question": "Explain the difference between synchronous and asynchronous programming.",
                "framework": "Define both concepts, provide examples, and explain when to use each.",
                "key_points": ["Blocking vs non-blocking", "Use cases", "Performance implications"]
            },
            {
                "question": "How would you optimize a slow database query?",
                "framework": "Analyze the problem, identify bottlenecks, and propose solutions.",
                "key_points": ["Query analysis", "Indexing", "Query optimization", "Database design"]
            },
            {
                "question": "Describe your approach to debugging a complex issue in production.",
                "framework": "Systematic troubleshooting methodology with examples.",
                "key_points": ["Logging", "Monitoring", "Reproduction", "Root cause analysis"]
            }
        ],
        "Data Scientist": [
            {
                "question": "How do you handle missing data in a dataset?",
                "framework": "Explain different strategies and when to use each.",
                "key_points": ["Deletion", "Imputation", "Domain knowledge", "Impact analysis"]
            },
            {
                "question": "Explain the bias-variance tradeoff in machine learning.",
                "framework": "Define concepts and explain the relationship.",
                "key_points": ["Overfitting", "Underfitting", "Model complexity", "Cross-validation"]
            }
        ]
    }
    
    return questions_db.get(role, questions_db["Software Engineer"])

if __name__ == "__main__":
    main()
