import psycopg2

conn = psycopg2.connect('dbname=example')

# cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing todos table
cur.execute("DROP TABLE IF EXISTS todos;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE todos (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")

cur.execute('INSERT INTO todos (id,description) VALUES (%s,%s);', (1, True))
SQL='INSERT INTO todos (id,description)values(%(id)s,%(description)s);'
DATA={
    'id':2,
    'description':False
}

cur.execute(SQL,DATA)

cur.execute('select * from todos;')
result=cur.fetchall()
print(result)



# commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()
