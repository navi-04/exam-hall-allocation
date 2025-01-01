import random

# Predefined registration numbers
registration_numbers = {
    "CSE": ["927623bCSE001", "927623bCSE002", "927623bCSE003", "927623bCSE004", "927623bCSE005", "927623bCSE006", "927623bCSE007"],
    "EEE": ["927623bEEE001", "927623bEEE002", "927623bEEE003", "927623bEEE004", "927623bEEE005", "927623bEEE006", "927623bEEE007"],
    "CE": ["927623bCE001", "927623bCE002", "927623bCE003", "927623bCE004", "927623bCE005", "927623bCE006", "927623bCE007"],
    "ECE": ["927623bECE001", "927623bECE002", "927623bECE003", "927623bECE004", "927623bECE005", "927623bECE006", "927623bECE007"]
}

def get_departments_and_seats():
    print("Enter the available departments:")
    available_departments = list(registration_numbers.keys())
    chosen_departments = []
    
    num_departments = int(input(f"How many departments do you want to allocate seats for? (Max {len(available_departments)}): "))
    if num_departments > len(available_departments):
        print(f"Error: You can only select up to {len(available_departments)} departments.")
        return
    
    print("Please choose the departments:")
    for i, dept in enumerate(available_departments):
        print(f"{i + 1}. {dept}")
    
    for i in range(num_departments):
        chosen_dept = int(input(f"Select department {i + 1}: ")) - 1
        chosen_departments.append(available_departments[chosen_dept])

    dept_seats = {}
    for dept in chosen_departments:
        num_seats = int(input(f"How many seats do you want to allocate for department {dept}? (Max {len(registration_numbers[dept])}): "))
        dept_seats[dept] = num_seats

    total_hall_capacity = 25  # Fixed to 5x5 (total 25 students)
    return chosen_departments, dept_seats, total_hall_capacity

def generate_seating_pattern(chosen_departments):
    rows, cols = 5, 5  # Fixed 5x5 seating pattern
    dept_queue = list(chosen_departments) * (rows * cols // len(chosen_departments) + 1)
    random.shuffle(dept_queue)

    # Initialize seating pattern (empty 5x5 grid)
    pattern = [[None] * cols for _ in range(rows)]

    def is_valid_placement(row, col, dept):
        # Ensure no clashes in columns 1 and 2 (same department should not be next to each other)
        if (col == 0 and pattern[row][1] == dept) or (col == 1 and pattern[row][0] == dept):
            return False
        
        # Ensure no clashes in columns 3 (same department should not be in same row as column 2 or 4)
        if col == 2 and (pattern[row][1] == dept or pattern[row][3] == dept):
            return False
        
        # Ensure no clashes in columns 4 and 5 (same department should not be next to each other)
        if (col == 3 and pattern[row][4] == dept) or (col == 4 and pattern[row][3] == dept):
            return False

        # Ensure no diagonal clashes for consecutive rows (X-shape check for columns 1 and 2)
        if row > 0:
            if col == 0 and (pattern[row - 1][1] == dept or pattern[row - 1][0] == dept):  # Diagonal for column 1
                return False
            if col == 1 and (pattern[row - 1][0] == dept or pattern[row - 1][1] == dept):  # Diagonal for column 2
                return False
            if col == 2 and (pattern[row - 1][1] == dept or pattern[row - 1][3] == dept):  # Diagonal for column 3
                return False
            if col == 3 and (pattern[row - 1][4] == dept or pattern[row - 1][2] == dept):  # Diagonal for column 4
                return False
            if col == 4 and (pattern[row - 1][3] == dept or pattern[row - 1][4] == dept):  # Diagonal for column 5
                return False

        # Ensure no vertical clashes (no same department in consecutive rows in the same column)
        if row > 0:
            if pattern[row - 1][col] == dept:
                return False
        
        return True

    # Assign departments to the grid based on the above rules
    for i in range(rows):
        for j in range(cols):
            while True:
                selected_dept = random.choice(dept_queue)
                if is_valid_placement(i, j, selected_dept):
                    pattern[i][j] = selected_dept
                    dept_queue.remove(selected_dept)
                    break
    return pattern

def creating_seating_arrangement(registration_numbers, pattern, dept_seats):
    departments = {key.lower(): registration_numbers[key] for key in registration_numbers}
    hall = []

    # Assign students to the seating arrangement
    for i, row in enumerate(pattern):
        hall_row = []
        for j, department in enumerate(row):
            department_lower = department.lower()
            if departments[department_lower] and dept_seats.get(department, 0) > 0:
                student = departments[department_lower].pop(0)
                hall_row.append(student)
                dept_seats[department] -= 1
            else:
                hall_row.append(None)
        hall.append(hall_row)

    return hall, departments

# Main program flow
chosen_departments, dept_seats, total_hall_capacity = get_departments_and_seats()
pattern = generate_seating_pattern(chosen_departments)

# Display the generated pattern
print("\nGenerated Seating Pattern:")
for row in pattern:
    print(row)

# Call the function and get the seating arrangement
seating_arrangement, remaining_departments = creating_seating_arrangement(registration_numbers, pattern, dept_seats)

# Print seating arrangement
print("\nSeating Arrangement for Hall 1:")
for row in seating_arrangement:
    print(row)

# Check if there are remaining students to be seated in another hall
remaining_students = sum([len(remaining_departments[dept]) for dept in remaining_departments])

if remaining_students > 0:
    print("\nRemaining Students (Not Allocated a Seat in Hall 1):")
    for department, students in remaining_departments.items():
        if students:
            print(f"{department.upper()}: {students}")
