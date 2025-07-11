#!/usr/bin/env python3
"""
Retrain the career prediction model with current scikit-learn version
"""

import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def preprocess_data(df):
    """Preprocess the dataset for training"""
    # Create a copy to avoid modifying the original
    newdf = df.copy()
    
    # Binary encoding for Yes/No categorical variables
    yes_no_cols = [
        "self-learning capability?",
        "Extra-courses did",
        "Taken inputs from seniors or elders",
        "worked in teams ever?",
        "Introvert",
    ]
    
    for col in yes_no_cols:
        if col in newdf.columns:
            cleanup_nums = {col: {"yes": 1, "no": 0}}
            newdf = newdf.replace(cleanup_nums)
    
    # Number encoding for skill levels
    skill_cols = ["reading and writing skills", "memory capability score"]
    for col in skill_cols:
        if col in newdf.columns:
            cleanup_nums = {col: {"poor": 0, "medium": 1, "excellent": 2}}
            newdf = newdf.replace(cleanup_nums)
    
    # Category encoding for other categorical features
    category_cols = [
        "certifications",
        "workshops", 
        "Interested subjects",
        "interested career area ",
        "Type of company want to settle in?",
        "Interested Type of Books",
    ]
    
    for col in category_cols:
        if col in newdf.columns:
            newdf[col] = newdf[col].astype("category")
            newdf[col + "_code"] = newdf[col].cat.codes
    
    # Dummy variable encoding for Management/Technical and Smart/Hard worker
    if "Management or Technical" in newdf.columns:
        newdf = pd.get_dummies(newdf, columns=["Management or Technical"], prefix=["A"])
    
    if "hard/smart worker" in newdf.columns:
        newdf = pd.get_dummies(newdf, columns=["hard/smart worker"], prefix=["B"])
    
    return newdf

def train_model():
    """Train and save the career prediction model"""
    print("Loading dataset...")
    df = pd.read_csv("./data/mldata.csv")
    
    # Fix the data inconsistency mentioned in the original code
    df["workshops"] = df["workshops"].replace(["testing"], "Testing")
    
    print(f"Dataset shape: {df.shape}")
    print(f"Target classes: {df['Suggested Job Role'].unique()}")
    
    # Preprocess the data
    print("Preprocessing data...")
    processed_df = preprocess_data(df)
    
    # Select features for training
    feature_columns = [
        "Logical quotient rating", 
        "coding skills rating",
        "hackathons",
        "public speaking points",
        "self-learning capability?",
        "Extra-courses did", 
        "Taken inputs from seniors or elders",
        "worked in teams ever?",
        "Introvert",
        "reading and writing skills",
        "memory capability score",
    ]
    
    # Add the encoded categorical features
    categorical_encoded = [
        "certifications_code",
        "workshops_code",
        "Interested subjects_code", 
        "interested career area _code",
        "Type of company want to settle in?_code",
        "Interested Type of Books_code",
    ]
    
    # Add dummy variables if they exist
    dummy_cols = [col for col in processed_df.columns if col.startswith(('A_', 'B_'))]
    
    # Combine all feature columns
    all_features = feature_columns + categorical_encoded + dummy_cols
    
    # Filter to only include existing columns
    available_features = [col for col in all_features if col in processed_df.columns]
    
    print(f"Using {len(available_features)} features for training")
    print("Features:", available_features)
    
    # Prepare the data
    X = processed_df[available_features]
    y = processed_df["Suggested Job Role"]
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print(f"Training set size: {X_train.shape}")
    print(f"Test set size: {X_test.shape}")
    
    # Train a Random Forest model (generally more robust than Decision Tree)
    print("Training Random Forest model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Model accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save the model
    print("Saving model...")
    with open("weights.pkl", "wb") as f:
        pickle.dump(model, f)
    
    print("Model saved successfully as 'weights.pkl'")
    
    return model, available_features

if __name__ == "__main__":
    try:
        model, features = train_model()
        print("\n✅ Model training completed successfully!")
        print(f"Model type: {type(model).__name__}")
        print(f"Number of features: {len(features)}")
        
    except Exception as e:
        print(f"❌ Error during model training: {str(e)}")
        import traceback
        traceback.print_exc()
