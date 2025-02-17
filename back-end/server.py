from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd 

app = Flask(__name__)
CORS(app)


hall_patterns = []

# @app.route('/attendance_data', methods=['POST'])
# def attendance_data():
#     try:
#         # Access file and form data
#         file = request.files.get('file')
#         percentage = request.form.get('percentage')

#         if not file:
#             return jsonify({"error": "No file provided"}), 400

#         # Read file content if needed
#         file_content = file.read().decode('utf-8')[:100]  # Limiting to 100 chars for display
#         print(f"Received file (first 100 chars): {file_content}")
#         print(f"Received percentage: {percentage}")

#         return jsonify({"message": "Data received successfully"}), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
@app.route('/attendance_data', methods=['POST'])
def attendance_data():
    try:
        print("🔍 Incoming request for attendance data")

        # Get the file from the request
        file = request.files.get('file')
        if not file:
            print("❌ No file provided")
            return jsonify({"error": "File is missing"}), 400

        # Ensure it's an Excel file
        if not file.filename.endswith('.xlsx'):
            print("❌ Invalid file type")
            return jsonify({"error": "Invalid file type. Please upload an .xlsx file"}), 400

        # Read the file using pandas
        try:
            df = pd.read_excel(file)
            print(f"📊 First 5 rows:\n{df.head()}")

        except Exception as e:
            print(f"❌ Failed to read Excel file: {e}")
            return jsonify({"error": f"Failed to read Excel file: {e}"}), 500

        # Get percentage
        percentage = request.form.get('percentage')
        if not percentage:
            print("❌ Percentage missing")
            return jsonify({"error": "Percentage is missing"}), 400

        print(f"🎯 Percentage received: {percentage}")

        return jsonify({"message": "Data received successfully", "rows": len(df)}), 200

    except Exception as e:
        print(f"🔥 Server error: {e}")
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

if __name__ == '__main__':
    app.run(debug=True)
