#!/usr/bin/env python3
"""
Enhanced Career Prediction Model with Extended Career Options
"""

import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# Extended career mapping - maps original careers to broader categories
CAREER_EXPANSION_MAP = {
    'Applications Developer': [
        'Mobile App Developer', 'Web Developer', 'Software Developer', 
        'Full Stack Developer', 'Frontend Developer', 'Backend Developer'
    ],
    'Software Developer': [
        'Senior Software Engineer', 'Lead Developer', 'Software Architect',
        'DevOps Engineer', 'Site Reliability Engineer', 'Platform Engineer'
    ],
    'Software Engineer': [
        'Machine Learning Engineer', 'AI Engineer', 'Data Engineer',
        'Cloud Engineer', 'Automation Engineer', 'Robotics Engineer'
    ],
    'Database Developer': [
        'Database Administrator', 'Data Architect', 'Data Warehouse Developer',
        'Big Data Engineer', 'Database Analyst', 'Data Migration Specialist'
    ],
    'Web Developer': [
        'UI/UX Designer', 'Frontend Specialist', 'WordPress Developer',
        'E-commerce Developer', 'JAMstack Developer', 'Progressive Web App Developer'
    ],
    'Network Security Engineer': [
        'Cybersecurity Analyst', 'Information Security Specialist', 'Penetration Tester',
        'Security Consultant', 'Incident Response Analyst', 'Security Architect'
    ],
    'Systems Security Administrator': [
        'Cloud Security Engineer', 'Identity Management Specialist', 'Compliance Officer',
        'Security Operations Center Analyst', 'Vulnerability Assessment Specialist'
    ],
    'Mobile Applications Developer': [
        'iOS Developer', 'Android Developer', 'React Native Developer',
        'Flutter Developer', 'Mobile Game Developer', 'AR/VR Developer'
    ],
    'Software Quality Assurance (QA) / Testing': [
        'QA Engineer', 'Test Automation Engineer', 'Performance Test Engineer',
        'Manual Tester', 'QA Manager', 'Test Lead'
    ],
    'Technical Support': [
        'IT Support Specialist', 'Help Desk Technician', 'System Administrator',
        'Customer Success Engineer', 'Technical Account Manager'
    ],
    'UX Designer': [
        'Product Designer', 'User Researcher', 'Interaction Designer',
        'Service Designer', 'Design System Manager', 'Creative Director'
    ],
    'CRM Technical Developer': [
        'Salesforce Developer', 'CRM Consultant', 'Business Analyst',
        'Process Automation Specialist', 'Integration Specialist'
    ]
}

# Business and non-tech career additions
BUSINESS_CAREERS = [
    'Product Manager', 'Project Manager', 'Business Analyst', 'Strategy Consultant',
    'Digital Marketing Manager', 'Sales Manager', 'Operations Manager', 'HR Manager',
    'Financial Analyst', 'Investment Banker', 'Management Consultant', 'Supply Chain Manager',
    'Risk Analyst', 'Marketing Coordinator', 'Business Development Manager'
]

CREATIVE_CAREERS = [
    'Graphic Designer', 'Video Editor', 'Content Creator', 'Social Media Manager',
    'Brand Manager', 'Creative Director', 'Photographer', 'Animation Artist',
    'Motion Graphics Designer', 'Interior Designer', 'Fashion Designer', 'Copywriter'
]

EMERGING_CAREERS = [
    'Data Scientist', 'AI Research Scientist', 'Blockchain Developer', 'IoT Developer',
    'Digital Transformation Specialist', 'Sustainability Consultant', 'Virtual Reality Developer',
    'Augmented Reality Developer', 'Digital Twin Specialist', 'Smart City Planner',
    'Biomedical Engineer', 'Health Informatics Specialist', 'EdTech Developer'
]

def expand_career_dataset(df):
    """Expand the dataset with additional career paths and synthetic data"""
    expanded_rows = []
    
    for _, row in df.iterrows():
        original_career = row['Suggested Job Role']
        
        # Add original row
        expanded_rows.append(row.to_dict())
        
        # Add expanded career variations
        if original_career in CAREER_EXPANSION_MAP:
            for new_career in CAREER_EXPANSION_MAP[original_career]:
                new_row = row.to_dict()
                new_row['Suggested Job Role'] = new_career
                
                # Add some variation to create realistic diversity
                new_row = add_career_specific_variations(new_row, new_career)
                expanded_rows.append(new_row)
    
    # Add completely new career paths with synthetic data
    expanded_rows.extend(generate_synthetic_career_data())
    
    return pd.DataFrame(expanded_rows)

