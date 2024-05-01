import psycopg2
import csv

conn = psycopg2.connect(host="localhost", dbname="MyContacts", user = "postgres",
                        password="m53371893",port=5432)

cur = conn.cursor()

conn.set_session(autocommit=True)

cur.execute('DROP TABLE contacts_4;')

conn.commit()


cur.execute("""
    CREATE TABLE contacts_4(
    name VARCHAR(255),
    phone_number VARCHAR(22) PRIMARY KEY    
    );
""")

file = "contacts2.csv"

with open(file, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        #print(row)

        name,phone_number = row

         
        cur.execute(f"""INSERT INTO contacts_4 (name, phone_number) VALUES ('{name}','{phone_number}');""")


cur.execute("""
    SELECT * FROM contacts_4 ORDER BY name DESC ;
""")

#print(cur.fetchall())

cur.execute("""
    SELECT * FROM contacts_4 WHERE name LIKE 'A%' ;
""")

print(cur.fetchall())

#cur.execute("""
#    SELECT * FROM contacts_4 WHERE name LIKE '%s' ;
#""")

#print(cur.fetchall())

conn.commit()
