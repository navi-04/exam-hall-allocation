import csv

def fetch_registration_data(file_path):
    registration_dict = {}

    try:
        # Open the CSV file
        with open(file_path, mode='r') as csvfile:
            csv_reader = csv.reader(csvfile)

            # Read the headers (department names)
            headers = next(csv_reader)

            # Initialize the dictionary with department names
            for department in headers:
                registration_dict[department] = []

            # Iterate through the rest of the rows
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

# Input CSV file path
file_path = input("Enter the CSV file path: ")

# Fetch and process registration data
output_dict = fetch_registration_data(file_path)

# Display the output
print(output_dict)
