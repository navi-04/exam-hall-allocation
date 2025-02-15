import attensinglefunc  # Importing the attendance calculation module

def filter_attendance(attendance_records):
    try:
        if not attendance_records:
            print("No attendance records found.")
            return

        limit = float(input("Enter the attendance percentage limit: "))
        choice = input("Do you want to see students above, below, or all? (Enter 'above', 'below', or 'all'): ").strip().lower()

        print("\nRegister Number\tAttendance Percentage")
        for register_number, (attendance_percentage, phone_number) in attendance_records.items():
            if choice == "above" and attendance_percentage > limit:
                print(f"{register_number}\t\t{attendance_percentage:.2f}%")
            elif choice == "below" and attendance_percentage < limit:
                print(f"{register_number}\t\t{attendance_percentage:.2f}%")
            elif choice == "all":
                print(f"{register_number}\t\t{attendance_percentage:.2f}%")

    except ValueError:
        print("Invalid input! Please enter a numerical value for the attendance percentage limit.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Fetch attendance records from the previous execution (assumes it's already calculated)
attendance_records = attensinglefunc.attendance_records  # Using the precomputed records

# Call the function with the attendance records
filter_attendance(attendance_records)
