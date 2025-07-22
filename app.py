
# backend/app.py
from flask import Flask, render_template, jsonify
from flask_cors import CORS
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__, template_folder='templates')
CORS(app)

def safe_scrape(url):
    """Safely scrapes a URL and returns a BeautifulSoup object or None."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {str(e)}")
        return None

# The function name is kept as get_competitor_data from your original script
def get_competitor_data():
    """Scrapes a list of competitor websites for features, pricing, and updates."""
    competitors = [
        {"name": "Monday.com", "url": "https://monday.com", "category": "Project Management"},
        {"name": "ClickUp", "url": "https://clickup.com", "category": "Project Management"},
        {"name": "Notion", "url": "https://notion.so", "category": "Workspace"},
        {"name": "Basecamp", "url": "https://basecamp.com", "category": "Project Management"},
        {"name": "Smartsheet", "url": "https://www.smartsheet.com", "category": "Project Management"},
        {"name": "Wrike", "url": "https://www.wrike.com", "category": "Project Management"},
        {"name": "Linear", "url": "https://linear.app", "category": "Project Management"}
    ]
    
    for comp in competitors:
        soup = safe_scrape(comp["url"])
        
        if soup:
            # Initialize lists for data
            features = []
            pricing = []
            updates = []
            
            # Define CSS selectors to find the data
            # NOTE: These are generic and MUST be customized for each site
            feature_elements = soup.select('h2, h3, .feature-title, .headline')
            price_elements = soup.select('.price, .pricing-plan, .plan-title')
            update_elements = soup.select('.release-note, .update-item, .changelog-entry')

            # Extract features
            for elem in feature_elements[:5]:
                text = elem.get_text().strip()
                if text and len(text) > 5 and text not in features:
                    features.append(text)
            
            # Extract pricing
            for price in price_elements[:3]:
                text = price.get_text().strip()
                if text and text not in pricing:
                    pricing.append(text)
            
            # Extract recent updates
            for update in update_elements[:3]:
                text = update.get_text().strip()
                if text and text not in updates:
                    updates.append(text)
            
            comp.update({
                "features": features if features else ["Visit website for features"],
                "pricing": pricing if pricing else ["Pricing info not available"],
                "updates": updates if updates else ["No recent updates found"],
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": "Active"
            })
        else:
            # Handle cases where scraping fails
            comp.update({
                "features": ["Unable to fetch data"],
                "pricing": ["Unable to fetch pricing"],
                "updates": ["Unable to fetch updates"],
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": "Error"
            })
        
        time.sleep(1) # Be polite and wait 1 second between requests
    
    return competitors

@app.route('/')
def home():
    """Renders the main HTML page."""
    return render_template('index.html')

@app.route('/api/status')
def status():
    """Provides the status of the tracking agent."""
    return jsonify({
        "status": "active",
        "agent": "AI Competitor Tracker",
        "version": "1.0",
        "last_scan": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route('/api/competitors')
def get_competitors():
    """The API endpoint to get competitor data."""
    # This now correctly calls the single data function
    return jsonify(get_competitor_data())

if __name__ == '__main__':
    app.run(debug=True, port=5001)
