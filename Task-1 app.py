from flask import Flask, jsonify, request

# Creating Flask application
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to my Backend Project"
    })

# Route to display student data
@app.route('/students')
def show_students():

    student_list = [
        "Sai",
        "Rahul",
        "Aman"
    ]

    return jsonify({
        "students": student_list
    })

# Route to receive data using POST method
@app.route('/add', methods=['POST'])
def add_student():

    # Getting JSON data from request
    user_data = request.json

    # Sending response back
    return jsonify({
        "message": "Data received successfully",
        "received_data": user_data
    })

# to run the Flask server
if __name__ == '__main__':
    app.run(debug=True)