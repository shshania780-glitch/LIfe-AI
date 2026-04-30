# Life AI - Lifestyle Prediction System

## 🎯 Project Overview

**Life AI** is an intelligent web application that predicts your lifestyle score based on key health metrics. Using machine learning algorithms, it analyzes your sleep patterns, exercise habits, and dietary choices to provide personalized lifestyle insights and recommendations.

![Life AI Logo](https://img.shields.io/badge/Life%20AI-Health%20Prediction-blue?style=for-the-badge&logo=ai&logoColor=white)

## ✨ Key Features

### 🔬 **Smart Prediction Engine**
- **Machine Learning Model**: Random Forest Classifier trained on lifestyle data
- **Real-time Scoring**: Instant lifestyle score calculation (0-100)
- **Personalized Insights**: Tailored recommendations based on your data

### 📊 **Comprehensive Data Collection**
- **Sleep Tracking**: Hours of sleep per day
- **Exercise Monitoring**: Daily physical activity hours
- **Diet Quality Assessment**: Poor/Fair/Good/Excellent ratings
- **Location-based Analysis**: Personalized insights by location

### 🎨 **Modern User Interface**
- **Dark Glass Design**: Beautiful, modern UI with glassmorphism effects
- **Responsive Layout**: Works perfectly on desktop and mobile
- **Intuitive Navigation**: Clean, user-friendly interface
- **Real-time Feedback**: Immediate prediction results

### 👤 **User Management**
- **Secure Authentication**: Django-powered user system
- **Personal Dashboard**: Track your lifestyle history
- **Data Privacy**: Secure data storage and management
- **Progress Tracking**: Monitor improvements over time

## 🛠️ Technology Stack

### Backend
- **Django 4.2**: High-level Python web framework
- **SQLite**: Lightweight database for data storage
- **Scikit-learn**: Machine learning library for predictions

### Frontend
- **HTML5**: Semantic markup structure
- **CSS3**: Modern styling with gradients and animations
- **JavaScript**: Interactive UI enhancements

### Machine Learning
- **Random Forest**: Ensemble learning algorithm
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Life AI"
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   cd config
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Open your browser to `http://127.0.0.1:8000/`
   - Register a new account or login

## 📱 Usage Guide

### 1. **User Registration**
- Create an account with username and password
- Secure authentication system

### 2. **Lifestyle Assessment**
- Fill out the comprehensive lifestyle form
- Input sleep hours, exercise hours, diet quality, and location
- Get instant prediction results

### 3. **View Results**
- See your lifestyle score immediately after submission
- Access detailed breakdown of your inputs
- Navigate to profile for historical data

### 4. **Track Progress**
- View all previous assessments in your dashboard
- Monitor lifestyle score trends over time
- Delete old entries if needed

## 📁 Project Structure

```
Life AI/
├── api_client.py          # API client utilities
├── app.py                 # ML prediction engine
├── lifestyle.csv          # Training dataset
├── requirements.txt       # Python dependencies
├── run_all.py            # Batch execution script
├── streamlit_app.py      # Streamlit interface (optional)
├── config/               # Django project
│   ├── manage.py
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── predictions/      # Main app
│   │   ├── models.py     # Database models
│   │   ├── views.py      # Business logic
│   │   ├── forms.py      # Django forms
│   │   └── migrations/
│   ├── users/           # User management
│   ├── static/          # CSS, JS assets
│   └── templates/       # HTML templates
└── model/               # ML model files
    ├── train_model.py   # Model training script
    └── lifestyle_model.pkl  # Trained model
```

## 🎨 UI/UX Highlights

### **Form Page**
- Clean, intuitive data collection interface
- Real-time prediction display
- Helper text for each field
- Immediate feedback on submission

### **Profile Dashboard**
- Personal lifestyle history
- Statistical overview cards
- Delete functionality for data management
- Responsive design for all devices

### **Authentication Pages**
- Modern login/register forms
- Consistent design language
- Error handling and validation

## 📈 Machine Learning Model

### **Training Data**
- 600+ lifestyle records
- Features: sleep_hours, exercise_hours, diet_quality
- Target: lifestyle_score (0-100)

### **Model Performance**
- **Algorithm**: Random Forest Classifier
- **Accuracy**: High prediction accuracy on test data
- **Features**: Handles both numerical and categorical data

### **Prediction Logic**
```python
# Diet quality encoding
diet_mapping = {
    'poor': 0,
    'fair': 1,
    'good': 2,
    'excellent': 3
}

# Features for prediction
features = [sleep_hours, exercise_hours, diet_quality_encoded]
```

## 🔒 Security & Privacy

- **User Authentication**: Django's built-in auth system
- **Data Encryption**: Secure password hashing
- **CSRF Protection**: Cross-site request forgery prevention
- **SQL Injection Prevention**: Django ORM protection
- **Session Management**: Secure session handling

## 📊 Sample Data Insights

Based on our training data:
- **Average Sleep**: ~7.5 hours per day
- **Average Exercise**: ~2.8 hours per day
- **Diet Distribution**: Balanced across quality levels
- **Score Range**: 60-100 (higher scores correlate with better habits)

## 🚀 Future Enhancements

### **Short Term**
- [ ] Mobile app development
- [ ] Advanced analytics dashboard
- [ ] Social features (friend comparisons)
- [ ] Export data functionality

### **Long Term**
- [ ] Integration with wearables (Fitbit, Apple Watch)
- [ ] Advanced ML models (Neural Networks)
- [ ] Personalized recommendations engine
- [ ] Health goal tracking and notifications

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Developer

**Life AI Team**
- Built with ❤️ using Django and Machine Learning
- Focused on promoting healthy lifestyle choices

---

## 🎯 Mission Statement

*"Empowering individuals to make informed lifestyle decisions through the power of artificial intelligence and data-driven insights."*

---

**Ready to optimize your lifestyle?** 🚀

Start your journey with Life AI today and discover your personalized health score!</content>
<parameter name="filePath">c:\Users\HP\Desktop\Life AI\README.md