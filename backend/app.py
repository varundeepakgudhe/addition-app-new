from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# # Root route
# @app.route('/')
# def home():
#     return "Welcome to the Addition App! Use the /add endpoint for calculations."


@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.json
    num1 = data.get('num1')
    num2 = data.get('num2')

    if num1 is None or num2 is None:
        return jsonify({"error": "Both number1 and number2 are required"}), 400

    try:
        result = float(num1) + float(num2)
        return jsonify({"result": result}), 200
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(debug=True)
