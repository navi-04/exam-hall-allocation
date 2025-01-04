def get_department_hash(registration_number):
    """
    Maps the registration number to a department:
    'bcs' -> 1 (CSE), 'bee' -> 2 (EEE), 'ece' -> 3 (ECE)
    """
    department_map = {"bcs": 1, "bee": 2, "ece": 3}
    for key, value in department_map.items():
        if key in registration_number:
            return value
    return -1  # Invalid department

def is_valid_hall_advanced(hall, check_diagonal=False, debug=False):
    """
    Validates the hall arrangement and returns True if valid,
    else returns False along with the reasons for invalidity.
    """
    rows, cols = len(hall), len(hall[0])

    # Check if the hall is a 5x5 matrix
    if rows != 5 or cols != 5:
        return False, ["The hall must be a 5x5 matrix."]
    
    department_hashes = [[get_department_hash(hall[row][col]) for col in range(cols)] for row in range(rows)]

    # Logging for debugging purposes
    if debug:
        print("Department Hashes Matrix:")
        for row in department_hashes:
            print(row)

    # Directions for horizontal and vertical checks
    directions = [(0, 1), (1, 0)]  # Only horizontal and vertical
    if check_diagonal:
        # Include diagonal directions if enabled
        directions += [(1, 1), (1, -1)]

    issues = []

    for row in range(rows):
        for col in range(cols):
            current_hash = department_hashes[row][col]
            if current_hash == -1:
                issues.append(f"Invalid department at ({row}, {col}).")
                continue

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols:
                    if department_hashes[r][c] == current_hash:
                        issues.append(f"Conflict at ({row}, {col}) and ({r}, {c}): Same department.")
    
    if issues:
        return False, issues
    return True, []

def check_hall(hall, check_diagonal=False, debug=False):
    """
    Validates a hall arrangement and prints the result.
    """
    is_valid, issues = is_valid_hall_advanced(hall, check_diagonal, debug)
    if is_valid:
        print("The hall arrangement is valid.")
    else:
        print("The hall arrangement is invalid due to the following reasons:")
        for issue in issues:
            print(f"- {issue}")

