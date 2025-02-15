0import csv
import pandas as pd
import os
import sqlite3


# Reset Database
def reset_database():
    conn = sqlite3.connect('registration_data.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS registrations')
    conn.commit()
    conn.close()


# Insert Data into DB from CSV/Excel
def insert_data_into_db(file_path):
    conn = sqlite3.connect('registration_data.db')
    cursor = conn.cursor()

    # Create the table with dynamic department columns
    with open(file_path, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader)

        # Create table query with department names as columns
        columns = ', '.join([f"{department} TEXT" for department in headers])
        create_table_query = f"CREATE TABLE IF NOT EXISTS registrations ({columns})"
        cursor.execute(create_table_query)

        # Insert data into the table
        for row in csv_reader:
            placeholders = ', '.join(['?' for _ in row])
            insert_query = f"INSERT INTO registrations VALUES ({placeholders})"
            cursor.execute(insert_query, row)

    conn.commit()
    print(f"Data from {file_path} inserted into the database.")
    conn.close()


# Fetch Data from DB
def fetch_data_from_db():
    conn = sqlite3.connect('registration_data.db')
    cursor = conn.cursor()

    # Fetch all data from the table
    cursor.execute('SELECT * FROM registrations')
    rows = cursor.fetchall()

    # Get column names
    columns = [description[0] for description in cursor.description]
    registration_dict = {column: [] for column in columns}

    # Populate the dictionary
    for row in rows:
        for column, value in zip(columns, row):
            if value:  # Avoid empty values
                registration_dict[column].append(value)

    conn.close()
    return registration_dict


# Convert Excel to CSV
def convert_excel_to_csv(excel_path):
    try:
        df = pd.read_excel(excel_path)
        csv_file_path = os.path.splitext(excel_path)[0] + '.csv'
        df.to_csv(csv_file_path, index=False)
        print(f"Excel file converted to CSV: {csv_file_path}")
        return csv_file_path
    except Exception as e:
        print(f"An error occurred while converting Excel to CSV: {e}")
        return None


# Allocate Seats based on department mapping and hall patterns
def allocate_seats(register_numbers, hall_patterns):
    department_iterators = {department: iter(register_numbers[department]) for department in register_numbers}
    hall_allocations = {hall: [['' for _ in range(len(pattern))] for pattern in hall_patterns[hall]] for hall in hall_patterns}

    for hall_name, pattern in hall_patterns.items():
        num_rows = len(pattern)
        num_cols = len(pattern[0])
        for col_index in range(num_cols):
            for row_index in range(num_rows):
                department_id = int(pattern[row_index][col_index])
                department = department_map[department_id]
                student_id = next(department_iterators[department], "No Student")
                hall_allocations[hall_name][row_index][col_index] = student_id
    return hall_allocations


# Department Mapping (You can change this as per your requirement)
department_map = {1: "CSE", 2: "MECH", 3: "AIDS", 4: "CSBS"}

# Hall Patterns
hall_patterns = {
    "HALL_1": [
        ["1", "3", "2", "3", "1"],
        ["2", "4", "1", "4", "2"],
        ["1", "3", "2", "3", "1"],
        ["2", "4", "1", "4", "2"],
        ["1", "3", "2", "3", "1"]
    ],
    "HALL_2": [
        ["4", "1", "3", "2", "4"],
        ["3", "2", "4", "1", "3"],
        ["4", "1", "3", "2", "4"],
        ["3", "2", "4", "1", "3"],
        ["4", "1", "3", "2", "4"]
    ],
    "HALL_3": [
        ["2", "4", "2", "3", "4"],
        ["1", "3", "1", "2", "1"],
        ["2", "4", "4", "3", "4"],
        ["1", "3", "1", "2", "1"],
        ["2", "4", "2", "3", "4"]
    ],
    "HALL_4": [
        ["3", "1", "2", "4", "3", "1", "2", "4", "3", "1"],
        ["2", "4", "3", "1", "2", "4", "3", "1", "2", "4"],
        ["3", "1", "2", "4", "3", "1", "2", "4", "3", "1"],
        ["2", "4", "3", "1", "2", "4", "3", "1", "2", "4"],
        ["3", "1", "2", "4", "3", "1", "2", "4", "3", "1"]
    ],
    "HALL_5": [
        ["4", "3", "4", "3", "4", "3", "4", "3", "4", "3"],
        ["1", "2", "1", "2", "1", "2", "1", "2", "1", "2"],
        ["4", "3", "4", "3", "4", "3", "4", "3", "4", "3"],
        ["1", "2", "1", "2", "1", "2", "1", "2", "1", "2"]
    ]
}


# Main Program Execution
reset_database()
file_path = input("Enter the file path (Excel or CSV): ").strip()

if file_path.lower().endswith(('.xlsx', '.xls')):
    csv_file_path = convert_excel_to_csv(file_path)
    if csv_file_path:
        insert_data_into_db(csv_file_path)
        register_numbers = fetch_data_from_db()
elif file_path.lower().endswith('.csv'):
    insert_data_into_db(file_path)
    register_numbers = fetch_data_from_db()
else:
    print("Invalid file format. Please provide a valid Excel or CSV file.")
    exit()

# Allocate seats based on the fetched registration data
allocations = allocate_seats(register_numbers, hall_patterns)

# Display the seat allocations for each hall
for hall_name, pattern in hall_patterns.items():
    print(f"\n{hall_name} Allocation:")
    for row in allocations[hall_name]:
        print("  " + " ".join(row))
        
#cd C:\Users\GOD;
#C:\sqlite\sqlite3.exe registration_data.db;