def add_career_specific_variations(row, career):
    """Add career-specific variations to make data more realistic"""
    
    # Data Science careers tend to have higher analytical skills
    if 'Data' in career or 'Analytics' in career:
        row['Logical quotient rating'] = min(10, row['Logical quotient rating'] + np.random.randint(1, 3))
        row['reading and writing skills'] = 'excellent' if np.random.random() > 0.3 else row['reading and writing skills']
    
    # Management roles tend to have better communication
    if 'Manager' in career or 'Lead' in career or 'Director' in career:
        row['public speaking points'] = min(10, row['public speaking points'] + np.random.randint(1, 4))
        row['Management or Technical'] = 'Management'
        row['worked in teams ever?'] = 'yes'
    
    # Creative roles have different characteristics
    if career in CREATIVE_CAREERS:
        row['Interested Type of Books'] = np.random.choice(['Art', 'Design', 'Creative', 'Visual'])
        row['Management or Technical'] = np.random.choice(['Management', 'Technical'])
    
    # Technical specialists
    if 'Engineer' in career or 'Developer' in career:
        row['coding skills rating'] = min(10, row['coding skills rating'] + np.random.randint(1, 3))
        row['Management or Technical'] = 'Technical'
    
    return row

def generate_synthetic_career_data():
    """Generate synthetic data for new career paths"""
    synthetic_data = []
    all_new_careers = BUSINESS_CAREERS + CREATIVE_CAREERS + EMERGING_CAREERS
    
    for career in all_new_careers:
        # Generate 10-20 samples per new career
        for _ in range(np.random.randint(10, 21)):
            row = generate_synthetic_profile(career)
            synthetic_data.append(row)
    
    return synthetic_data

def generate_synthetic_profile(career):
    """Generate a realistic synthetic profile for a given career"""
    
    # Base profile
    profile = {
        'Logical quotient rating': np.random.randint(3, 9),
        'hackathons': np.random.randint(0, 8),
        'coding skills rating': np.random.randint(2, 8),
        'public speaking points': np.random.randint(2, 9),
        'self-learning capability?': np.random.choice(['yes', 'no'], p=[0.7, 0.3]),
        'Extra-courses did': np.random.choice(['yes', 'no'], p=[0.6, 0.4]),
        'certifications': np.random.choice([
            'information security', 'machine learning', 'cloud computing',
            'data science', 'project management', 'digital marketing'
        ]),
        'workshops': np.random.choice([
            'data science', 'cloud computing', 'leadership', 'design thinking'
        ]),
        'reading and writing skills': np.random.choice(['poor', 'medium', 'excellent'], p=[0.1, 0.4, 0.5]),
        'memory capability score': np.random.choice(['poor', 'medium', 'excellent'], p=[0.1, 0.5, 0.4]),
        'Interested subjects': np.random.choice([
            'programming', 'Management', 'data engineering', 'business strategy'
        ]),
        'interested career area ': np.random.choice([
            'technology', 'business', 'creative', 'consulting'
        ]),
        'Type of company want to settle in?': np.random.choice([
            'Technology', 'Startup', 'Consulting', 'Healthcare', 'Finance'
        ]),
        'Taken inputs from seniors or elders': np.random.choice(['yes', 'no'], p=[0.7, 0.3]),
        'Interested Type of Books': np.random.choice([
            'Business', 'Technology', 'Self-help', 'Science', 'Biography'
        ]),
        'Management or Technical': get_mgmt_tech_preference(career),
        'hard/smart worker': np.random.choice(['smart worker', 'hard worker'], p=[0.6, 0.4]),
        'worked in teams ever?': np.random.choice(['yes', 'no'], p=[0.8, 0.2]),
        'Introvert': np.random.choice(['yes', 'no'], p=[0.4, 0.6]),
        'Suggested Job Role': career
    }
    
    # Career-specific adjustments
    if career in BUSINESS_CAREERS:
        profile['public speaking points'] = max(profile['public speaking points'], 6)
        profile['Management or Technical'] = 'Management'
        profile['worked in teams ever?'] = 'yes'
    
    elif career in CREATIVE_CAREERS:
        profile['Interested Type of Books'] = np.random.choice(['Art', 'Design', 'Creative'])
        profile['hackathons'] = max(0, profile['hackathons'] - 2)  # Less hackathons
    
    elif career in EMERGING_CAREERS:
        profile['Logical quotient rating'] = max(profile['Logical quotient rating'], 7)
        profile['self-learning capability?'] = 'yes'
        profile['Extra-courses did'] = 'yes'
    
    return profile

def get_mgmt_tech_preference(career):
    """Determine management vs technical preference based on career"""
    management_careers = [
        'Product Manager', 'Project Manager', 'Operations Manager', 'HR Manager',
        'Sales Manager', 'Marketing Manager', 'Creative Director'
    ]
    
    if any(mgmt_role in career for mgmt_role in management_careers):
        return 'Management'
    elif 'Developer' in career or 'Engineer' in career or 'Analyst' in career:
        return 'Technical'
    else:
        return np.random.choice(['Management', 'Technical'])

