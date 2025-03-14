import pandas as pd
import sqlite3

def filter_attendance(limit_percentage, db_name="attendance.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT percentage_limit FROM attendance")
    first_value = cursor.fetchone()[0]  

    if limit_percentage == "none":
        return None
    elif limit_percentage == "1":
        cursor.execute("SELECT register_number, percentage FROM attendance")
    elif limit_percentage == "2":
        cursor.execute("SELECT register_number, percentage FROM attendance WHERE percentage >= ?", (first_value,))
    elif limit_percentage == "3":
        cursor.execute("SELECT register_number, percentage FROM attendance WHERE percentage <= ?", (first_value,))
    
    rows = cursor.fetchall()
    result = [{"regno": row[0], "percentage": row[1]} for row in rows]
    
    cursor.close()
    conn.close()
    return result

