import pickle
import pandas as pd
import os

# Load the trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'lifestyle_model.pkl')

def load_model():
    """Load the trained lifestyle prediction model"""
    try:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        raise Exception(f"Model not found at {MODEL_PATH}")

def predict_lifestyle_score(sleep_hours, exercise_hours, diet_quality):
    """
    Predict lifestyle score based on user input
    
    Parameters:
    - sleep_hours: float (hours of sleep)
    - exercise_hours: float (hours of exercise)
    - diet_quality: str ('poor', 'fair', 'good', 'excellent')
    
    Returns:
    - float: predicted lifestyle score
    """
    # Load model
    model = load_model()
    
    # Encode diet_quality (assuming the model uses numeric encoding 0-3)
    diet_encoding = {
        'poor': 0,
        'fair': 1,
        'good': 2,
        'excellent': 3
    }
    
    diet_encoded = diet_encoding.get(diet_quality.lower(), 3)
    
    # Create feature array (order must match training data)
    features = pd.DataFrame({
        'sleep_hours': [float(sleep_hours)],
        'exercise_hours': [float(exercise_hours)],
        'diet_quality': [diet_encoded]
    })
    
    # Make prediction
    prediction = model.predict(features)[0]
    
    return round(float(prediction), 2)
