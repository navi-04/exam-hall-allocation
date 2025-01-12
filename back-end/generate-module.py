import csv
import pandas as pd
import os
import sqlite3

def fetch_registration_data(file_path):
    registration_dict = {}
    try:
        with open(file_path, mode='r') as csvfile:
            csv_reader = csv.reader(csvfile)
            headers = next(csv_reader)
            for department in headers:
                registration_dict[department] = []
            for row in csv_reader:
                for i, reg_number in enumerate(row):
                    department = headers[i]
                    registration_dict[department].append(reg_number.upper())
        return registration_dict
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

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

def reset_database():
    conn = sqlite3.connect('registration_data.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS registrations')
    conn.commit()
    conn.close()

def insert_data_into_db(file_path):
    conn = sqlite3.connect('registration_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registrations (
            department TEXT,
            reg_number TEXT
        )
    ''')
    try:
        with open(file_path, mode='r') as csvfile:
            csv_reader = csv.reader(csvfile)
            headers = next(csv_reader)
            for row in csv_reader:
                for i, reg_number in enumerate(row):
                    department = headers[i]
                    cursor.execute('''
                        INSERT INTO registrations (department, reg_number)
                        VALUES (?, ?)
                    ''', (department, reg_number.upper()))
        conn.commit()
        print(f"Data from {file_path} inserted into the database.")
    except Exception as e:
        print(f"An error occurred while inserting data: {e}")
    finally:
        conn.close()

def fetch_data_from_db():
    conn = sqlite3.connect('registration_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT department, reg_number FROM registrations')
    registration_dict = {}
    for department, reg_number in cursor.fetchall():
        if department not in registration_dict:
            registration_dict[department] = []
        registration_dict[department].append(reg_number)
    conn.close()
    return registration_dict

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

department_map = {1: "CSE", 2: "MECH", 3: "AIDS", 4: "CSBS"}
allocations = allocate_seats(register_numbers, hall_patterns)

for hall_name, pattern in hall_patterns.items():
    print(f"\n{hall_name} Allocation:")
    for row in allocations[hall_name]:
        print("  " + " ".join(row))
