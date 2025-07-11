"""
Ultimate Career Analytics and Exploration System
Advanced analytics, market insights, and career planning tools
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pickle
import requests
import json
from datetime import datetime, timedelta
import seaborn as sns
import matplotlib.pyplot as plt

class CareerAnalytics:
    def __init__(self):
        self.load_career_data()
        self.setup_market_data()
        
    def load_career_data(self):
        """Load career database and model data"""
        try:
            with open("mega_career_database.pkl", "rb") as f:
                self.career_database = pickle.load(f)
            with open("mega_career_list.pkl", "rb") as f:
                self.all_careers = pickle.load(f)
            print(f"✅ Loaded {len(self.all_careers)} careers from mega database")
        except FileNotFoundError:
            print("⚠️ Mega database not found, using default data")
            self.career_database = self.get_default_database()
            self.all_careers = []
            for careers in self.career_database.values():
                self.all_careers.extend(careers)
    
    def get_default_database(self):
        """Fallback career database"""
        return {
            "Technology & Software": ["Software Engineer", "Web Developer", "Mobile Developer"],
            "Data Science & AI": ["Data Scientist", "ML Engineer", "AI Researcher"],
            "Business & Management": ["Product Manager", "Business Analyst", "Consultant"]
        }
    
    def setup_market_data(self):
        """Setup synthetic market data for analysis"""
        self.market_trends = self.generate_market_trends()
        self.salary_data = self.generate_salary_data()
        self.skills_demand = self.generate_skills_demand()
        self.location_data = self.generate_location_data()

def career_analytics_dashboard():
    """Main analytics dashboard"""
    st.markdown("## 📊 Ultimate Career Analytics Dashboard")
    
    analytics = CareerAnalytics()
    
    # Sidebar filters
    st.sidebar.markdown("### 🎛️ Analytics Filters")
    
    # Career category filter
    categories = ["All"] + list(analytics.career_database.keys())
    selected_category = st.sidebar.selectbox("Category:", categories)
    
    # Time period filter
    time_period = st.sidebar.selectbox("Time Period:", [
        "Last 6 months", "Last year", "Last 2 years", "All time"
    ])
    
    # Analysis type
    analysis_type = st.sidebar.selectbox("Analysis Type:", [
        "Market Overview", "Salary Analysis", "Skills Demand", 
        "Geographic Analysis", "Career Pathways", "Future Trends"
    ])
    
    # Main dashboard content
    if analysis_type == "Market Overview":
        market_overview_analysis(analytics, selected_category, time_period)
    elif analysis_type == "Salary Analysis":
        salary_analysis(analytics, selected_category)
    elif analysis_type == "Skills Demand":
        skills_demand_analysis(analytics)
    elif analysis_type == "Geographic Analysis":
        geographic_analysis(analytics)
    elif analysis_type == "Career Pathways":
        career_pathways_analysis(analytics)
    elif analysis_type == "Future Trends":
        future_trends_analysis(analytics)

def market_overview_analysis(analytics, category, time_period):
    """Comprehensive market overview"""
    st.markdown("### 🌟 Market Overview Analysis")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Job Openings",
            value="125,430",
            delta="15.2% vs last month"
        )
    
    with col2:
        st.metric(
            label="Average Salary Growth",
            value="8.4%",
            delta="2.1% vs last year"
        )
    
    with col3:
        st.metric(
            label="Remote Job %",
            value="67%",
            delta="5% vs last quarter"
        )
    
    with col4:
        st.metric(
            label="Skill Gap Index",
            value="2.3",
            delta="-0.2 vs last month"
        )
    
    # Market trends chart
    st.markdown("#### 📈 Job Market Trends")
    
    trends_data = analytics.market_trends
    fig_trends = px.line(
        trends_data, 
        x='date', 
        y=['AI_ML', 'Cloud', 'Cybersecurity', 'Data_Science', 'Software_Dev'],
        title='Job Posting Trends by Category',
        labels={'value': 'Number of Job Postings', 'date': 'Date'}
    )
    fig_trends.update_layout(height=400)
    st.plotly_chart(fig_trends, use_container_width=True)
    
    # Industry breakdown
    col1, col2 = st.columns(2)
    
    with col1:
        industry_data = {
            'Industry': ['Technology', 'Healthcare', 'Finance', 'Education', 'Manufacturing'],
            'Job_Openings': [45000, 28000, 22000, 15000, 18000],
            'Growth_Rate': [25, 18, 15, 12, 8]
        }
        
        fig_industry = px.scatter(
            industry_data,
            x='Job_Openings',
            y='Growth_Rate',
            size='Job_Openings',
            color='Industry',
            title='Industry Analysis: Jobs vs Growth'
        )
        st.plotly_chart(fig_industry, use_container_width=True)
    
    with col2:
        # Experience level distribution
        exp_data = {
            'Experience_Level': ['Entry (0-2 years)', 'Mid (3-5 years)', 'Senior (6-10 years)', 'Lead (10+ years)'],
            'Percentage': [35, 40, 20, 5]
        }
        
        fig_exp = px.pie(
            exp_data,
            values='Percentage',
            names='Experience_Level',
            title='Job Distribution by Experience Level'
        )
        st.plotly_chart(fig_exp, use_container_width=True)

def salary_analysis(analytics, category):
    """Detailed salary analysis"""
    st.markdown("### 💰 Comprehensive Salary Analysis")
    
    # Salary statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Average Salary", "$95,750", "5.2% YoY growth")
    
    with col2:
        st.metric("Median Salary", "$87,500", "4.8% YoY growth")
    
    with col3:
        st.metric("Salary Range", "$45k - $250k", "Expanding range")
    
    # Salary by career
    salary_data = analytics.salary_data
    
    # Interactive salary chart
    fig_salary = px.box(
        salary_data,
        x='Category',
        y='Salary',
        title='Salary Distribution by Career Category',
        hover_data=['Experience_Level']
    )
    fig_salary.update_layout(height=500)
    st.plotly_chart(fig_salary, use_container_width=True)
    
    # Salary progression analysis
    st.markdown("#### 📊 Career Progression Analysis")
    
    progression_data = generate_progression_data()
    
    fig_progression = px.line(
        progression_data,
        x='Years_Experience',
        y='Average_Salary',
        color='Career_Path',
        title='Salary Progression by Career Path',
        markers=True
    )
    fig_progression.update_layout(height=400)
    st.plotly_chart(fig_progression, use_container_width=True)
    
    # Compensation components
    st.markdown("#### 💼 Compensation Breakdown")
    
    col1, col2 = st.columns(2)
    
    with col1:
        comp_data = {
            'Component': ['Base Salary', 'Bonus', 'Stock Options', 'Benefits'],
            'Percentage': [70, 15, 10, 5]
        }
        
        fig_comp = px.pie(
            comp_data,
            values='Percentage',
            names='Component',
            title='Average Compensation Components'
        )
        st.plotly_chart(fig_comp, use_container_width=True)
    
    with col2:
        # Top paying skills
        skills_salary = {
            'Skill': ['Machine Learning', 'Cloud Architecture', 'Blockchain', 'DevOps', 'Data Science'],
            'Salary_Premium': [25, 22, 20, 18, 15]
        }
        
        fig_skills = px.bar(
            skills_salary,
            x='Skill',
            y='Salary_Premium',
            title='Skills with Highest Salary Premium (%)',
            color='Salary_Premium',
            color_continuous_scale='viridis'
        )
        st.plotly_chart(fig_skills, use_container_width=True)

def skills_demand_analysis(analytics):
    """Skills demand and gap analysis"""
    st.markdown("### 🛠️ Skills Demand Analysis")
    
    # Skills overview metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Hot Skills", "47", "New skills emerging")
    
    with col2:
        st.metric("Skill Gap Index", "2.8", "Moderate shortage")
    
    with col3:
        st.metric("Learning Time", "6.2 months", "Average skill acquisition")
    
    with col4:
        st.metric("Certification ROI", "34%", "Average salary increase")
    
    # Skills demand heatmap
    skills_matrix = generate_skills_matrix()
    
    fig_heatmap = px.imshow(
        skills_matrix,
        title="Skills Demand Heatmap by Industry",
        aspect="auto",
        color_continuous_scale="viridis"
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)
    
    # Trending skills
    col1, col2 = st.columns(2)
    
    with col1:
        trending_skills = {
            'Skill': ['Generative AI', 'Kubernetes', 'Rust', 'WebAssembly', 'Edge Computing'],
            'Growth_Rate': [156, 89, 67, 45, 34],
            'Demand_Score': [9.2, 8.7, 7.8, 7.2, 8.1]
        }
        
        fig_trending = px.scatter(
            trending_skills,
            x='Growth_Rate',
            y='Demand_Score',
            size='Demand_Score',
            hover_name='Skill',
            title='Trending Skills: Growth vs Demand'
        )
        st.plotly_chart(fig_trending, use_container_width=True)
    
    with col2:
        # Skills with highest ROI
        roi_skills = {
            'Skill': ['AWS Certification', 'Kubernetes', 'Machine Learning', 'Cybersecurity', 'Data Analytics'],
            'ROI_Percentage': [45, 38, 35, 32, 28],
            'Learning_Time_Months': [3, 4, 6, 5, 4]
        }
        
        fig_roi = px.bar(
            roi_skills,
            x='Skill',
            y='ROI_Percentage',
            title='Skills with Highest ROI',
            color='Learning_Time_Months',
            color_continuous_scale='plasma'
        )
        st.plotly_chart(fig_roi, use_container_width=True)

def geographic_analysis(analytics):
    """Geographic job market analysis"""
    st.markdown("### 🌍 Geographic Market Analysis")
    
    # Location metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Top Tech Hub", "San Francisco", "15% of all tech jobs")
    
    with col2:
        st.metric("Fastest Growing", "Austin", "67% job growth YoY")
    
    with col3:
        st.metric("Best Value", "Raleigh", "High salary, low cost")
    
    # Geographic distribution
    location_data = analytics.location_data
    
    fig_geo = px.scatter_geo(
        location_data,
        lat='Latitude',
        lon='Longitude',
        size='Job_Count',
        color='Average_Salary',
        hover_name='City',
        hover_data=['Job_Count', 'Average_Salary', 'Cost_of_Living'],
        title='Job Market by Location',
        projection='natural earth'
    )
    st.plotly_chart(fig_geo, use_container_width=True)
    
    # City comparison
    col1, col2 = st.columns(2)
    
    with col1:
        city_comparison = location_data.head(10)
        
        fig_cities = px.bar(
            city_comparison,
            x='City',
            y='Job_Count',
            title='Top 10 Cities by Job Count',
            color='Average_Salary',
            color_continuous_scale='viridis'
        )
        fig_cities.update_xaxes(tickangle=45)
        st.plotly_chart(fig_cities, use_container_width=True)
    
    with col2:
        # Cost of living vs salary
        fig_cost = px.scatter(
            location_data,
            x='Cost_of_Living',
            y='Average_Salary',
            size='Job_Count',
            hover_name='City',
            title='Salary vs Cost of Living',
            trendline='ols'
        )
        st.plotly_chart(fig_cost, use_container_width=True)

def career_pathways_analysis(analytics):
    """Career pathway and transition analysis"""
    st.markdown("### 🛤️ Career Pathways Analysis")
    
    # Career transition metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Avg Transition Time", "18 months", "To senior role")
    
    with col2:
        st.metric("Success Rate", "73%", "Career transitions")
    
    with col3:
        st.metric("Skill Overlap", "65%", "Between related roles")
    
    # Career progression visualization
    st.markdown("#### 🌊 Career Flow Analysis")
    
    # Sankey diagram for career flows
    fig_sankey = create_career_sankey()
    st.plotly_chart(fig_sankey, use_container_width=True)
    
    # Skills transition matrix
    st.markdown("#### 🔄 Skills Transition Matrix")
    
    transition_matrix = generate_transition_matrix()
    
    fig_transition = px.imshow(
        transition_matrix,
        title="Skills Overlap Between Career Paths",
        aspect="auto",
        color_continuous_scale="blues"
    )
    st.plotly_chart(fig_transition, use_container_width=True)
    
    # Career ladder visualization
    col1, col2 = st.columns(2)
    
    with col1:
        ladder_data = {
            'Level': ['Junior', 'Mid-Level', 'Senior', 'Staff', 'Principal', 'Distinguished'],
            'Years': [0, 3, 6, 10, 15, 20],
            'Salary': [75000, 105000, 140000, 180000, 230000, 300000],
            'Percentage': [100, 80, 60, 35, 15, 5]
        }
        
        fig_ladder = px.line(
            ladder_data,
            x='Years',
            y='Salary',
            title='Typical Career Ladder Progression',
            markers=True
        )
        st.plotly_chart(fig_ladder, use_container_width=True)
    
    with col2:
        # Role transition popularity
        transition_pop = {
            'From_Role': ['Software Engineer', 'Data Analyst', 'Product Manager', 'Designer'],
            'To_Role': ['Senior Engineer', 'Data Scientist', 'Director', 'Design Lead'],
            'Transition_Count': [1200, 800, 600, 400]
        }
        
        fig_trans_pop = px.bar(
            transition_pop,
            x='From_Role',
            y='Transition_Count',
            title='Most Popular Career Transitions'
        )
        st.plotly_chart(fig_trans_pop, use_container_width=True)

def future_trends_analysis(analytics):
    """Future trends and predictions"""
    st.markdown("### 🔮 Future Career Trends & Predictions")
    
    # Future predictions metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("AI Impact", "65%", "Jobs will change")
    
    with col2:
        st.metric("Remote Work", "45%", "Permanently remote")
    
    with col3:
        st.metric("New Job Types", "23%", "Created by 2030")
    
    with col4:
        st.metric("Reskilling Need", "78%", "Workers need training")
    
    # Future job growth predictions
    future_growth = {
        'Job_Category': ['AI/ML Specialist', 'Sustainability Engineer', 'VR/AR Developer', 
                        'Cybersecurity Analyst', 'Cloud Architect', 'Data Engineer'],
        'Growth_2025': [85, 67, 45, 34, 28, 25],
        'Growth_2030': [156, 89, 78, 56, 45, 38]
    }
    
    fig_future = px.bar(
        future_growth,
        x='Job_Category',
        y=['Growth_2025', 'Growth_2030'],
        title='Predicted Job Growth by 2025 and 2030 (%)',
        barmode='group'
    )
    fig_future.update_xaxes(tickangle=45)
    st.plotly_chart(fig_future, use_container_width=True)
    
    # Technology adoption timeline
    st.markdown("#### 🚀 Technology Adoption Timeline")
    
    tech_timeline = {
        'Technology': ['Quantum Computing', 'Brain-Computer Interface', 'Advanced AI', 
                      'Autonomous Systems', '6G Networks', 'Synthetic Biology'],
        'Mainstream_Year': [2028, 2035, 2025, 2027, 2030, 2032],
        'Job_Impact_Score': [7.5, 9.2, 8.8, 8.1, 6.8, 7.9]
    }
    
    fig_timeline = px.scatter(
        tech_timeline,
        x='Mainstream_Year',
        y='Job_Impact_Score',
        size='Job_Impact_Score',
        hover_name='Technology',
        title='Technology Mainstream Adoption vs Job Impact'
    )
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Skills of the future
    col1, col2 = st.columns(2)
    
    with col1:
        future_skills = {
            'Skill': ['AI/ML', 'Emotional Intelligence', 'Systems Thinking', 
                     'Digital Literacy', 'Creativity', 'Critical Thinking'],
            'Importance_2030': [9.5, 8.7, 8.9, 9.2, 8.5, 9.0]
        }
        
        fig_skills = px.bar(
            future_skills,
            x='Skill',
            y='Importance_2030',
            title='Most Important Skills for 2030',
            color='Importance_2030',
            color_continuous_scale='viridis'
        )
        st.plotly_chart(fig_skills, use_container_width=True)
    
    with col2:
        # Automation risk by role
        automation_risk = {
            'Role': ['Data Entry', 'Basic Coding', 'Customer Service', 
                    'Creative Work', 'Strategic Planning', 'Research'],
            'Automation_Risk': [95, 45, 65, 15, 25, 35]
        }
        
        fig_automation = px.bar(
            automation_risk,
            x='Role',
            y='Automation_Risk',
            title='Automation Risk by Role Type (%)',
            color='Automation_Risk',
            color_continuous_scale='reds'
        )
        st.plotly_chart(fig_automation, use_container_width=True)

# Helper functions for data generation

def generate_market_trends():
    """Generate synthetic market trends data"""
    dates = pd.date_range(start='2023-01-01', end='2024-12-31', freq='W')
    
    np.random.seed(42)
    data = {
        'date': dates,
        'AI_ML': np.cumsum(np.random.normal(50, 10, len(dates))) + 1000,
        'Cloud': np.cumsum(np.random.normal(30, 8, len(dates))) + 800,
        'Cybersecurity': np.cumsum(np.random.normal(25, 6, len(dates))) + 600,
        'Data_Science': np.cumsum(np.random.normal(35, 9, len(dates))) + 700,
        'Software_Dev': np.cumsum(np.random.normal(40, 12, len(dates))) + 1200
    }
    
    return pd.DataFrame(data)

def generate_salary_data():
    """Generate synthetic salary data"""
    np.random.seed(42)
    
    categories = ['Technology', 'Data Science', 'Business', 'Design', 'Management']
    experience_levels = ['Entry', 'Mid', 'Senior', 'Lead']
    
    data = []
    for category in categories:
        for exp_level in experience_levels:
            for _ in range(100):
                base_salary = {
                    'Entry': 70000, 'Mid': 100000, 'Senior': 140000, 'Lead': 180000
                }[exp_level]
                
                category_multiplier = {
                    'Technology': 1.1, 'Data Science': 1.2, 'Business': 0.9,
                    'Design': 0.85, 'Management': 1.15
                }[category]
                
                salary = base_salary * category_multiplier * np.random.normal(1, 0.2)
                salary = max(salary, 40000)  # Minimum salary
                
                data.append({
                    'Category': category,
                    'Experience_Level': exp_level,
                    'Salary': salary
                })
    
    return pd.DataFrame(data)

def generate_progression_data():
    """Generate career progression data"""
    careers = ['Software Engineer', 'Data Scientist', 'Product Manager', 'Designer']
    years = range(0, 21)
    
    data = []
    for career in careers:
        for year in years:
            base_growth = {
                'Software Engineer': 1.08,
                'Data Scientist': 1.10,
                'Product Manager': 1.07,
                'Designer': 1.06
            }[career]
            
            starting_salary = {
                'Software Engineer': 75000,
                'Data Scientist': 85000,
                'Product Manager': 80000,
                'Designer': 65000
            }[career]
            
            salary = starting_salary * (base_growth ** year)
            
            data.append({
                'Career_Path': career,
                'Years_Experience': year,
                'Average_Salary': salary
            })
    
    return pd.DataFrame(data)

def generate_skills_matrix():
    """Generate skills demand matrix"""
    skills = ['Python', 'JavaScript', 'SQL', 'Machine Learning', 'Cloud', 'Leadership']
    industries = ['Technology', 'Finance', 'Healthcare', 'Education', 'Manufacturing']
    
    np.random.seed(42)
    return np.random.rand(len(industries), len(skills)) * 10

def generate_transition_matrix():
    """Generate career transition matrix"""
    careers = ['Software Engineer', 'Data Scientist', 'Product Manager', 'Designer', 'DevOps']
    
    np.random.seed(42)
    matrix = np.random.rand(len(careers), len(careers))
    
    # Make diagonal stronger (same career progression)
    for i in range(len(careers)):
        matrix[i][i] = 0.9
    
    return matrix

def create_career_sankey():
    """Create Sankey diagram for career flows"""
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=["Junior Dev", "Mid Dev", "Senior Dev", "Tech Lead", "Principal", "Staff"],
            color="blue"
        ),
        link=dict(
            source=[0, 1, 2, 3, 4],
            target=[1, 2, 3, 4, 5],
            value=[1000, 800, 600, 300, 150]
        )
    )])
    
    fig.update_layout(title_text="Career Progression Flow", font_size=10)
    return fig

# Main execution
if __name__ == "__main__":
    st.set_page_config(page_title="Career Analytics", layout="wide")
    career_analytics_dashboard()
