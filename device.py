import sqlite3

def create_db():
    conn = sqlite3.connect('devices.db')  # Cambia el nombre si es necesario
    c = conn.cursor()
    
    # Crear tabla si no existe
    c.execute('''
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY,
            ip TEXT,
            hostname TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
