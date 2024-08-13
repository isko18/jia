import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Выполняем запрос для создания таблицы
cursor.execute('''
CREATE TABLE base_slidertitle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    title_ru VARCHAR(255),
    title_ky VARCHAR(255),
    title_en VARCHAR(255)
);
''')

conn.commit()
conn.close()
