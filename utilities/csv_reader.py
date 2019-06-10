import csv

def get_csv_data(filename):
    # Define an empty list of rows
    all_rows = []

    # Read the input csv file in read mode
    input_file = open(filename, "r")

    # Define a reader to read rows from the csv file
    reader = csv.reader(input_file)

    # Skip the header by going to second row, by using the 'next()' method
    next(reader)

    # Read all other rows into the empty list , and return the contents
    for row in reader:
        all_rows.append(row)
    return all_rows