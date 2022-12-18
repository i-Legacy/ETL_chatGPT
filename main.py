import mysql.connector
import extract
import load
import transform


def main():
    db = "springboot"
    host = "localhost"
    user = "root"
    pword = "admin"

    # Connect to the database
    cnx = mysql.connector.connect(
        user=user, password=pword, host=host, database=db
    )
    cursor = cnx.cursor()

    # Empty the user table, and print it empty
    cursor.execute("DELETE FROM destination")

    # Print the rows
    cursor.execute("SELECT * FROM destination")
    rows = cursor.fetchall()
    print("Table: \n")
    for row in rows:
        print(row)

    # Extract data from source
    data = extract.extract_data_from_source(cursor)

    # Transform the data
    transformed_data = transform.transform_data(data)

    # Load the data into the target database
    load.load_data_into_database(transformed_data, cursor, cnx)

    # Print the rows
    cursor.execute("SELECT * FROM destination")
    rows = cursor.fetchall()
    print("Table: \n")
    for row in rows:
        print(row)

    # Close the connection to the database
    cnx.close()


if __name__ == "__main__":
    main()
