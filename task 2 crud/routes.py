from flask import request, jsonify
from models import User
from database import db

def register_routes(app):

#     # CREATE
#     @app.route('/users', methods=['POST'])
#     def create_user():
#         data = request.get_json()
#         existing_user = User.query.filter_by(email=data['email']).first()
#         if existing_user:
#             return jsonify({"message": "Email already exists"}), 400
#         user = User(name=data['name'], email=data['email'], age=data['age'])
#         db.session.add(user)
#         db.session.commit()
#         return jsonify({"message": "User created successfully"}), 201

#     # READ
#     @app.route('/users', methods=['GET'])
#     def get_users():
#         users = User.query.all()
#         return jsonify([user.to_dict() for user in users])

#     # UPDATE
#     @app.route('/users/<int:id>', methods=['PUT'])
#     def update_user(id):
#         user = User.query.get(id)
#         if not user:
#             return jsonify({"message": "User not found"}), 404
#         data = request.get_json()
#         user.name = data.get('name', user.name)
#         user.email = data.get('email', user.email)
#         user.age = data.get('age', user.age)
#         db.session.commit()
#         return jsonify({"message": "User updated successfully"})

#     # DELETE
#     @app.route('/users/<int:id>', methods=['DELETE'])
#     def delete_user(id):
#         user = User.query.get(id)
#         if not user:
#             return jsonify({"message": "User not found"}), 404
#         db.session.delete(user)
#         db.session.commit()
#         return jsonify({"message": "User deleted successfully"})


 @app.route('/users', methods=['POST'])
 def create_user():
    data = request.get_json()

    # Validation: required fields
    if 'name' not in data or 'email' not in data or 'age' not in data:
        return jsonify({"message": "Missing required fields"}), 400

    # Validation: age must be non-negative
    if data['age'] < 0:
        return jsonify({"message": "Age must be non-negative"}), 400

    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({"message": "Email already exists"}), 409

    new_user = User(name=data['name'], email=data['email'], age=data['age'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


