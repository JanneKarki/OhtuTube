from database_connection import get_database_connection


def drop_tables(parameter):

    cursor = parameter.cursor()
    print(parameter)
    cursor.execute("DROP TABLE IF EXISTS Books")

    parameter.commit()


def create_tables(connection):

    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE Books(
                    reference_id text,
                    author text, 
                    title text, 
                    year integer, 
                    publisher text,
                    address text,
                    reference_datetime DATETIME DEFAULT CURRENT_TIMESTAMP
                    )""")


    connection.commit()


def initialize_database(test_db=None):
    if not test_db:
        connection = get_database_connection()
        drop_tables(connection)
        create_tables(connection)
    else:
        connection = get_database_connection(test_db)
        drop_tables(connection)
        create_tables(connection)

if __name__ == "__main__":
    initialize_database()
