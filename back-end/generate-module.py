"""def generate_registration_numbers(departments, year):
    # Dictionary to store the result
    registration_numbers = {}

    # Iterate through each department
    for obj in departments:
        # Extract department name and number of students
        department_name = obj['name'].lower()  # Convert name to lowercase for the registration number
        num_students = int(obj['numStudents'])

        # Create the prefix using year and department
        prefix = f"9276{year}{department_name}"

        # Generate registration numbers for this department
        registration_numbers[department_name.upper()] = [
            f"{prefix}{str(i).zfill(3)}" for i in range(1, num_students + 1)
        ]

    return registration_numbers

# Example input
departments = [
    {'name': 'EEE', 'numStudents': 45},
    {'name': 'AI', 'numStudents': 60}
]
year = "23"  # Year for CSE students
year_ece = "22"  # Year for ECE students
num_departments = int(input("Enter the number of departments: "))
departments = []
for _ in range(num_departments):
    name = input("Enter the department name: ")
    num_students = int(input(f"Enter the number of students in {name}: "))
    departments.append({'name': name, 'numStudents': num_students})


# Generate registration numbers with different years for different departments
generated_numbers = generate_registration_numbers(
    departments, year="23")

generated_numbers.update(
    generate_registration_numbers(departments, year="22")
)

print(generated_numbers)"""

#===============================================
import csv

def generate_registration_numbers(departments, year):
    # Dictionary to store the result
    registration_numbers = {}

    # Iterate through each department
    for department_name, num_students in departments.items():
        # Convert department name to lowercase for the registration number
        department_name_lower = department_name.lower()
        num_students = int(num_students)

        # Create the prefix using year and department
        prefix = f"9276{year}{department_name_lower}"

        # Generate registration numbers for this department
        registration_numbers[department_name.upper()] = [
            f"{prefix}{str(i).zfill(3)}" for i in range(1, num_students + 1)
        ]

    return registration_numbers

# Read input from a CSV file
def read_departments_from_csv(file_path):
    departments = {}
    try:
        with open(file_path, mode='r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                for department, num_students in row.items():
                    departments[department] = num_students
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit(1)
    return departments

# Main script
input_file = input("Enter the input CSV file path: ")

departments = read_departments_from_csv(input_file)

# Generate registration numbers with different years for different departments
generated_numbers = generate_registration_numbers(departments, year="23")
generated_numbers.update(generate_registration_numbers(departments, year="22"))

print(generated_numbers)


