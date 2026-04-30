import requests
import json
from typing import Optional, Dict, List, Any
from datetime import datetime

class DjangoAPIClient:
    """Client to interact with Django backend API"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
        self.auth_token = None
    
    def login(self, username: str, password: str) -> bool:
        """Login user and store authentication token"""
        try:
            response = self.session.post(
                f"{self.base_url}/api/auth/login/",
                json={"username": username, "password": password},
                timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                self.auth_token = data.get('token')
                self.session.headers.update({'Authorization': f'Token {self.auth_token}'})
                return True
            return False
        except Exception as e:
            print(f"Login error: {e}")
            return False
    
    def logout(self) -> bool:
        """Logout user"""
        try:
            self.session.post(f"{self.base_url}/api/auth/logout/", timeout=5)
            self.auth_token = None
            self.session.headers.pop('Authorization', None)
            return True
        except Exception as e:
            print(f"Logout error: {e}")
            return False
    
    def get_user_profile(self) -> Optional[Dict[str, Any]]:
        """Get current user profile"""
        try:
            response = self.session.get(
                f"{self.base_url}/api/user/profile/",
                timeout=5
            )
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Get profile error: {e}")
            return None
    
    def get_lifestyle_entries(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Get user's lifestyle entries"""
        try:
            response = self.session.get(
                f"{self.base_url}/api/lifestyle/entries/",
                params={"limit": limit},
                timeout=5
            )
            if response.status_code == 200:
                return response.json()
            return []
        except Exception as e:
            print(f"Get entries error: {e}")
            return []
    
    def get_lifestyle_entry(self, entry_id: int) -> Optional[Dict[str, Any]]:
        """Get specific lifestyle entry"""
        try:
            response = self.session.get(
                f"{self.base_url}/api/lifestyle/entries/{entry_id}/",
                timeout=5
            )
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Get entry error: {e}")
            return None
    
    def create_lifestyle_entry(self, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Create new lifestyle entry"""
        try:
            response = self.session.post(
                f"{self.base_url}/api/lifestyle/entries/",
                json=data,
                timeout=5
            )
            if response.status_code == 201:
                return response.json()
            return None
        except Exception as e:
            print(f"Create entry error: {e}")
            return None
    
    def get_statistics(self) -> Optional[Dict[str, Any]]:
        """Get user statistics and analytics"""
        try:
            response = self.session.get(
                f"{self.base_url}/api/lifestyle/statistics/",
                timeout=5
            )
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Get statistics error: {e}")
            return None
    
    def predict_score(self, sleep_hours: float, exercise_hours: float, 
                     diet_quality: str) -> Optional[float]:
        """Get prediction for lifestyle score"""
        try:
            response = self.session.post(
                f"{self.base_url}/api/prediction/predict/",
                json={
                    "sleep_hours": sleep_hours,
                    "exercise_hours": exercise_hours,
                    "diet_quality": diet_quality
                },
                timeout=5
            )
            if response.status_code == 200:
                return response.json().get('score')
            return None
        except Exception as e:
            print(f"Prediction error: {e}")
            return None
    
    def is_authenticated(self) -> bool:
        """Check if user is authenticated"""
        return self.auth_token is not None


# Helper functions for common operations
def get_client(base_url: str = "http://localhost:8000") -> DjangoAPIClient:
    """Get API client instance"""
    return DjangoAPIClient(base_url)


def format_lifestyle_data(entry: Dict[str, Any]) -> Dict[str, Any]:
    """Format lifestyle entry data for display"""
    return {
        'id': entry.get('id'),
        'date': entry.get('created_at', '').split('T')[0],
        'time': entry.get('created_at', '').split('T')[1][:5] if 'T' in entry.get('created_at', '') else '',
        'sleep_hours': entry.get('sleep_hours'),
        'exercise_hours': entry.get('exercise_hours'),
        'diet_quality': entry.get('diet_quality'),
        'lifestyle_score': entry.get('lifestyle_score'),
        'address': entry.get('address', 'Not specified'),
        'score_percentage': int((entry.get('lifestyle_score', 0) / 100) * 100)
    }


def get_score_interpretation(score: float) -> tuple:
    """Get interpretation and recommendation for score"""
    if score >= 80:
        return "Excellent!", "🌟 Your lifestyle score is outstanding. You're maintaining great habits!"
    elif score >= 60:
        return "Good!", "✅ Your lifestyle is healthy. Keep up the good habits and you could improve more!"
    elif score >= 40:
        return "Average", "⚠️ There's room for improvement. Consider increasing exercise or improving your diet."
    else:
        return "Needs Improvement", "❌ Focus on increasing sleep, exercise, or improving diet quality."
