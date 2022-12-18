def transform_data(data):
    # Filter out rows with missing values
    data = [row for row in data if None not in row]
    # Transform tuple to list
    data = list(data)
    print(data)
    # Apply transformations to the data

    return data
