import sqlite3

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usersTab (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT,
            lastname TEXT,
            username TEXT UNIQUE,
            password TEXT,
            type TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS favoritesTab (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            cost INTEGER,
            FOREIGN KEY(vacationID) REFERENCES vacationTab(id)
            FOREIGN KEY(pictureURL) REFERENCES vacationTab(pictureURL)
        )
    ''')
# for favorites, text = accommodation, flight, activity, restaurants

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS planTab (
            planID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            cost INTEGER,
            location TEXT,
            date TEXT,
            time TEXT,
            available BOOLEAN,
            FOREIGN KEY(userID) REFERENCES usersTab(id),
            FOREIGN KEY(vacationID) REFERENCES vacationTab(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vacationTab (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            breed TEXT,
            age INTEGER,
            pictureUrl TEXT,
            available BOOLEAN
        )
    ''')
    # type is same as favorites

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profileTab (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            FOREIGN KEY(userID) REFERENCES usersTab(id),
            FOREIGN KEY(username) REFERENCES usersTab(username),
            followers INTEGER,
            following INTEGER,
            type TEXT,
            pictureURL TEXT
        )
    ''')
    # type public or private

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS surveyTab (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            age INTEGER,
            pictureUrl TEXT,
            available BOOLEAN
            dateAvailability TEXT,
            timeAvailability TEXT
            costMin INTEGER,
            costMax INTEGER
        )
    ''')
    conn.commit()

def insert_sample_data(conn):
    cursor = conn.cursor()

    # Only insert if usersTab is empty
    cursor.execute("SELECT COUNT(*) FROM usersTab")
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO usersTab (username, password, type)
            VALUES (?, ?, ?)
        ''', ('Conrad_29', 'password123', 'public'))

        cursor.execute('''
            INSERT INTO usersTab (username, password, type)
            VALUES (?, ?, ?)
        ''', ('Arjona_02', 'wordpass321', 'admin'))

    # Only insert if petsTab is empty
    cursor.execute("SELECT COUNT(*) FROM petsTab")
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO petsTab (name, type, breed, personality, age, pictureUrl, available)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', ('Buddy', 'dog', 'Husky', 'friendly', 3, 'https://images.dog.ceo/breeds/husky/n02110185_9086.jpg', True))

        cursor.execute('''
            INSERT INTO petsTab (name, type, breed, personality, age, pictureUrl, available)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', ('Whiskers', 'cat', 'Tabby', 'shy', 2, 'https://cataas.com/cat', False))

        cursor.execute('''
            INSERT INTO petsTab (name, type, breed, personality, age, pictureUrl, available)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', ('Max', 'dog', 'Papillon', 'energetic', 5, 'https://images.dog.ceo/breeds/papillon/n02086910_4623.jpg', True))

    conn.commit()

def init_db():
    conn = sqlite3.connect('pets_adoption.db')
    create_tables(conn)
    insert_sample_data(conn)
    conn.close()
    print("Database initialized and sample data inserted.")

if __name__ == '__main__':
    init_db()
