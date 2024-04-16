import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_connection():
    """Create a database connection to the PostgreSQL database"""
    conn = None
    try:
        # Connect to the default 'postgres' database to perform administrative tasks
        conn = psycopg2.connect(
            host='localhost',
            database='postgres',  # default administrative database
            user='jimmy',
            password='admin'
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL database: {e}")

def create_database(conn, db_name):
    """Create a database if it does not exist"""
    try:
        cursor = conn.cursor()
        # Check if the database already exists to avoid errors
        cursor.execute("SELECT 1 FROM pg_database WHERE datname=%s", (db_name,))
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
            print(f"Database {db_name} created successfully")
        cursor.close()
    except Exception as e:
        print(f"Failed to create database {db_name}: {e}")

def main():
    database = "salesbricks_db"  # The desired database name
    conn = create_connection()
    if conn is not None:
        create_database(conn, database)
        # Close the initial connection
        conn.close()
        # Connect to the newly created database to set up tables
        conn = psycopg2.connect(
            host='localhost',
            database=database,
            user='jimmy',
            password='admin'
        )
        # Example: Function to create tables could be called here
        # create_tables(conn)
        conn.close()
    else:
        print("Cannot create the database connection.")

if __name__ == '__main__':
    main()