def train_enhanced_model():
    """Train the enhanced career prediction model"""
    print("Loading and expanding dataset...")
    
    # Load original data
    df = pd.read_csv("./data/mldata.csv")
    df["workshops"] = df["workshops"].replace(["testing"], "Testing")
    
    print(f"Original dataset shape: {df.shape}")
    print(f"Original careers: {len(df['Suggested Job Role'].unique())}")
    
    # Expand dataset
    expanded_df = expand_career_dataset(df)
    print(f"Expanded dataset shape: {expanded_df.shape}")
    print(f"Total careers: {len(expanded_df['Suggested Job Role'].unique())}")
    
    # Preprocess data
    processed_df = preprocess_enhanced_data(expanded_df)
    
    # Prepare features and target
    feature_columns = [
        "Logical quotient rating", "coding skills rating", "hackathons", "public speaking points",
        "self-learning capability?", "Extra-courses did", "Taken inputs from seniors or elders",
        "worked in teams ever?", "Introvert", "reading and writing skills", "memory capability score",
        "certifications_code", "workshops_code", "Interested subjects_code", 
        "interested career area _code", "Type of company want to settle in?_code",
        "Interested Type of Books_code"
    ]
    
    # Add dummy variables
    dummy_cols = [col for col in processed_df.columns if col.startswith(('A_', 'B_'))]
    all_features = feature_columns + dummy_cols
    
    # Filter existing columns
    available_features = [col for col in all_features if col in processed_df.columns]
    
    print(f"Using {len(available_features)} features for training")
    
    X = processed_df[available_features]
    y = processed_df["Suggested Job Role"]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    print(f"Training set size: {X_train.shape}")
    print(f"Test set size: {X_test.shape}")
    print(f"Number of unique careers: {len(y.unique())}")
    
    # Train ensemble model
    print("Training Enhanced Random Forest model...")
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        class_weight='balanced'  # Handle class imbalance
    )
    
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Enhanced Model Accuracy: {accuracy:.4f}")
    print(f"Number of career predictions: {len(model.classes_)}")
    
    # Save the enhanced model
    print("Saving enhanced model...")
    with open("enhanced_weights.pkl", "wb") as f:
        pickle.dump(model, f)
    
    # Save feature names for consistency
    with open("feature_names.pkl", "wb") as f:
        pickle.dump(available_features, f)
    
    # Save career list
    with open("career_list.pkl", "wb") as f:
        pickle.dump(list(model.classes_), f)
    
    print("✅ Enhanced model saved successfully!")
    print(f"Career options available: {len(model.classes_)}")
    
    # Display some sample careers
    print("\nSample career predictions available:")
    for i, career in enumerate(sorted(model.classes_)[:20]):
        print(f"  {i+1}. {career}")
    
    if len(model.classes_) > 20:
        print(f"  ... and {len(model.classes_) - 20} more careers!")
    
    return model, available_features

def preprocess_enhanced_data(df):
    """Enhanced preprocessing for the expanded dataset"""
    newdf = df.copy()
    
    # Binary encoding
    yes_no_cols = ["self-learning capability?", "Extra-courses did", 
                   "Taken inputs from seniors or elders", "worked in teams ever?", "Introvert"]
    
    for col in yes_no_cols:
        if col in newdf.columns:
            cleanup_nums = {col: {"yes": 1, "no": 0}}
            newdf = newdf.replace(cleanup_nums)
    
    # Skill level encoding
    skill_cols = ["reading and writing skills", "memory capability score"]
    for col in skill_cols:
        if col in newdf.columns:
            cleanup_nums = {col: {"poor": 0, "medium": 1, "excellent": 2}}
            newdf = newdf.replace(cleanup_nums)
    
    # Category encoding
    category_cols = ["certifications", "workshops", "Interested subjects", 
                    "interested career area ", "Type of company want to settle in?", 
                    "Interested Type of Books"]
    
    for col in category_cols:
        if col in newdf.columns:
            newdf[col] = newdf[col].astype("category")
            newdf[col + "_code"] = newdf[col].cat.codes
    
    # Dummy encoding
    if "Management or Technical" in newdf.columns:
        newdf = pd.get_dummies(newdf, columns=["Management or Technical"], prefix=["A"])
    
    if "hard/smart worker" in newdf.columns:
        newdf = pd.get_dummies(newdf, columns=["hard/smart worker"], prefix=["B"])
    
    return newdf

if __name__ == "__main__":
    try:
        model, features = train_enhanced_model()
        print(f"\n🎉 Enhanced training completed successfully!")
        print(f"Model can predict {len(model.classes_)} different career paths!")
        
    except Exception as e:
        print(f"❌ Error during enhanced training: {str(e)}")
        import traceback
        traceback.print_exc()
