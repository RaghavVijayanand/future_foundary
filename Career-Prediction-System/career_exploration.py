"""
Career Exploration and Skill Gap Analysis Module
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Career categories and their associated skills
CAREER_CATEGORIES = {
    "Software Development": {
        "careers": ["Software Developer", "Full Stack Developer", "Backend Developer", "Frontend Developer"],
        "skills": ["Programming", "Problem Solving", "System Design", "Testing", "Version Control"],
        "tools": ["Python", "JavaScript", "Git", "Docker", "AWS"],
        "salary_range": "$70k - $150k",
        "growth_rate": "22%"
    },
    "Data Science & AI": {
        "careers": ["Data Scientist", "Machine Learning Engineer", "AI Research Scientist", "Data Engineer"],
        "skills": ["Statistics", "Machine Learning", "Data Visualization", "Python/R", "SQL"],
        "tools": ["Python", "TensorFlow", "Pandas", "Jupyter", "Tableau"],
        "salary_range": "$85k - $180k",
        "growth_rate": "35%"
    },
    "Cybersecurity": {
        "careers": ["Cybersecurity Analyst", "Penetration Tester", "Security Architect", "Incident Response"],
        "skills": ["Network Security", "Risk Assessment", "Cryptography", "Compliance", "Ethical Hacking"],
        "tools": ["Wireshark", "Metasploit", "Nessus", "Kali Linux", "SIEM"],
        "salary_range": "$75k - $160k",
        "growth_rate": "31%"
    },
    "Product Management": {
        "careers": ["Product Manager", "Product Owner", "Strategy Manager", "Innovation Manager"],
        "skills": ["Strategic Thinking", "User Research", "Analytics", "Communication", "Leadership"],
        "tools": ["Jira", "Figma", "Analytics", "A/B Testing", "Roadmapping"],
        "salary_range": "$90k - $170k",
        "growth_rate": "19%"
    },
    "Design & UX": {
        "careers": ["UX Designer", "UI Designer", "Product Designer", "Design Researcher"],
        "skills": ["User Research", "Prototyping", "Visual Design", "Usability Testing", "Design Systems"],
        "tools": ["Figma", "Sketch", "Adobe Creative", "InVision", "Principle"],
        "salary_range": "$65k - $140k",
        "growth_rate": "13%"
    },
    "Cloud & DevOps": {
        "careers": ["DevOps Engineer", "Cloud Architect", "Site Reliability Engineer", "Platform Engineer"],
        "skills": ["Cloud Platforms", "Automation", "CI/CD", "Monitoring", "Infrastructure as Code"],
        "tools": ["AWS", "Docker", "Kubernetes", "Terraform", "Jenkins"],
        "salary_range": "$80k - $165k",
        "growth_rate": "25%"
    }
}

def create_skill_radar_chart(user_skills, required_skills):
    """Create a radar chart comparing user skills to required skills"""
    
    categories = list(required_skills.keys())
    user_values = [user_skills.get(skill, 0) for skill in categories]
    required_values = [required_skills[skill] for skill in categories]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=user_values,
        theta=categories,
        fill='toself',
        name='Your Skills',
        line_color='blue'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=required_values,
        theta=categories,
        fill='toself',
        name='Required Level',
        line_color='red',
        opacity=0.6
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )),
        showlegend=True,
        title="Skill Gap Analysis"
    )
    
    return fig

def create_career_explorer():
    """Create the career exploration interface"""
    
    st.header("🔍 Career Explorer & Skill Gap Analysis")
    
    # Career category selection
    selected_category = st.selectbox(
        "🎯 Select a Career Category to Explore:",
        list(CAREER_CATEGORIES.keys())
    )
    
    if selected_category:
        category_data = CAREER_CATEGORIES[selected_category]
        
        # Display category overview
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("💰 Salary Range", category_data["salary_range"])
        
        with col2:
            st.metric("📈 Growth Rate", category_data["growth_rate"])
        
        with col3:
            st.metric("🎯 Career Options", len(category_data["careers"]))
        
        # Career options in this category
        st.subheader(f"🚀 Careers in {selected_category}")
        
        for i, career in enumerate(category_data["careers"], 1):
            st.markdown(f"**{i}. {career}**")
        
        # Required skills
        st.subheader("🛠️ Key Skills Required")
        skills_cols = st.columns(3)
        for i, skill in enumerate(category_data["skills"]):
            with skills_cols[i % 3]:
                st.markdown(f"• {skill}")
        
        # Tools and technologies
        st.subheader("⚙️ Common Tools & Technologies")
        tools_cols = st.columns(5)
        for i, tool in enumerate(category_data["tools"]):
            with tools_cols[i % 5]:
                st.markdown(f"`{tool}`")
        
        # Skill assessment for gap analysis
        st.subheader("📊 Assess Your Current Skills")
        st.write("Rate your current skill level (1-10 scale):")
        
        user_skills = {}
        skill_cols = st.columns(2)
        
        for i, skill in enumerate(category_data["skills"]):
            with skill_cols[i % 2]:
                user_skills[skill] = st.slider(
                    skill, 
                    min_value=1, 
                    max_value=10, 
                    value=5,
                    key=f"skill_{skill}"
                )
        
        # Required skill levels (example - in real app, these would be data-driven)
        required_skills = {skill: 7 for skill in category_data["skills"]}  # Assume 7/10 required
        
        # Create and display radar chart
        if st.button("📈 Analyze Skill Gap"):
            fig = create_skill_radar_chart(user_skills, required_skills)
            st.plotly_chart(fig, use_container_width=True)
            
            # Gap analysis recommendations
            st.subheader("💡 Personalized Recommendations")
            
            gaps = []
            strengths = []
            
            for skill, required_level in required_skills.items():
                user_level = user_skills[skill]
                gap = required_level - user_level
                
                if gap > 2:
                    gaps.append((skill, gap))
                elif user_level >= required_level:
                    strengths.append(skill)
            
            if gaps:
                st.warning("🎯 **Skills to Focus On:**")
                for skill, gap in sorted(gaps, key=lambda x: x[1], reverse=True):
                    st.write(f"• **{skill}**: Need to improve by {gap} points")
                    
                    # Suggest learning resources
                    if skill == "Programming":
                        st.info("💡 Recommended: Try coding bootcamps, LeetCode, or online courses")
                    elif skill == "Machine Learning":
                        st.info("💡 Recommended: Coursera ML course, Kaggle competitions, hands-on projects")
                    elif skill == "User Research":
                        st.info("💡 Recommended: UX research courses, user interview practice, design thinking workshops")
            
            if strengths:
                st.success("✅ **Your Strengths:**")
                for strength in strengths:
                    st.write(f"• {strength} - You're ready!")
            
            # Career readiness score
            total_gap = sum(gap for _, gap in gaps)
            max_possible_gap = len(required_skills) * 10
            readiness_score = max(0, 100 - (total_gap / max_possible_gap * 100))
            
            st.metric("🎯 Career Readiness Score", f"{readiness_score:.0f}%")
            
            if readiness_score >= 80:
                st.balloons()
                st.success("🎉 You're ready to pursue careers in this field!")
            elif readiness_score >= 60:
                st.info("🚀 You're on the right track! Focus on the key gaps identified.")
            else:
                st.warning("💪 Keep learning! You have a solid foundation to build upon.")

def create_learning_path_generator():
    """Generate personalized learning paths"""
    
    st.header("🎓 Personalized Learning Path Generator")
    
    # User inputs for learning path
    col1, col2 = st.columns(2)
    
    with col1:
        target_career = st.selectbox(
            "🎯 Target Career:",
            ["Data Scientist", "Software Developer", "Product Manager", "UX Designer", 
             "DevOps Engineer", "Cybersecurity Analyst", "AI Engineer"]
        )
        
        current_level = st.selectbox(
            "📊 Current Experience Level:",
            ["Complete Beginner", "Some Experience", "Intermediate", "Advanced"]
        )
    
    with col2:
        time_commitment = st.selectbox(
            "⏰ Weekly Time Commitment:",
            ["5-10 hours", "10-20 hours", "20-30 hours", "30+ hours"]
        )
        
        learning_style = st.selectbox(
            "📚 Preferred Learning Style:",
            ["Video Courses", "Hands-on Projects", "Reading/Books", "Interactive Coding", "Mixed Approach"]
        )
    
    if st.button("🚀 Generate My Learning Path"):
        st.subheader(f"📋 Your Personalized Path to Become a {target_career}")
        
        # Generate learning path based on selections
        learning_path = generate_learning_path(target_career, current_level, time_commitment, learning_style)
        
        for i, phase in enumerate(learning_path, 1):
            with st.expander(f"Phase {i}: {phase['title']} ({phase['duration']})"):
                st.write(f"**Objective:** {phase['objective']}")
                
                st.write("**Skills to Learn:**")
                for skill in phase['skills']:
                    st.write(f"• {skill}")
                
                st.write("**Recommended Resources:**")
                for resource in phase['resources']:
                    st.write(f"• {resource}")
                
                st.write("**Projects to Build:**")
                for project in phase['projects']:
                    st.write(f"• {project}")
                
                if phase.get('milestone'):
                    st.success(f"🎯 **Milestone:** {phase['milestone']}")

def generate_learning_path(career, level, time_commitment, style):
    """Generate a structured learning path"""
    
    # Sample learning paths (in a real app, this would be more sophisticated)
    paths = {
        "Data Scientist": [
            {
                "title": "Foundation Phase",
                "duration": "2-3 months",
                "objective": "Build mathematical and programming foundations",
                "skills": ["Python basics", "Statistics", "Data manipulation with Pandas", "Basic SQL"],
                "resources": ["Python for Data Science Coursera", "Khan Academy Statistics", "Kaggle Learn"],
                "projects": ["Data cleaning project", "Exploratory data analysis", "Basic visualizations"],
                "milestone": "Complete first data analysis project"
            },
            {
                "title": "Machine Learning Phase",
                "duration": "3-4 months",
                "objective": "Learn core ML algorithms and techniques",
                "skills": ["Supervised Learning", "Unsupervised Learning", "Model Evaluation", "Feature Engineering"],
                "resources": ["Andrew Ng's ML Course", "Scikit-learn documentation", "Hands-On ML book"],
                "projects": ["Prediction model", "Classification project", "Clustering analysis"],
                "milestone": "Build and deploy your first ML model"
            },
            {
                "title": "Specialization Phase",
                "duration": "2-3 months",
                "objective": "Develop expertise in specific areas",
                "skills": ["Deep Learning", "NLP or Computer Vision", "Big Data tools", "MLOps"],
                "resources": ["Fast.ai courses", "TensorFlow tutorials", "AWS ML specialty"],
                "projects": ["Deep learning project", "End-to-end ML pipeline", "Portfolio website"],
                "milestone": "Complete capstone project and job applications"
            }
        ],
        "Software Developer": [
            {
                "title": "Programming Fundamentals",
                "duration": "2-3 months", 
                "objective": "Master programming basics and problem-solving",
                "skills": ["Programming language (Python/JavaScript)", "Data structures", "Algorithms", "Version control"],
                "resources": ["FreeCodeCamp", "LeetCode", "Git tutorials", "CS50 course"],
                "projects": ["Calculator app", "To-do list", "Personal website"],
                "milestone": "Solve 50 coding problems"
            },
            {
                "title": "Web Development",
                "duration": "3-4 months",
                "objective": "Build full-stack web applications",
                "skills": ["Frontend (HTML/CSS/JS)", "Backend framework", "Database", "API development"],
                "resources": ["The Odin Project", "MDN Web Docs", "Framework tutorials"],
                "projects": ["Portfolio website", "CRUD application", "API project"],
                "milestone": "Deploy first full-stack application"
            },
            {
                "title": "Advanced Development",
                "duration": "2-3 months",
                "objective": "Learn advanced concepts and best practices",
                "skills": ["Testing", "DevOps basics", "System design", "Code quality"],
                "resources": ["Clean Code book", "Docker tutorials", "System design interviews"],
                "projects": ["Microservices app", "Open source contribution", "System design project"],
                "milestone": "Contribute to open source and start job search"
            }
        ]
    }
    
    return paths.get(career, paths["Software Developer"])

def create_career_comparison_tool():
    """Create a tool to compare different careers"""
    
    st.header("⚖️ Career Comparison Tool")
    
    st.write("Compare up to 3 careers side by side:")
    
    col1, col2, col3 = st.columns(3)
    
    career_options = list(CAREER_CATEGORIES.keys())
    
    with col1:
        career1 = st.selectbox("Career 1:", career_options, key="career1")
    
    with col2:
        career2 = st.selectbox("Career 2:", career_options, key="career2")
    
    with col3:
        career3 = st.selectbox("Career 3:", career_options, key="career3")
    
    if st.button("📊 Compare Careers"):
        careers_to_compare = [career1, career2, career3]
        
        # Create comparison table
        comparison_data = []
        
        for career in careers_to_compare:
            if career:
                data = CAREER_CATEGORIES[career]
                comparison_data.append({
                    "Career Field": career,
                    "Salary Range": data["salary_range"],
                    "Growth Rate": data["growth_rate"],
                    "# of Roles": len(data["careers"]),
                    "Key Skills": ", ".join(data["skills"][:3]) + "...",
                    "Main Tools": ", ".join(data["tools"][:3]) + "..."
                })
        
        if comparison_data:
            df = pd.DataFrame(comparison_data)
            st.table(df)
            
            # Visual comparison
            fig = px.bar(
                df, 
                x="Career Field", 
                y="# of Roles",
                title="Number of Career Options by Field",
                color="Career Field"
            )
            st.plotly_chart(fig, use_container_width=True)

# Add these functions to the main enhanced_app.py tabs
def add_exploration_features_to_app():
    """Add the exploration features to the main app"""
    
    # Add new tabs for exploration features
    tab5, tab6, tab7 = st.tabs(["🔍 Career Explorer", "🎓 Learning Paths", "⚖️ Compare Careers"])
    
    with tab5:
        create_career_explorer()
    
    with tab6:
        create_learning_path_generator()
    
    with tab7:
        create_career_comparison_tool()
