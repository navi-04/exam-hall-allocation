from process_registration_data import process_registration_data, department_map  # Import first script functions
from get_hall_pattern import hall_patterns  # Import hall patterns

def validate_hall_arrangement(hall, check_diagonal=False, debug=False):
    """
    Validates the hall arrangement and prints the result.
    """
    def get_department_hash(registration_number):
        department_map = {"bcs": 1, "bee": 2, "ece": 3}
        for key, value in department_map.items():
            if key in registration_number:
                return value
        return -1  # Invalid department

    def is_valid_hall_advanced(hall):
        rows, cols = len(hall), len(hall[0])
        if rows != 5 or cols != 5:
            return False, ["The hall must be a 5x5 matrix."]
        
        department_hashes = [[get_department_hash(hall[row][col]) for col in range(cols)] for row in range(rows)]
        
        if debug:
            print("Department Hashes Matrix:")
            for row in department_hashes:
                print(row)
        
        directions = [(0, 1), (1, 0)]
        if check_diagonal:
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
                    if 0 <= r < rows and 0 <= c < cols and department_hashes[r][c] == current_hash:
                        issues.append(f"Conflict at ({row}, {col}) and ({r}, {c}): Same department.")
        
        return (False, issues) if issues else (True, [])

    is_valid, issues = is_valid_hall_advanced(hall)
    if is_valid:
        print("The hall arrangement is valid.")
    else:
        print("The hall arrangement is invalid due to the following reasons:")
        for issue in issues:
            print(f"- {issue}")

# Fetch hall allocations dynamically
file_path = "C:/Users/GOD/Documents/GitHub/exam-hall-allocation/data/file.csv"
allocations = process_registration_data(file_path, department_map,hall_patterns)

# Validate each hall
for hall_name, hall_arrangement in allocations.items():
    print(f"Validating {hall_name}:")
    validate_hall_arrangement([row.split() for row in hall_arrangement], check_diagonal=False, debug=True)
    print()
