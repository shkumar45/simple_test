from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a simple route for the root URL
@app.route('/')
def home():
    return jsonify({"message": "Welcome to my simple API!"})

# Define a route to add two numbers
@app.route('/add', methods=['GET'])
def add_numbers():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
        return jsonify({"result": a + b})
    except ValueError:
        return jsonify({"error": "Invalid input, please provide integers"}), 400

if __name__ == '__main__':
    app.run(debug=True)
