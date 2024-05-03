import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

#setting up
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
                                    
CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    email  TEXT
) ;

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
) ;

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
	role        INTEGER,
    PRIMARY KEY (user_id, course_id)
) 
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print(name, title, role)

    #insert a row in User table AND getting a foreign key to Member 
    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES (?)''', (name,) ) 
    #IGNORE means it will not do anything because it already exists in the database
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    #insert a row in Course table AND getting a foreign key to Member 
    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES (?)''', (title,) )
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

                
    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?,?,?)''',
    (user_id, course_id, role))
    #caution: if user_id, course_id already exists, it updates by REPLACE!

    conn.commit()

sqlstr =  '''SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
'''
    
for result in cur.execute(sqlstr):
    print(result)

cur.execute('''SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;''')

answer = cur.fetchone()[0]
print(answer)
#challenge: insert variable role