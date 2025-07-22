# backend/app.py
from flask import Flask, render_template, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__, template_folder='templates')
CORS(app)

def get_competitor_data():
    return [
        {
            "name": "Monday.com",
            "url": "https://monday.com",
            "category": "Project Management",
            "status": "Active",
            "features": ["Task Management", "Team Collaboration", "Automation"],
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "name": "ClickUp",
            "url": "https://clickup.com",
            "category": "Project Management",
            "status": "Active",
            "features": ["Project Planning", "Docs", "Goals"],
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        {
            "name": "Notion",
            "url": "https://notion.so",
            "category": "Workspace",
            "status": "Active",
            "features": ["Notes", "Databases", "Wiki"],
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    ]

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
            "name": "Basecamp",
            "url": "https://basecamp.com/",
            "category": "Project Management"
        },
        {
            "name": "Smartsheet",
            "url": "https://www.smartsheet.com/",
            "category": "Project Management"
        },
        {
            "name": "Wrike",
            "url": "https://www.wrike.com/",
            "category": "Project Management"
        },
        {
            "name": "Airtable",
            "url": "https://airtable.com/",
            "category": "Database/Project Management"
        },
        {
            "name": "Linear",
            "url": "https://linear.app/",
            "category": "Project Management"
        },
        {
            "name": "Height",
            "url": "https://height.app/",
            "category": "Project Management"
        }
    ]
    
    for comp in competitors:
        soup = safe_scrape(comp["url"])
        if soup:
            features = []
            pricing = []
            updates = []
            
            # Look for various content types
            feature_elements = soup.select('h2, h3, .feature-title, .headline, .feature-card')
            pricing_elements = soup.select('.pricing, .price, .plan-price, .pricing-card')
            update_elements = soup.select('.update, .new-feature, .blog-post, .whats-new')
            
            # Extract features
            for elem in feature_elements[:5]:
                text = elem.get_text().strip()
                if text and len(text) > 5 and text not in features:
                    features.append(text)
            
            # Extract pricing
            for price in pricing_elements[:3]:
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


