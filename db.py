import psycopg

conn_string = "dbname=cms user=postgres password= host=localhost"

def select(columns, table, where):
    with psycopg.connect(conn_string) as connection:
        with connection.cursor() as cursor:
            column_list = ", ".join(columns)
            where_string = f"WHERE {where[0]} {where[1]} {where[2]}" if where else ""
            query = f"SELECT {column_list} FROM {table} {where_string};"
            cursor.execute(query)

            result = cursor.fetchall()
    
    return result

def delete(table, where):
    connection = psycopg.connect(conn_string)

    with connection.cursor() as cursor:
        
        where_string = f"WHERE {where[0]} {where[1]} {where[2]}" if where else ""

        query = f"DELETE FROM {table} {where_string};"
        cursor.execute(query)

        result = cursor.fetchall()
    
    cursor.execute()
    connection.close()
    return result

def insert(table, columns, values):
    connection = psycopg.connect(conn_string)

    with connection.cursor() as cursor:

        column_list = ", ".join(columns)        
        value_string = f"VALUES {values}"

        query = f"INSERT INTO {table} ({column_list}) {value_string};"
        cursor.execute(query)

        result = cursor.fetchall()
    
    cursor.execute()
    connection.close()
    return result