def main():
    """
    Main function to test hall arrangements with diagonal checks disabled.
    """
    # Test Case 1: Valid 5x5 arrangement
    hall_1 = [
        ["927623bcs001", "927623bee001", "927623ece001", "927623bcs002", "927623bee002"],
        ["927623ece002", "927623bcs004", "927623bee003", "927623ece003", "927623bcs005"],
        ["927623bee004", "927623ece004", "927623bcs006", "927623bee005", "927623ece005"],
        ["927623bcs007", "927623bee006", "927623ece006", "927623bcs008", "927623bee007"],
        ["927623ece007", "927623bcs009", "927623bee008", "927623ece008", "927623bcs010"]
    ]

    # Test Case 2: Invalid arrangement (Not 5x5)
    hall_2 = [
        ["927623bcs001", "927623bee001", "927623ece001", "927623bcs002"],
        ["927623ece002", "927623bcs003", "927623bee003", "927623ece003"],
        ["927623bcs004", "927623bee004", "927623ece004", "927623bcs005"],
        ["927623ece005", "927623bcs006", "927623bee005", "927623ece006"]
    ]
    
    # Test Case 3: Valid 5x5 arrangement with diagonal check
    hall_3 = [
        ["927623bcs001", "927623bee001", "927623ece001", "927623bcs002", "927623bee002"],
        ["927623ece002", "927623bcs004", "927623bee003", "927623ece003", "927623bcs005"],
        ["927623bee004", "927623ece004", "927623bcs006", "927623bee005", "927623ece005"],
        ["927623bcs007", "927623bee006", "927623ece006", "927623bcs008", "927623bee007"],
        ["927623ece007", "927623bcs009", "927623bee008", "927623ece008", "927623bcs010"]
    ]
    
    # Test Case 4: Invalid entry in one position
    hall_4 = [
        ["927623bcs001", "927623bee001", "927623ece001", "INVALID12345", "927623bee002"],
        ["927623ece002", "927623bcs004", "927623bee003", "927623ece003", "927623bcs005"],
        ["927623bee004", "927623ece004", "927623bcs006", "927623bee005", "927623ece005"],
        ["927623bcs007", "927623bee006", "927623ece006", "927623bcs008", "927623bee007"],
        ["927623ece007", "927623bcs009", "927623bee008", "927623ece008", "927623bcs010"]
    ]

    # Test Case 5: Conflict between two departments
    hall_5 = [
        ["927623bcs001", "927623bcs002", "927623ece001", "927623bcs003", "927623bee002"],
        ["927623ece002", "927623bcs004", "927623bee003", "927623ece003", "927623bcs005"],
        ["927623bee004", "927623ece004", "927623bcs006", "927623bee005", "927623ece005"],
        ["927623bcs007", "927623bcs008", "927623ece006", "927623bcs009", "927623bee007"],
        ["927623ece007", "927623bcs009", "927623bee008", "927623ece008", "927623bcs010"]
    ]

    # Test Case 6: Invalid hall (not 5x5)
    hall_6 = [
        ["927623bcs001", "927623bee001", "927623ece001", "927623bcs002"],
        ["927623ece002", "927623bcs003", "927623bee003", "927623ece003"],
        ["927623bcs004", "927623bee004", "927623ece004", "927623bcs005"],
        ["927623ece005", "927623bcs006", "927623bee005", "927623ece006"]
    ]
    
    # Test Case 7: Hall with all departments matching
    hall_7 = [
        ["927623bcs001", "927623bcs002", "927623bcs003", "927623bcs004", "927623bcs005"],
        ["927623bcs006", "927623bcs007", "927623bcs008", "927623bcs009", "927623bcs010"],
        ["927623bcs011", "927623bcs012", "927623bcs013", "927623bcs014", "927623bcs015"],
        ["927623bcs016", "927623bcs017", "927623bcs018", "927623bcs019", "927623bcs020"],
        ["927623bcs021", "927623bcs022", "927623bcs023", "927623bcs024", "927623bcs025"]
    ]

    # Test Case 8: Hall with random invalid entries
    hall_8 = [
        ["INVALID12345", "927623bcs001", "927623bee001", "927623ece001", "927623bcs002"],
        ["927623ece002", "927623bcs004", "927623bee003", "927623ece003", "927623bcs005"],
        ["927623bee004", "927623ece004", "927623bcs006", "927623bee005", "927623ece005"],
        ["927623bcs007", "927623bee006", "927623ece006", "927623bcs008", "927623bee007"],
        ["927623ece007", "927623bcs009", "927623bee008", "927623ece008", "927623bcs010"]
    ]

    # Test Case 9: Hall with mixed departments and no conflicts
    hall_9 = [
        ["927623bcs001", "927623bee001", "927623ece001", "927623bcs002", "927623bee002"],
        ["927623ece002", "927623bcs003", "927623bee003", "927623ece003", "927623bcs004"],
        ["927623bee004", "927623ece004", "927623bcs005", "927623bee005", "927623ece005"],
        ["927623bcs006", "927623bee006", "927623ece006", "927623bcs007", "927623bee007"],
        ["927623ece007", "927623bcs008", "927623bee008", "927623ece008", "927623bcs009"]
    ]

    # Test Case 10: Single valid entry
    hall_10 = [["927623bcs001"]]

    # Running all test cases
    test_cases = [
        ("Test Case 1: Valid 5x5 Hall Arrangement", hall_1),
        ("Test Case 2: Invalid Hall Arrangement (Not 5x5)", hall_2),
        ("Test Case 3: Valid 5x5 Hall with Diagonal Check", hall_3),
        ("Test Case 4: Invalid Entry", hall_4),
        ("Test Case 5: Conflict Between Two Departments", hall_5),
        ("Test Case 6: Invalid Hall Arrangement (Not 5x5)", hall_6),
        ("Test Case 7: Hall with All Departments Matching", hall_7),
        ("Test Case 8: Hall with Random Invalid Entries", hall_8),
        ("Test Case 9: Hall with Mixed Departments and No Conflicts", hall_9),
        ("Test Case 10: Single Valid Entry", hall_10)
    ]

    for name, hall in test_cases:
        print(f"{name}")
        check_hall(hall, check_diagonal=False, debug=True)
        print()

if __name__ == "__main__":
    main()
