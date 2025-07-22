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
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        return BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")
        return None

def get_competitor_data():
    competitors = [
        {
            "name": "Monday.com",
            "url": "https://monday.com",
            "category": "Project Management"
        },
        {
            "name": "ClickUp",
            "url": "https://clickup.com",
            "category": "Project Management"
        },
        {
            "name": "Notion",
            "url": "https://notion.so",
            "category": "Workspace"
        },
        {
            "name": "Basecamp",
            "url": "https://basecamp.com",
            "category": "Project Management"
        },
        {
            "name": "Smartsheet",
            "url": "https://www.smartsheet.com",
            "category": "Project Management"
        },
        {
            "name": "Wrike",
            "url": "https://www.wrike.com",
            "category": "Project Management"
        },
        {
            "name": "Linear",
            "url": "https://linear.app",
            "category": "Project Management"
        }
    ]
    
    for comp in competitors:
        soup = safe_scrape(comp["url"])
        if soup:
            features = []
            feature_elements = soup.select('h2, h3, .feature-title, .headline')
            
            for elem in feature_elements[:5]:
                text = elem.get_text().strip()
                if text and len(text) > 5:
                    features.append(text)
            
            comp.update({
                "features": features if features else ["Visit website for features"],
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": "Active"
            })
        else:
            comp.update({
                "features": ["Unable to fetch data"],
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": "Error"
            })
        time.sleep(1)
    
    return competitors

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({
        "status": "active",
        "agent": "AI Competitor Tracker",
        "version": "1.0",
        "last_scan": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route('/api/competitors')
def get_competitors():
    return jsonify(get_competitor_data())

if __name__ == '__main__':
    app.run(debug=True, port=5001)
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
                "pricing": pricing if pricing else ["Pricing information not available"],
                "updates": updates if updates else ["No recent updates found"],
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": "Active"
            })
        else:
            comp.update({
                "features": ["Unable to fetch data"],
                "pricing": ["Unable to fetch pricing"],
                "updates": ["Unable to fetch updates"],
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": "Error"
            })
        
        time.sleep(1)
    
    return competitors

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({
        "status": "active",
        "agent": "AI Competitor Tracker",
        "version": "1.0",
        "last_scan": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route('/api/competitors')
def get_competitors():
    return jsonify(scrape_competitor_data())

if __name__ == '__main__':
    app.run(debug=True, port=5001)


