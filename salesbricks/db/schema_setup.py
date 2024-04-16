import psycopg2

def create_tables(conn):
    """Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE tenants (
            tenant_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
        """,
        """ 
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            tenant_id INT NOT NULL,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            CONSTRAINT fk_tenant FOREIGN KEY (tenant_id)
                REFERENCES tenants (tenant_id) ON DELETE CASCADE
        );
        """,
        """
        CREATE TABLE orders (
            order_id SERIAL PRIMARY KEY,
            user_id INT NOT NULL,
            tenant_id INT NOT NULL,
            status VARCHAR(100),
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_user FOREIGN KEY (user_id)
                REFERENCES users (user_id) ON DELETE CASCADE,
            CONSTRAINT fk_tenant FOREIGN KEY (tenant_id)
                REFERENCES tenants (tenant_id) ON DELETE CASCADE
        );
        """,
        """
        CREATE OR REPLACE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = now();
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
        """,
        """
        CREATE TRIGGER update_orders_updated_at BEFORE UPDATE
        ON orders FOR EACH ROW
        EXECUTE FUNCTION update_updated_at_column();
        """,
        """
        CREATE TABLE events (
            event_id SERIAL PRIMARY KEY,
            order_id INT NOT NULL,
            type VARCHAR(100) NOT NULL,
            timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            details JSONB,
            CONSTRAINT fk_order FOREIGN KEY (order_id)
                REFERENCES orders (order_id) ON DELETE CASCADE
        );
        """
    )
    try:
        cursor = conn.cursor()
        # Create table one by one
        for command in commands:
            cursor.execute(command)
        cursor.close()  # Close communication with the PostgreSQL database server
        conn.commit()  # Commit the changes
        print("Tables and triggers created successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def main():
    conn = psycopg2.connect(host='localhost', database='salesbricks_db', user='jimmy', password='admin')
    if conn is not None:
        create_tables(conn)
        conn.close()
    else:
        print("Cannot create the database connection.")

if __name__ == '__main__':
    main()