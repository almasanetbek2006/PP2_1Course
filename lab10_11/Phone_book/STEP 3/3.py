import psycopg2
import csv

conn = psycopg2.connect(host="localhost", dbname="MyContacts", user = "postgres",
                        password="m53371893",port=5432)

cur = conn.cursor()

conn.set_session(autocommit=True)

cur.execute('DROP TABLE contacts_3;')

conn.commit()

cur.execute("""
    CREATE TABLE contacts_3 (
    name VARCHAR(255),
    phone_number VARCHAR(22) PRIMARY KEY    
    );
""")

cur.execute("""
            INSERT INTO contacts_3 (name,phone_number) VALUES ('Rodrygo','+46664544');
""")

#cur.execute("""
#            UBDATE contacts_3 SET name  = 'Zidan' WHERE phone_number = '+46664544';
#""")

cur.execute("""
            UPDATE contacts_3 SET name = 'Zidan'  WHERE name = 'Rodrygo';
""")



