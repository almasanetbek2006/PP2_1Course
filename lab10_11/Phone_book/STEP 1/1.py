import psycopg2

conn = psycopg2.connect(host="localhost", dbname="MyContacts", user = "postgres",
                        password="m53371893",port=5432)

cur = conn.cursor()

conn.set_session(autocommit=True)

cur.execute('DROP TABLE contacts ;')

conn.commit()

cur.execute("""
    CREATE TABLE contacts (
    name VARCHAR(255),
    phone_number VARCHAR(255) PRIMARY KEY
    ):
""")

conn.commit()




