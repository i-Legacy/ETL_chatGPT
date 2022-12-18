def load_data_into_database(data, cursor, cnx):
    # Construct the INSERT statement
    sql = "INSERT INTO destination"
    sql = sql + "(id, email, priority, username) VALUES (%s, %s, %s, %s)"
    print(sql)

    # Execute the INSERT statement for each row of data
    for row in data:
        print(row)
        cursor.execute(sql, row)

    # Commit the changes to the database
    cnx.commit()
