from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import sqlite3
from calculate_percentage import calculate_and_store_attendance
from display_attendence_precentage import filter_attendance
app = Flask(__name__)
CORS(app)

hall_patterns = []

@app.route('/attendance_data', methods=['POST'])
def attendance_data():
    try:
        file = request.files.get('file')
        try:
            df = pd.read_excel(file)

        except Exception as e:
            return jsonify({"error": f"Failed to read Excel file: {e}"}), 500

        percentage = request.form.get('percentage')
        if not percentage:
            return jsonify({"error": "Percentage is missing"}), 400

        calculate_and_store_attendance(df,int(percentage))
        return jsonify({"message": "Data received successfully", "rows": len(df)}), 200

    except Exception as e:
        print(f"Server error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/add_hall', methods=['POST'])
def add_hall():
    try:
        data = request.json
        hall_patterns = data.get('previews')
        print(hall_patterns)
        return jsonify({"message": "Data received successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_register_num', methods=['POST'])
def get_register_num():
    try:
        data = request.json
        hall_patterns = data.get('previews')
        print(hall_patterns)
        # regiser_num = data.get('regiser_num')
        #search_and_display_halls(regiser_num)
        return jsonify({"message": "Data received successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/attendance_data_2', methods=['POST'])
def attendance_data_2():
        data = request.json
        selected_option = data.get('selectedOption')
        rows = filter_attendance(selected_option)
        return jsonify({"message": "Data received successfully", "rows": rows}), 200



if __name__ == '__main__':
    app.run(debug=True)
