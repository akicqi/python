# --coding:utf-8--
import sqlite3

name = raw_input('Input:')

con = sqlite3.connect(test.db)

cur = con.cursor()

cur.execute('select * from student where name=?',(name,))

rows = cur.fetchall()
for row in rows:
	print row