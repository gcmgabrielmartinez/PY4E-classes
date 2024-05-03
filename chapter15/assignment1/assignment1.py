import sqlite3

conn = sqlite3.connect('ages.sqlite')
cur = conn.cursor()

cur.execute('''
            DROP TABLE IF EXISTS Ages''')

cur.execute('''
            CREATE TABLE Ages (name TEXT, age INTEGER)''')

cur.executescript('''
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Danial', 18);
INSERT INTO Ages (name, age) VALUES ('Leland', 20);
INSERT INTO Ages (name, age) VALUES ('Shanai', 35);
INSERT INTO Ages (name, age) VALUES ('Saif', 29);
INSERT INTO Ages (name, age) VALUES ('Mitchel', 28);
''')

cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')

result = cur.fetchone()[0]
print(result)
cur.close()