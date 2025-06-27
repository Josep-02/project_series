import sqlite3

DATABASE = 'database.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS persona (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            edad INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Esto permite acceder a las columnas por nombre
    return conn

# Funciones CRUD para Persona
def get_all_personas():
    conn = get_db_connection()
    personas = conn.execute('SELECT * FROM persona').fetchall()
    conn.close()
    return personas

def get_persona_by_id(persona_id):
    conn = get_db_connection()
    persona = conn.execute('SELECT * FROM persona WHERE id = ?', (persona_id,)).fetchone()
    conn.close()
    return persona

def create_persona(nombre, apellido, edad):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO persona (nombre, apellido, edad) VALUES (?, ?, ?)', (nombre, apellido, edad))
    conn.commit()
    persona_id = cursor.lastrowid
    conn.close()
    return persona_id

def update_persona(persona_id, nombre, apellido, edad):
    conn = get_db_connection()
    conn.execute('UPDATE persona SET nombre = ?, apellido = ?, edad = ? WHERE id = ?', (nombre, apellido, edad, persona_id))
    conn.commit()
    conn.close()

def delete_persona(persona_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM persona WHERE id = ?', (persona_id,))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Base de datos inicializada y tabla 'persona' creada (si no existía).")