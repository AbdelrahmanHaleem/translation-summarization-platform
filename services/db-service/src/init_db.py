import psycopg2

def init_db():
    conn = psycopg2.connect(
        dbname="translation_platform",
        user="admin",
        password="password",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS logs (
            request_id SERIAL PRIMARY KEY,
            user_id INT REFERENCES users(id),
            input_text TEXT NOT NULL,
            output_text TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    init_db()

