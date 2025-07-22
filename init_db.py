import sqlite3

def init_db():
    conn = sqlite3.connect('tracker.db')
    c = conn.cursor()
    
    # Create summaries table
    c.execute('''
        CREATE TABLE IF NOT EXISTS summaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Insert some test data
    c.execute('''
        INSERT INTO summaries (title, content) VALUES 
        ('Test Summary 1', 'This is test content 1'),
        ('Test Summary 2', 'This is test content 2')
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully!")
