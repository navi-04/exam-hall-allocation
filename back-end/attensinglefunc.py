import pandas as pd
import sqlite3
from twilio.rest import Client
import os

def attendance_tracker(file_path, account_sid, auth_token, twilio_phone):
    # Database initialization
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            student_name TEXT,
            phone_number TEXT,
            attendance_percentage REAL
        )
    """)
    conn.commit()

    data_frame = None  # Dataframe to hold Excel data

    def load_excel_file(file_path):
        nonlocal data_frame
        if not os.path.isfile(file_path):
            return

        try:
            data_frame = pd.read_excel(file_path)
        except Exception as e:
            return

    def calculate_attendance():
        nonlocal data_frame
        if data_frame is None:
            return

        date_columns = data_frame.columns[1:-1]  # Exclude name and phone columns

        for _, row in data_frame.iterrows():
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
                if account_sid and auth_token and twilio_phone:
                    send_sms(phone_number, student_name, attendance_percentage)
                else:
                    continue

        conn.commit()
       #print("Attendance calculated and stored successfully!")

    def send_sms(phone_number, student_name, attendance):
        try:
            client = Client(account_sid, auth_token)
            client.messages.create(
                body=f"Dear {student_name}, your attendance is {attendance:.2f}% which is below the required 80%. Please improve your attendance.",
                from_=twilio_phone,
                to=phone_number
            )
        except Exception as e:
            return

    load_excel_file(file_path)
    calculate_attendance()

# Example usage (input parameters passed)
attendance_tracker(
    file_path=r"C:\Users\nisha\OneDrive\Documents\GitHub\exam-hall-allocation\data\atten.xlsx",
    account_sid="your_account_sid",
    auth_token="your_auth_token",
    twilio_phone="your_twilio_phone_number"
)
