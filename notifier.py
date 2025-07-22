# backend/notifier.py (Notion Version)
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def add_summary_to_notion(competitor, summary, source_url):
    """Adds a new row to a Notion database with the competitor summary."""
    api_key = os.getenv("NOTION_API_KEY")
    database_id = os.getenv("NOTION_DATABASE_ID")

    if not api_key or not database_id:
        print("Error: Notion API Key or Database ID not found in .env")
        return

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }
    
    # This payload structure is required by the Notion API
    new_page_data = {
        "parent": {"database_id": database_id},
        "properties": {
            "Competitor": {"title": [{"text": {"content": competitor}}]},
            "Summary": {"rich_text": [{"text": {"content": summary}}]},
            "Source": {"url": source_url},
        },
    }

    try:
        response = requests.post(
            "https://api.notion.com/v1/pages",
            headers=headers,
            data=json.dumps(new_page_data),
            timeout=10
        )
        response.raise_for_status()
        print(f"Successfully added {competitor} summary to Notion.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to Notion: {e}")