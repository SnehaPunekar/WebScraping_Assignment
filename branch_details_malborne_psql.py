import csv
import psycopg2
conn = psycopg2.connect(host="localhost", dbname="test", user="postgres", password="1248")
print("Connected..!!")

cur = conn.cursor()


#If the table "branch_details" already exist in your database. Uncomment the following two lines.
#Else you can also change the name of the table.

cur.execute("DROP TABLE branch_details")
#print("DROP TABLE")

cur.execute("""
    CREATE TABLE branch_details(
    id serial primary key,
    store_name text,
    lattitude numeric,
    longitude numeric,
    postal_code int,
    suburb text,
    city text,
    country text,
    url_details text,
    phone_number text,
    off_days text
)
""")
print("\nCREATE TABLE\n")

with open('Store_Details.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # We have to skip the header row..!!

    for row in reader:
        cur.execute("INSERT INTO branch_details(store_name, lattitude, longitude, postal_code, suburb, city, country, url_details, phone_number, off_days) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",row)
        print("Inserted..!!")


#For retrieving the details.

#print("Table Contents are:\n")

#cur.execute("SELECT * FROM branch_details")
#result = cur.fetchall();
#print(result)

conn.commit()
conn.close()