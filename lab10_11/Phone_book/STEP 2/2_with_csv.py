import psycopg2
import csv

conn = psycopg2.connect(host="localhost", dbname="MyContacts", user = "postgres",
                        password="m53371893",port=5432)

cur = conn.cursor()

conn.set_session(autocommit=True)

cur.execute('DROP TABLE contacts_2;')

conn.commit()

cur.execute("""
    CREATE TABLE contacts_2 (
    name VARCHAR(255),
    phone_number VARCHAR(22) PRIMARY KEY    
    );
""")

file = "contacts.csv"

with open(file, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)

        name, phone_number = row

         
        cur.execute(f"""INSERT INTO contacts_2 (name, phone_number) VALUES ('{name}','{phone_number}');""")

conn.commit()
