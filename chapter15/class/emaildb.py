import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
            DROP TABLE IF EXISTS Counts''')

cur.execute('''
            CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input("ENter file name: ")
if len(fname) < 1: fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith("From: "): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,)) #search for the email row
    row = cur.fetchone() #save the row data in a variable
    if row is None: #if not found
        cur.execute('''INSERT INTO Counts (email, count) VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,)) #as soon it os found, add 1
    conn.commit() #need to commit to actually modify the database

    sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10' #str of command line in sql

for row in cur.execute(sqlstr): #cur.execute() is got the data
    print(str(row[0]), row[1])

cur.close()