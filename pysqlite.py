'''Python CRUD operations for sqlite db'''
import sqlite3

conn = sqlite3.connect('crud.db')
c = conn.cursor()

#create a table

try:
    c.execute('''
            CREATE TABLE tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            priority INTEGER NOT NULL);''')
    print('Table created')
except:
    print('Database Already exists')



# INSERT DATA IN TABLE
c.execute('INSERT INTO tasks (name,priority) VALUES (?,?)', ('first task', 1))
conn.commit()
print('One row inserted')

#INSERT MANY DATA

data = [('Second task',2),('Third task',2),('Fourth task',2),('Fifth task',2),('Sixth task',2)]
c.executemany('INSERT INTO tasks (name, priority) VALUES (?,?)',data)
conn.commit()
print('Multiple rows inserted')

# Read from database

c.execute('SELECT * FROM tasks')
result = c.fetchall()

print(result)

c.execute('''UPDATE tasks SET name='first task updated' WHERE rowid=1;
            ''')
conn.commit()


c.execute('SELECT rowid, * FROM tasks')
result = c.fetchall()
print(result)

c.execute('SELECT rowid, * FROM tasks ORDER BY rowid DESC')
result = c.fetchall()
print(result)

c.execute('SELECT rowid, * FROM tasks LIMIT 3,7')
result = c.fetchall()
print(result)


#finally drop the table
#c.execute('''DROP TABLE tasks;''')
#print('Table deleted. Thank You!')
