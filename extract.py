# Extract function
def extract_data_from_source(cursor):
    # Execute a SQL query to retrieve the data
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()

    return data
