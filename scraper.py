# backend/scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """Scrapes the text content from a given URL."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Raises an HTTPError for bad responses

        soup = BeautifulSoup(response.content, 'html.parser')

        # THIS IS THE PART YOU MUST CUSTOMIZE
        # Find the main content area. You need to inspect the competitor's
        # changelog page to find the right tag and class.
        # Example for a generic blog/changelog page:
        content_area = soup.find('article') or soup.find('main')
        
        if not content_area:
            return "Could not find main content area. The website structure might have changed."
            
        # Get text and clean it up
        text = ' '.join(content_area.get_text(separator=' ', strip=True).split())
        return text

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None