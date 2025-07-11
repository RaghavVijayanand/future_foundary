# Future Foundry - Career Prediction System

A comprehensive career guidance platform that combines machine learning predictions with a modern web interface.

## Project Structure

```
Future Foundary/
├── Career-Prediction-System/     # Python ML backend
│   ├── app.py                    # Main Streamlit application
│   ├── requirements.txt          # Python dependencies
│   ├── weights.pkl              # Trained ML model
│   ├── data/mldata.csv          # Training dataset
│   ├── pythonFunctions/         # Core ML functions
│   └── assets/                  # Images and resources
├── Main site/                   # React frontend
│   ├── package.json             # Node.js dependencies
│   ├── src/                     # React source code
│   └── public/                  # Static assets
└── carousel/                    # Additional components
```

## Setup Instructions

### 1. Career Prediction System (Python Backend)

1. Navigate to the Career-Prediction-System directory:
   ```bash
   cd "Career-Prediction-System"
   ```

2. Create a virtual environment:
   ```bash
   python -m venv career_env
   career_env\Scripts\activate  # Windows
   # source career_env/bin/activate  # Linux/Mac
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

### 2. Main Site (React Frontend)

1. Navigate to the Main site directory:
   ```bash
   cd "Main site"
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

## Features

### Career Prediction System
- **Machine Learning Model**: Trained model for career path prediction
- **Interactive Interface**: Streamlit-based user interface
- **Database Integration**: SQLite database for storing user data
- **Multiple Input Methods**: Support for various user input formats

### Main Website
- **Modern React Interface**: Built with React 18 and Vite
- **Responsive Design**: Mobile-friendly interface
- **Navigation**: Multi-page application with React Router
- **Animations**: Smooth transitions with Framer Motion
- **3D Graphics**: Three.js integration for enhanced visuals

## Recent Fixes Applied

✅ **Parameter Naming Issues**
- Fixed `Interested_Type_of_Books` mislabeling in certification selectbox
- Corrected `Magement_or_Techinical` typo to `Management_or_Technical`

✅ **Variable Consistency**
- Fixed `K` vs `k` variable inconsistencies throughout the codebase
- Resolved undefined variable references

✅ **Import and Dependencies**
- Added missing imports in GUI.py
- Updated requirements.txt with all necessary packages
- Fixed model loading references (`dtree` → `regressor`)

✅ **Code Quality**
- Removed invalid pip install statements from Python code
- Fixed undefined variable references
- Standardized parameter naming conventions

## Usage

1. **Start the Python backend** (Streamlit app) for career predictions
2. **Start the React frontend** for the main website interface
3. Users can input their information and receive career guidance
4. The system stores user data and provides personalized recommendations

## Technologies Used

### Backend
- Python 3.7+
- Streamlit
- Pandas, NumPy
- Scikit-learn
- SQLite
- Gradio (for alternative interface)

### Frontend
- React 18
- Vite
- React Router DOM
- Framer Motion
- Three.js
- Lucide React (icons)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

See LICENSE file for details.
# future_foundary
# future_foundary
