import psycopg2

name = input("New name:")
phone_number = input("New phone number")

conn = psycopg2.connect(host="localhost", dbname="MyContacts", user = "postgres",
                        password="m53371893",port=5432)

cur = conn.cursor()

conn.set_session(autocommit=True)

#cur.execute('DROP TABLE contacts_1 ;')

#conn.commit()

cur.execute(""" 
    CREATE TABLE if not exists contacts_1 (
    name VARCHAR(255),
    phone_number VARCHAR(22) PRIMARY KEY    
    );  
""")

cur.execute(f""" 
    INSERT INTO contacts_1 (name,phone_number) VALUES ('{name}','{phone_number}')
""")

conn.commit()

