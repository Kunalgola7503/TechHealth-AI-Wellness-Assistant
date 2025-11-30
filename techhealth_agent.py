"""TechHealth: AI-Powered Wellness Assistant
Multi-Agent Healthcare Solution for Kaggle AI Agents Capstone Project

This implementation demonstrates concepts from the 5-Day AI Agents Intensive Course:
- Day 1: Agent architecture and prompt-to-action
- Day 2: Tools integration and MCP
- Day 3: Sessions and memory management
- Day 4: Observability and evaluation
- Day 5: A2A protocol and deployment

Author: Kunal Gola
Date: November 30, 2025
Track: Agents for Good (Healthcare)
"""

import os
import json
import logging
from datetime import datetime
from typing import Dict, List, Any
import google.generativeai as genai

# Configure logging for observability (Day 4)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configure Gemini API
API_KEY = os.getenv('GEMINI_API_KEY', 'YOUR_API_KEY_HERE')
genai.configure(api_key=API_KEY)

class HealthMonitoringAgent:
    """Agent 1: Monitors user health metrics and detects anomalies"""
    
    def __init__(self):
        self.name = "HealthMonitor"
        self.model = genai.GenerativeModel('gemini-pro')
        logger.info(f"{self.name} initialized")
    
    def analyze_health_data(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze health metrics and detect potential issues"""
        logger.info(f"{self.name}: Analyzing health data")
        
        prompt = f"""
        As a health monitoring AI, analyze the following health metrics:
        
        Heart Rate: {user_data.get('heart_rate', 'N/A')} bpm
        Blood Pressure: {user_data.get('blood_pressure', 'N/A')}
        Sleep Hours: {user_data.get('sleep_hours', 'N/A')}
        Activity Level: {user_data.get('activity_level', 'N/A')}
        
        Provide:
        1. Risk level (Low/Medium/High)
        2. Key concerns if any
        3. Suggested monitoring frequency
        
        Respond in JSON format.
        """
        
        try:
            response = self.model.generate_content(prompt)
            result = {
                'agent': self.name,
                'timestamp': datetime.now().isoformat(),
                'analysis': response.text,
                'status': 'success'
            }
            logger.info(f"{self.name}: Analysis complete")
            return result
        except Exception as e:
            logger.error(f"{self.name}: Error - {str(e)}")
            return {'agent': self.name, 'status': 'error', 'error': str(e)}

class RecommendationAgent:
    """Agent 2: Provides personalized wellness recommendations"""
    
    def __init__(self):
        self.name = "RecommendationEngine"
        self.model = genai.GenerativeModel('gemini-pro')
        logger.info(f"{self.name} initialized")
    
    def generate_recommendations(self, user_profile: Dict[str, Any], health_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Generate personalized health recommendations"""
        logger.info(f"{self.name}: Generating recommendations")
        
        prompt = f"""
        Based on the user profile and health analysis, provide personalized recommendations:
        
        User Profile:
        - Age: {user_profile.get('age', 'N/A')}
        - Fitness Goal: {user_profile.get('fitness_goal', 'N/A')}
        - Dietary Preferences: {user_profile.get('dietary_preferences', 'N/A')}
        
        Health Analysis:
        {health_analysis.get('analysis', 'No analysis available')}
        
        Provide:
        1. 3 actionable nutrition tips
        2. 3 exercise recommendations
        3. 2 lifestyle adjustments
        
        Make recommendations specific and achievable.
        """
        
        try:
            response = self.model.generate_content(prompt)
            result = {
                'agent': self.name,
                'timestamp': datetime.now().isoformat(),
                'recommendations': response.text,
                'status': 'success'
            }
            logger.info(f"{self.name}: Recommendations generated")
            return result
        except Exception as e:
            logger.error(f"{self.name}: Error - {str(e)}")
            return {'agent': self.name, 'status': 'error', 'error': str(e)}

class MedicalKnowledgeAgent:
    """Agent 3: Answers medical questions using Gemini's knowledge"""
    
    def __init__(self):
        self.name = "MedicalQA"
        self.model = genai.GenerativeModel('gemini-pro')
        logger.info(f"{self.name} initialized")
    
    def answer_question(self, question: str) -> Dict[str, Any]:
        """Answer health-related questions"""
        logger.info(f"{self.name}: Processing question")
        
        prompt = f"""
        As a medical information assistant, answer this health question accurately:
        
        Question: {question}
        
        Provide:
        1. Clear, evidence-based answer
        2. Important disclaimers
        3. When to consult a healthcare professional
        
        Note: Always emphasize this is informational and not a substitute for professional medical advice.
        """
        
        try:
            response = self.model.generate_content(prompt)
            result = {
                'agent': self.name,
                'timestamp': datetime.now().isoformat(),
                'question': question,
                'answer': response.text,
                'status': 'success'
            }
            logger.info(f"{self.name}: Question answered")
            return result
        except Exception as e:
            logger.error(f"{self.name}: Error - {str(e)}")
            return {'agent': self.name, 'status': 'error', 'error': str(e)}

class CoordinationAgent:
    """Agent 4: Orchestrates multi-agent communication (A2A Protocol)"""
    
    def __init__(self):
        self.name = "Coordinator"
        self.health_monitor = HealthMonitoringAgent()
        self.recommender = RecommendationAgent()
        self.medical_qa = MedicalKnowledgeAgent()
        self.session_memory = {}  # Day 3: Session management
        logger.info(f"{self.name} initialized with all sub-agents")
    
    def create_session(self, user_id: str) -> str:
        """Create a new user session with memory"""
        session_id = f"session_{user_id}_{datetime.now().timestamp()}"
        self.session_memory[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now().isoformat(),
            'interactions': []
        }
        logger.info(f"{self.name}: Session {session_id} created")
        return session_id
    
    def process_health_check(self, session_id: str, user_data: Dict[str, Any], user_profile: Dict[str, Any]) -> Dict[str, Any]:
        """Coordinate complete health check workflow"""
        logger.info(f"{self.name}: Starting health check workflow")
        
        workflow_result = {
            'session_id': session_id,
            'workflow': 'health_check',
            'timestamp': datetime.now().isoformat(),
            'steps': []
        }
        
        # Step 1: Health monitoring
        health_analysis = self.health_monitor.analyze_health_data(user_data)
        workflow_result['steps'].append(health_analysis)
        
        # Step 2: Generate recommendations based on analysis
        if health_analysis['status'] == 'success':
            recommendations = self.recommender.generate_recommendations(user_profile, health_analysis)
            workflow_result['steps'].append(recommendations)
        
        # Store in session memory
        if session_id in self.session_memory:
            self.session_memory[session_id]['interactions'].append(workflow_result)
        
        logger.info(f"{self.name}: Health check workflow complete")
        return workflow_result
    
    def handle_question(self, session_id: str, question: str) -> Dict[str, Any]:
        """Handle medical Q&A through dedicated agent"""
        logger.info(f"{self.name}: Routing question to Medical QA agent")
        
        result = self.medical_qa.answer_question(question)
        
        # Store in session memory
        if session_id in self.session_memory:
            self.session_memory[session_id]['interactions'].append(result)
        
        return result
    
    def get_session_summary(self, session_id: str) -> Dict[str, Any]:
        """Retrieve session history (Day 3: Memory)"""
        if session_id in self.session_memory:
            return self.session_memory[session_id]
        return {'error': 'Session not found'}

# Main TechHealth System
class TechHealthSystem:
    """Main system orchestrating all agents"""
    
    def __init__(self):
        self.coordinator = CoordinationAgent()
        logger.info("TechHealth System initialized")
    
    def start_wellness_session(self, user_id: str, user_profile: Dict[str, Any]) -> str:
        """Start a new wellness consultation session"""
        session_id = self.coordinator.create_session(user_id)
        logger.info(f"Wellness session started for user {user_id}")
        return session_id
    
    def perform_health_check(self, session_id: str, health_data: Dict[str, Any], user_profile: Dict[str, Any]) -> Dict[str, Any]:
        """Perform comprehensive health assessment"""
        return self.coordinator.process_health_check(session_id, health_data, user_profile)
    
    def ask_medical_question(self, session_id: str, question: str) -> Dict[str, Any]:
        """Get answer to medical question"""
        return self.coordinator.handle_question(session_id, question)
    
    def get_session_history(self, session_id: str) -> Dict[str, Any]:
        """Retrieve complete session history"""
        return self.coordinator.get_session_summary(session_id)

# Example Usage
if __name__ == "__main__":
    print("=== TechHealth AI Wellness Assistant ===")
    print("Multi-Agent Healthcare Solution Demo\n")
    
    # Initialize system
    system = TechHealthSystem()
    
    # User profile
    user_profile = {
        'age': 28,
        'fitness_goal': 'Weight loss and cardiovascular health',
        'dietary_preferences': 'Vegetarian'
    }
    
    # Start session
    session_id = system.start_wellness_session("user_123", user_profile)
    print(f"Session ID: {session_id}\n")
    
    # Health data
    health_data = {
        'heart_rate': 82,
        'blood_pressure': '130/85',
        'sleep_hours': 6,
        'activity_level': 'Moderate'
    }
    
    # Perform health check
    print("Performing health assessment...")
    health_check = system.perform_health_check(session_id, health_data, user_profile)
    print(json.dumps(health_check, indent=2))
    
    # Ask a medical question
    print("\nAsking medical question...")
    question = "What are the benefits of regular cardiovascular exercise?"
    qa_response = system.ask_medical_question(session_id, question)
    print(json.dumps(qa_response, indent=2))
    
    # Get session summary
    print("\nRetrieving session history...")
    history = system.get_session_history(session_id)
    print(f"Total interactions: {len(history.get('interactions', []))}")
    
    print("\nDemo complete! TechHealth system successfully demonstrated multi-agent coordination.")
