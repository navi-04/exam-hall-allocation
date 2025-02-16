from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/add_hall', methods=['POST'])
def add_hall():
    global hall_patterns
    try:
        data = request.json
        hall_patterns = data.get('previews')
        print(hall_patterns)
        return jsonify({"message": "Data received successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
