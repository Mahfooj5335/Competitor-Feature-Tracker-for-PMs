# backend/analyzer.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv() # Load environment variables from .env file

def summarize_with_ai(text_content, competitor_name):
    """Summarizes text to find product updates using Gemini."""
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file")
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')

        prompt = f"""
        Analyze the following text from {competitor_name}'s website or changelog.
        Identify and summarize any new features, product updates, pricing changes, or changes in product messaging.
        Focus only on concrete changes. If no significant updates are found, state that.
        Present the summary as a clean, bulleted list.

        TEXT:
        ---
        {text_content[:8000]} 
        ---
        """
        # We slice the text to avoid exceeding API limits

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print(f"An error occurred during AI analysis: {e}")
        return "Error: Could not generate summary."