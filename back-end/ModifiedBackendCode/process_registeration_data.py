import csv
import pandas as pd
import os
import sqlite3

# Main function to handle all operations
def process_registration_data(path,department_map, hall_patterns):

    
    # Reset Database
    def reset_database():
        conn = sqlite3.connect('registration_data.db')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS registrations')
        conn.commit()
        conn.close()

    # Insert Data into DB from CSV
    def insert_data_into_db(file_path):
        conn = sqlite3.connect('registration_data.db')
        cursor = conn.cursor()
        
        with open(file_path, mode='r') as csvfile:
            csv_reader = csv.reader(csvfile)
            headers = next(csv_reader)
            
            columns = ', '.join([f"{department} TEXT" for department in headers])
            create_table_query = f"CREATE TABLE IF NOT EXISTS registrations ({columns})"
            cursor.execute(create_table_query)
            
            for row in csv_reader:
                placeholders = ', '.join(['?' for _ in row])
                insert_query = f"INSERT INTO registrations VALUES ({placeholders})"
                cursor.execute(insert_query, row)

        conn.commit()
        conn.close()

    # Fetch Data from DB
    def fetch_data_from_db():
        conn = sqlite3.connect('registration_data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM registrations')
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        registration_dict = {column: [] for column in columns}
        
        for row in rows:
            for column, value in zip(columns, row):
                if value:
                    registration_dict[column].append(value)
        
        conn.close()
        return registration_dict

    # Allocate Seats
    def allocate_seats(register_numbers, hall_patterns):
        department_iterators = {department: iter(register_numbers[department]) for department in register_numbers}
        hall_allocations = {}
        
        for hall_name, pattern in hall_patterns.items():
            num_rows = len(pattern)
            num_cols = len(pattern[0])
            hall_allocations[hall_name] = []
            for row_index in range(num_rows):
                row_data = []
                for col_index in range(num_cols):
                    department_id = int(pattern[row_index][col_index])
                    department = department_map[department_id]
                    student_id = next(department_iterators[department], "No Student")
                    row_data.append(student_id)
                hall_allocations[hall_name].append(" ".join(row_data))
        return hall_allocations

    reset_database()
    insert_data_into_db(file_path)
    register_numbers = fetch_data_from_db()
    allocations = allocate_seats(register_numbers, hall_patterns)
    
    return allocations
def print_hall_allocation(allocations):
    for hall, allocation in allocations.items():
        print(f"{hall} Allocation:")
        for row in allocation:
            print(f"  {row}")
        print()

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

# Department Mapping
department_map = {1: "CSE", 2: "MECH", 3: "AIDS", 4: "CSBS"}
file_path = "C:/Users/GOD/Documents/GitHub/exam-hall-allocation/data/file.csv"
# Process Data and Get Allocations
allocations = process_registration_data(file_path,department_map, hall_patterns)
#print(allocations)
#print_hall_allocation(allocations)