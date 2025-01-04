
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
    # Test Case 1: Valid arrangement
    hall_1 = [
        ["927623bcs001", "927623bee001", "927623ece001", "927623bcs002", "927623bee002"],
        ["927623ece002", "927623bcs004", "927623bee003", "927623ece003", "927623bcs005"],
        ["927623bee004", "927623ece004", "927623bcs006", "927623bee005", "927623ece005"],
        ["927623bcs007", "927623bee006", "927623ece006", "927623bcs008", "927623bee007"],
        ["927623ece007", "927623bcs009", "927623bee008", "927623ece008", "927623bcs010"]
    ]

    # Test Case 2: Invalid arrangement
    hall_2 = [
        ["927623bcs001", "927623bee001", "927623ece001", "927623bcs002", "927623bee002"],
        ["927623ece002", "INVALID12345", "927623bee003", "927623bee003", "927623bcs005"],  # Conflict and invalid entry
        ["927623bee004", "927623ece004", "927623bcs006", "927623bee005", "927623ece005"],
        ["927623bcs007", "927623bee006", "927623ece006", "927623bcs008", "927623bee007"],
        ["927623ece007", "927623bcs009", "927623bee008", "927623ece008", "927623bcs010"]
    ]

    print("Test Case 1: Valid Hall Arrangement")
    check_hall(hall_1, check_diagonal=False, debug=True)

    print("\nTest Case 2: Invalid Hall Arrangement")
    check_hall(hall_2, check_diagonal=False, debug=True)

if __name__ == "__main__":
    main()

