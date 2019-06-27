from endpoints.user_endpoints import user_endpoints
from endpoints.comment_endpoints import comment_endpoints
from endpoints.post_endpoints import post_endpoints
from endpoints.project_endpoints import project_endpoints

from flask import Flask, render_template, request, redirect, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flask_cors import CORS
import database
import function

app = Flask(__name__)

# Register the different endpoints to the resources
app.register_blueprint(user_endpoints)
app.register_blueprint(project_endpoints)
app.register_blueprint(comment_endpoints)
app.register_blueprint(post_endpoints)

# Connect to the MySQL database
host = 'localhost'
user = 'webapp'
password = 'admin' # Super encripted and safe password usage
database_name = 'newdb'
database.init(user, password, host, database_name)

# Configure CORS parameters
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

# Configure JWT parameters
app.config['JWT_SECRET_KEY'] = 'super-secret-JWT-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600
JWTManager(app)

# Authentication endpoint
@app.route('/login', methods=['POST'])
def login():
    # Get user details from request body
    userDetails = request.get_json()
    name = userDetails.get('name')
    password = userDetails.get('password')

    # Check if the user details are set
    if name is None:
        return jsonify({"error": "Username not specified"}), 400
    if password is None:
        return jsonify({"error": "Password not specified"}), 400

    # Check if the user exists
    user = database.getUserByName(name)
    if user is None:
        return jsonify({"error": "User with username " + name + " does not exist"}), 400

    # Check the hashed password against the one provided
    if function.verify_hashed_password(user['userPass'], password):
        jwt_token = create_access_token(identity=user['userID'])
        return jsonify({"id": user['userID'], "jwt_token": jwt_token}), 200
    else:
        return jsonify({"error": "Incorrect password"}), 401

# Start the server
if(__name__ == '__main__'):
    app.run(debug=True)
