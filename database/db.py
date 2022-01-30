import psycopg2

def execute_query(operation, name=None, location=None):

    connection = psycopg2.connect(
        user='postgres',
        password='admin',
        host='localhost',
        port='5432',
        database='flask'
    )
    cursor = connection.cursor()
    if operation == 'select':
        try:
            query = f"SELECT * FROM users where name='{name}';"
            cursor.execute(query)
            records = cursor.fetchone()
            cursor.close()
            connection.close()
            return f'{records}'
        except Exception as e:
            cursor.close()
            connection.close()
            return f'{e}'

    elif operation == 'insert':
        try:
            query = f"INSERT INTO users (name,location) VALUES ('{name}','{location}');"
            cursor.execute(query)
            connection.commit()
            cursor.close()
            connection.close()
            return f'User added successfully'
        except Exception as e:
            cursor.close()
            connection.close()
            return f'{e}'