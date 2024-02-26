import sqlite3

con = sqlite3.connect('users.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE users(NAME, ID, POINTS)")
cur.execute("""INSERT INTO users VALUES
            ('Steve Smith', 211, 80), 
            ('Jian Wong', 122, 92), 
            ('Chris Peterson', 213, 91),
            ('Sai Patel', 524, 94), 
            ('Andrew Whitehead', 425, 99), 
            ('Lynn Roberts', 626, 90), 
            ('Robert Sanders' , 287, 75)
            """)
con.commit()
cur.close()