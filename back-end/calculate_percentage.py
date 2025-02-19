import pandas as pd
import sqlite3

def calculate_and_store_attendance(df, percentage_limit, db_name="attendance.db"):

    attendance_data = df.iloc[:, 2:]
    
    total_days = attendance_data.shape[1]
    df['percentage'] = (attendance_data.apply(lambda row: (row == 'p').sum(), axis=1) / total_days) * 100
    
    df['percentage_limit'] = percentage_limit

    result_df = df[['register_number', 'percentage', 'phone_number', 'percentage_limit']]
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            register_no TEXT PRIMARY KEY,
            percentage REAL,
            phone_number TEXT,
            percentage_limit REAL
        )
    """)

    result_df.to_sql('attendance', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()


