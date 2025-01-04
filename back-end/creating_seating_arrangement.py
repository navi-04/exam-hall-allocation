# Register numbers for different departments
register_numbers = {
    "CSE": ['927623BCS001', '927623BCS002', '927623BCS003', '927623BCS004', '927623BCS005', '927623BCS006', '927623BCS007', '927623BCS008', '927623BCS009', '927623BCS010', '927623BCS011', '927623BCS012', '927623BCS013', '927623BCS014', '927623BCS015', '927623BCS016', '927623BCS017', '927623BCS018', '927623BCS019', '927623BCS020', '927623BCS021', '927623BCS022', '927623BCS023', '927623BCS024', '927623BCS025', '927623BCS026', '927623BCS027', '927623BCS028', '927623BCS029', '927623BCS030', '927623BCS031', '927623BCS032', '927623BCS033', '927623BCS034', '927623BCS035', '927623BCS036', '927623BCS037', '927623BCS038', '927623BCS039', '927623BCS040', '927623BCS041', '927623BCS042'],
    "MECH": ['927623BME001', '927623BME002', '927623BME003', '927623BME004', '927623BME005', '927623BME006', '927623BME007', '927623BME008', '927623BME009', '927623BME010', '927623BME011', '927623BME012', '927623BME013', '927623BME014', '927623BME015', '927623BME016', '927623BME017', '927623BME018', '927623BME019', '927623BME020', '927623BME021', '927623BME022', '927623BME023', '927623BME024', '927623BME025', '927623BME026', '927623BME027', '927623BME028', '927623BME029', '927623BME030', '927623BME031', '927623BME032', '927623BME033', '927623BME034', '927623BME035', '927623BME036', '927623BME037', '927623BME038', '927623BME039', '927623BME040', '927623BME041'],
    "AIDS": ['927623BAD001', '927623BAD002', '927623BAD003', '927623BAD004', '927623BAD005', '927623BAD006', '927623BAD007', '927623BAD008', '927623BAD009', '927623BAD010', '927623BAD011', '927623BAD012', '927623BAD013', '927623BAD014', '927623BAD015', '927623BAD016', '927623BAD017', '927623BAD018', '927623BAD019', '927623BAD020', '927623BAD021', '927623BAD022', '927623BAD023', '927623BAD024', '927623BAD025', '927623BAD026', '927623BAD027', '927623BAD028', '927623BAD029', '927623BAD030', '927623BAD031', '927623BAD032', '927623BAD033', '927623BAD034', '927623BAD035', '927623BAD036', '927623BAD037', '927623BAD038', '927623BAD039', '927623BAD040', '927623BAD041'],
    "CSBS": ['927623BCB001', '927623BCB002', '927623BCB003', '927623BCB004', '927623BCB005', '927623BCB006', '927623BCB007', '927623BCB008', '927623BCB009', '927623BCB010', '927623BCB011', '927623BCB012', '927623BCB013', '927623BCB014', '927623BCB015', '927623BCB016', '927623BCB017', '927623BCB018', '927623BCB019', '927623BCB020', '927623BCB021', '927623BCB022', '927623BCB023', '927623BCB024', '927623BCB025', '927623BCB026', '927623BCB027', '927623BCB028', '927623BCB029', '927623BCB030', '927623BCB031', '927623BCB032', '927623BCB033', '927623BCB034', '927623BCB035', '927623BCB036', '927623BCB037', '927623BCB038', '927623BCB039', '927623BCB040', '927623BCB041']
}

# Hall patterns for seat allocation
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

# Mapping of department to its respective number
department_map = {
    1: "CSE",
    2: "MECH",
    3: "AIDS",
    4: "CSBS"
}

# Function to assign students to halls based on the pattern
def allocate_seats(register_numbers, hall_patterns):
    # Create student iterators for each department
    department_iterators = {
        department: iter(register_numbers[department]) for department in register_numbers
    }

    # Store the student allocations for each hall (2D list per hall)
    hall_allocations = {hall: [['' for _ in range(len(pattern))] for pattern in hall_patterns[hall]] for hall in hall_patterns}

    # Iterate through each hall and its seating pattern
    for hall_name, pattern in hall_patterns.items():
        # Fill columns first
        num_rows = len(pattern)
        num_cols = len(pattern[0])
        
        # Allocate students vertically (column-wise)
        for col_index in range(num_cols):
            for row_index in range(num_rows):
                department_id = int(pattern[row_index][col_index])
                department = department_map[department_id]
                
                # Get the next student for this department
                student_id = next(department_iterators[department], "No Student")
                
                # Allocate student ID to the position in the hall
                hall_allocations[hall_name][row_index][col_index] = student_id

    return hall_allocations


# Allocate seats based on the pattern
allocations = allocate_seats(register_numbers, hall_patterns)

# Output the seat allocation in the given pattern
for hall_name, pattern in hall_patterns.items():
    print(f"\n{hall_name} Allocation:")
    for row in allocations[hall_name]:
        print("  " + " ".join(row))
