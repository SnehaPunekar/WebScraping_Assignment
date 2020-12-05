import csv
import psycopg2
conn = psycopg2.connect(host="localhost", dbname="test", user="postgres", password="1248")
print("Connected..!!")

cur = conn.cursor()

#If the table "branches" already exist in your database. Uncomment the following two lines.
#Else you can also change the name of the table.

cur.execute("DROP TABLE branches")
#print("DROP TABLE")

cur.execute("""
    CREATE TABLE branches(
    id serial primary key,
    beyond_bank_branches text
)
""")
print("\nCREATE TABLE\n")

with open('Stores.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # We have to skip the header row..!!

    for row in reader:
        cur.execute("INSERT INTO branches(beyond_bank_branches) VALUES (%s)",row)
        print("Inserted..!!")

#For retrieving the details.

#print("Table Contents are:\n")

#cur.execute("SELECT * FROM branches")
#result = cur.fetchall();
#print(result)

conn.commit()
conn.close()