import pandas as pd
import os
from twilio.rest import Client

# Global variable to store attendance records
attendance_records = {}

def calculate_attendance(file_path):
    global attendance_records  # Use global variable to store records

    if not os.path.isfile(file_path):
        return {}

    try:
        data_frame = pd.read_excel(file_path)
    except Exception:
        return {}

    attendance_records = {}  # Reset before storing new records
    date_columns = data_frame.columns[1:-1]  # Exclude name and phone columns
    for _, row in data_frame.iterrows():
        register_number = row[0]  # Register number
        phone_number = row[-1]  # Last column as phone number

        present_count = sum(1 for col in date_columns if str(row[col]).strip().upper() == "P")
        total_classes = len(date_columns)
        attendance_percentage = (present_count / total_classes) * 100 if total_classes > 0 else 0

        attendance_records[register_number] = (attendance_percentage, phone_number)
    
    return attendance_records

def send_sms(phone_number, register_number, attendance, account_sid, auth_token, twilio_phone):
    try:
        client = Client(account_sid, auth_token, timeout=30)
        client.messages.create(
            body=f"Dear {register_number}, your attendance is {attendance:.2f}% which is below the required percentage. Please improve your attendance.",
            from_=twilio_phone,
            to=phone_number
        )
    except Exception:
        pass

# Example usage
try:
    attendance_records = calculate_attendance(  # Store the records in the global variable
        file_path=r"C:\Users\nisha\OneDrive\Documents\GitHub\exam-hall-allocation\data\atten.xlsx"
    )
    
    for register_number, (attendance_percentage, phone_number) in attendance_records.items():
        if attendance_percentage < 80:
            send_sms(phone_number, register_number, attendance_percentage, "your_account_sid", "your_auth_token", "your_twilio_phone_number")
except Exception:
    pass