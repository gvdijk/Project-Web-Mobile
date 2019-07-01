from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import (jwt_required, get_jwt_identity)
import database
import function

user_endpoints = Blueprint('user_endpoints', __name__)

# USERS
@user_endpoints.route('/user', methods=['POST'])
def add_user():
    # Fetch form data
    userDetails = request.get_json()
    name = userDetails.get('name')
    password = userDetails.get('password')

    # Check if all data is supplied
    if name is None:
        return jsonify({"error": "Username not specified"}), 400
    if password is None:
        return jsonify({"error": "Password not specified"}), 400

    # Strip leading and trailing spaces
    name = name.strip()
    
    # Check is username and password comply to the requirements
    username_message = function.check_username(name)
    password_message = function.check_password(password)
    if(username_message is not "ok"):
        return jsonify({"error": username_message}), 400
    elif(password_message is not "ok"):
        return jsonify({"error": password_message}), 400
    
    # Check if the user already exists
    user = database.getUserByName(name)
    if user is not None:
        return "Username already exists"

    # Hash the userpassword for secure storage
    hashedpass = function.hash_password(password)

    # Add user to the database and return newly created userID
    user = database.addUser(name, hashedpass)
    return jsonify(user), 201

@user_endpoints.route('/user/<string:id>', methods=['GET'])
@jwt_required
def get_user(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    data = database.getUserByID(id)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@user_endpoints.route('/user/<string:id>/projects', methods=['GET'])
@jwt_required
def get_user_projects(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Check if user actually exists
    user = database.getUserByID(id)
    if user is None:
        return jsonify({"error": "Specified user does not exist"})

    data = database.getUserProjects(id)
    if data is None:
        return jsonify({"error": "No results found"}), 404
    else:
        for projectuser in data:
            project = database.getProjectByID(str(projectuser['Project_projectID']))
            projectuser['project'] = project
        return jsonify(data), 200

@user_endpoints.route('/user/<string:id>/posts', methods=['GET'])
@jwt_required
def get_user_posts(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Check if user actually exists
    user = database.getUserByID(id)
    if user is None:
        return jsonify({"error": "Specified user does not exist"})

    data = database.getUserPosts(id)
    if data is None:
        return jsonify({"error": "No results found"}), 404
    else:
        userPosts = []
        for post in data:
            project = database.getProjectByID(str(post['postProject']))
            post['project'] = project
            if project is not None:
                userPosts.append(post)
        return jsonify(userPosts), 200

@user_endpoints.route('/user/<string:id>/comments', methods=['GET'])
@jwt_required
def get_user_comments(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Check if user actually exists
    user = database.getUserByID(id)
    if user is None:
        return jsonify({"error": "Specified user does not exist"})

    data = database.getUserComments(id)
    if data is None:
        return jsonify({"error": "No results found"}), 404
    else:
        userComments = []
        for comment in data:
            post = database.getPostByID(str(comment['commentPost']))
            comment['post'] = post
            if post is not None:
                userComments.append(comment)
        return jsonify(userComments), 200

@user_endpoints.route('/user', methods=['GET'])
@jwt_required
def get_user_name():
    name = request.args.get('name')
    limit = request.args.get('limit')
    offset = request.args.get('offset')

    if limit is not None and not function.isInt(limit):
        return jsonify({"error": "limit is not an integer"}), 400
    if offset is not None and not function.isInt(offset):
        return jsonify({"error": "offset is not an integer"}), 400
    
    data = database.getUser(name, limit, offset)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@user_endpoints.route('/user/<string:id>', methods=['PUT'])
@jwt_required
def put_user(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Check if token identity corresponds to the user being updated
    if not(int(id) == get_jwt_identity()):
        return jsonify({"error": "Not allowed to update this users information"}), 403

    # Fetch form data
    userDetails = request.get_json()
    name = userDetails.get('name')
    password = userDetails.get('password')

    # Check if all data is supplied
    if name is None:
        return jsonify({"error": "Username not specified"}), 400
    if password is None:
        return jsonify({"error": "Password not specified"}), 400
    
    # Check if user actually exists
    user = database.getUserByID(id)
    if user is None:
        return jsonify({"error": "Specified user does not exist"})

    # Check is username and password comply to the requirements
    username_message = function.check_username(name)
    password_message = function.check_password(password)
    if(username_message is not "ok"):
        return jsonify({"error": username_message}), 400
    elif(password_message is not "ok"):
        return jsonify({"error": password_message}), 400
    
    # Hash the userpassword for secure storage
    hashedpass = function.hash_password(password)

    data = database.updateUser(id, name, hashedpass)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404
    
@user_endpoints.route('/user/<string:id>', methods=['DELETE'])
@jwt_required
def del_user(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Check if token identity corresponds to the user being deleted
    if not(int(id) == get_jwt_identity()):
        return jsonify({"error": "Not allowed to delete this user"}), 403
    
    # Check if user actually exists
    user = database.getUserByID(id)
    if user is None:
        return jsonify({"error": "Specified user does not exist"})
    
    # Delete user
    if database.deleteUser(id):
        return jsonify({"Info": "User deleted successfully"}), 200
    else:
        return jsonify({"erorr": "Something went wrong deleting user"}), 500