#Code Author: José Carlos del Castillo Estrada

#Excercise solved from the book "Python for Everybody" by Dr. Charles R. Severance
#Following the Coursera program "Using Databases with Python" by the University of Michigan
'''
Count the number of emails sent by each domain and order them in a DESC way.
The data extracted is obtained from mbox.txt 
'''

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
count = 0
fh = open(fname)#r'C:\users\Path\file\Using Python Databases with Python\Week 2\mbox.txt')
for line in fh:
    if not line.startswith('From: '): continue
    count = count + 1
    pieces = line.split()
    email = pieces[1].split('@')
    org = email[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    
# https://www.sqlite.org/lang_select.html
conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
print(count)
cur.close()