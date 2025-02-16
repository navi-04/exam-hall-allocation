import pandas as pd
import sqlite3
from twilio.rest import Client
import os


'''

'''

class AttendanceTracker:
    def __init__(self):
        # Twilio credentials (replace with actual credentials)
        self.ACCOUNT_SID = "your_account_sid"
        self.AUTH_TOKEN = "your_auth_token"
        self.TWILIO_PHONE = "your_twilio_phone_number"

        # Database initialization
        self.conn = sqlite3.connect("attendance.db")
        self.initialize_db()

        self.data_frame = None  # Dataframe to hold Excel data

    def initialize_db(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                student_name TEXT,
                phone_number TEXT,
                attendance_percentage REAL
            )
        """)
        self.conn.commit()

    def load_excel_file(self, file_path):
        if not os.path.isfile(file_path):
            print("Invalid file path.")
            return

        try:
            self.data_frame = pd.read_excel(file_path)
            print("Excel file loaded successfully!")
            self.display_data()
        except Exception as e:
            print(f"Failed to load Excel file: {e}")

    def display_data(self):
        if self.data_frame is not None:
            print("\nLoaded Data:")
            print(self.data_frame)

    def calculate_attendance(self):
        if self.data_frame is None:
            print("No data loaded. Please load an Excel file first.")
            return

        date_columns = self.data_frame.columns[1:-1]  # Exclude name and phone columns

        cursor = self.conn.cursor()
        for _, row in self.data_frame.iterrows():
            student_name = row[0]
            phone_number = row[-1]
            
            present_count = sum(1 for col in date_columns if str(row[col]).strip().lower() == "present")
            attendance_percentage = (present_count / len(date_columns)) * 100

            # Save to database
            cursor.execute("""
                INSERT OR REPLACE INTO attendance (student_name, phone_number, attendance_percentage)
                VALUES (?, ?, ?)
            """, (student_name, phone_number, attendance_percentage))

            # Send SMS if attendance < 80%
            if attendance_percentage < 80:
                if self.ACCOUNT_SID and self.AUTH_TOKEN and self.TWILIO_PHONE:
                    self.send_sms(phone_number, student_name, attendance_percentage)
                else:
                    print(f"Skipping SMS for {student_name} due to missing Twilio credentials.")

        self.conn.commit()
        print("Attendance calculated and stored successfully!")

    def send_sms(self, phone_number, student_name, attendance):
        try:
            client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)
            message = client.messages.create(
                body=f"Dear {student_name}, your attendance is {attendance:.2f}% which is below the required 80%. Please improve your attendance.",
                from_=self.TWILIO_PHONE,
                to=phone_number
            )
            print(f"SMS sent to {phone_number}: {message.sid}")
        except Exception as e:
            print(f"Failed to send SMS to {phone_number}: {e}")

def main():
    tracker = AttendanceTracker()

    while True:
        print("\nMenu:")
        print("1. Load Excel file")
        print("2. Calculate Attendance")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            file_path = input("Enter the path to the Excel file: ").strip()
            tracker.load_excel_file(file_path)
        elif choice == "2":
            tracker.calculate_attendance()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 