# backend/main_script.py (Notion Version)
# ... (imports remain the same, but import the Notion notifier)
from notifier import add_summary_to_notion 

def run_tracker():
    # ... (competitors dictionary and db connection are the same)
    
    for name, url in competitors.items():
        print(f"Scraping {name} from {url}...")
        scraped_text = scrape_website(url)
        
        if scraped_text:
            print(f"Analyzing content for {name}...")
            summary = summarize_with_ai(scraped_text, name)
            print(f"Summary for {name}:\n{summary}\n")
            
            # Save to local database
            cursor.execute(
                "INSERT INTO summaries (competitor, summary, source_url) VALUES (?, ?, ?)",
                (name, summary, url)
            )
            conn.commit()

            # ✅ SEND THIS UPDATE DIRECTLY TO NOTION
            add_summary_to_notion(name, summary, url)
            
        else:
            print(f"Could not scrape {name}.")

    conn.close()

if __name__ == '__main__':
    run_tracker()