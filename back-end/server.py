from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


hall_patterns = []

@app.route('/attendance_data', methods=['POST'])
def attendance_data():
    global file_data, percentage
    try:
        file = request.files.get('file')
        percentage = request.form.get('percentage')

        if not file:
            return jsonify({"error": "No file provided"}), 400

        # Read file content if needed
        file_content = file.read().decode('utf-8')[:100]  # Limiting to 100 chars for display
        print(f"Received file (first 100 chars): {file_content}")
        print(f"Received percentage: {percentage}")
        
        return jsonify({"message": "Data received successfully"}), 200

    except Exception as e:
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
