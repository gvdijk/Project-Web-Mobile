from flask import Flask, render_template, request, redirect, jsonify
from flask_mysqldb import MySQL
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flask_cors import CORS
import mysql.connector
import database
import datetime

app = Flask(__name__)

# Connect to the MySQL database
host = 'localhost'
user = 'webapp'
password = 'admin' # Super encripted and safe password usage
database_name = 'mydb'
database.connect(user, password, host, database_name)

# Configure CORS parameters
CORS(app)

# Configure JWT parameters
app.config['JWT_SECRET_KEY'] = 'super-secret-JWT-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600
JWTManager(app)

# Tuples to help check for correct enumerator inserts in the database
allowed_project_visibilities = ("PUBLIC", "RESTRICTED", "PRIVATE")
allowed_post_states = ("VISIBLE", "ARCHIVED", "DELETED")
allowed_projectUser_states = ("OWNER", "USER", "ADMIN", "PENDING", "INVITED")

# Helper function to check if a String represents an integer or not
def isInt(var):
    try:
        int(var)
        return True
    except ValueError as e:
        return False

# USERS
@app.route('/user', methods=['POST'])
def add_user():
    # Fetch form data
    userDetails = request.form
    name = userDetails.get('name')
    password = userDetails.get('password')

    # Check if all data is supplied
    if name is None:
        return jsonify({"error": "Username not specified"}), 400
    if password is None:
        return jsonify({"error": "Password not specified"}), 400
    
    # TODO: Check for duplicate username
    # TODO: password validation
    # TODO: password hashing
    userid = database.addUser(name, password)
    return jsonify({"id": userid}), 201

@app.route('/user/<string:id>', methods=['GET'])
def get_user(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    data = database.getUserByID(id)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@app.route('/user/<string:id>/projects', methods=['GET'])
def get_user_projects(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Check if user actually exists
    user = database.getUserByID(id)
    if user is None:
        return jsonify({"error": "Specified user does not exist"})

    data = database.getUserProjects(id)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@app.route('/user/<string:id>/posts', methods=['GET'])
def get_user_posts(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Check if user actually exists
    user = database.getUserByID(id)
    if user is None:
        return jsonify({"error": "Specified user does not exist"})

    data = database.getUserPosts(id)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@app.route('/user/<string:id>/comments', methods=['GET'])
def get_user_comments(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Check if user actually exists
    user = database.getUserByID(id)
    if user is None:
        return jsonify({"error": "Specified user does not exist"})

    data = database.getUserComments(id)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@app.route('/user', methods=['GET'])
def get_user_name():
    name = request.args.get('name')
    limit = request.args.get('limit')
    offset = request.args.get('offset')

    if limit is not None and not isInt(limit):
        return jsonify({"error": "limit is not an integer"}), 400
    if offset is not None and not isInt(offset):
        return jsonify({"error": "offset is not an integer"}), 400
    
    data = database.getUser(name, limit, offset)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@app.route('/user/<string:id>', methods=['PUT'])
def put_user(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400
    # Fetch form data
    userDetails = request.form
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

    # TODO: Check for duplicate username
    # TODO: password validation
    # TODO: password hashing
    data = database.updateUser(id, name, password)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404
    
@app.route('/user/<string:id>', methods=['DELETE'])
def del_user(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400
    
    # Check if user actually exists
    user = database.getUserByID(id)
    if user is None:
        return jsonify({"error": "Specified user does not exist"})
    
    # Delete user
    if database.deleteUser(id):
        return jsonify({"Info": "User deleted successfully"}), 200
    else:
        return jsonify({"erorr": "Something went wrong deleting user"}), 500



# Projects
@app.route('/project', methods=['POST'])
def add_project():
    # Fetch form data
    projectDetails = request.form
    name = projectDetails.get('name')
    description = projectDetails.get('description')
    visibility = projectDetails.get('visibility')
    owner = projectDetails.get('ownerID')

    # Check if all data is supplied correctly
    if name is None:
        return jsonify({"error": "Project name not specified"}), 400
    if description is None:
        return jsonify({"error": "Project description not specified"}), 400
    if visibility is None:
        return jsonify({"error": "Project visibility not specified"}), 400
    if visibility not in allowed_project_visibilities:
            return jsonify({"error": "Project visibility not a legal value"}), 400
    if owner is None:
        return jsonify({"error": "Project owner not specified"}), 400
    if not isInt(owner):
        return jsonify({"error": "ownerID should be string"})
    
    # Add project to the database
    projectid = database.addProject(name, description, visibility, owner)
    return jsonify({"id": projectid}), 201

@app.route('/project/<string:id>/posts', methods=['POST'])
def add_post(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Fetch form data
    projectDetails = request.form
    title = projectDetails.get('title')
    content = projectDetails.get('content')
    owner = projectDetails.get('userID')

    # Check if all data is supplied
    if title is None:
        return jsonify({"error": "Post title not specified"}), 400
    if content is None:
        return jsonify({"error": "Post content not specified"}), 400
    if owner is None:
        return jsonify({"error": "Project owner not specified"}), 400
    if not isInt(owner):
        return jsonify({"error": "ownerID should be string"})
    
    # Check if project actually exists
    project = database.getProjectByID(id)
    if project is None:
        return jsonify({"error": "Specified project does not exist"})

    # Add post to the database
    postid = database.addProjectPost(title, content, owner, id)
    return jsonify({"id": postid}), 201

@app.route('/project/<string:id>/users', methods=['POST'])
def add_project_user(id):
    # Fetch form data
    projectDetails = request.form
    user = projectDetails.get('user')
    role = projectDetails.get('role')

    # Check if all data is supplied
    if user is None:
        return jsonify({"error": "Project user not specified"}), 400
    if role is None:
        return jsonify({"error": "Project user role not specified"}), 400
    if role not in allowed_projectUser_states:
        return jsonify({"error": "Project user role not a legal value"}), 400

    # Check if project actually exists
    project = database.getProjectByID(id)
    if project is None:
        return jsonify({"error": "Specified project does not exist"})

    projectUserID = database.addProjectUser(user, id, role)
    return jsonify({"id": projectUserID}), 201

@app.route('/project', methods=['GET'])
def get_project():
    name = request.args.get('name')
    limit = request.args.get('limit')
    offset = request.args.get('offset')

    if limit is not None and not isInt(limit):
        return jsonify({"error": "limit is not an integer"}), 400
    if offset is not None and not isInt(offset):
        return jsonify({"error": "offset is not an integer"}), 400
    
    data = database.getProjects(name, limit, offset)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@app.route('/project/<string:id>', methods=['GET'])
def get_project_id(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    data = database.getProjectByID(id)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@app.route('/project/<string:id>/users', methods=['GET'])
def get_project_users(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Check if project actually exists
    project = database.getProjectByID(id)
    if project is None:
        return jsonify({"error": "Specified project does not exist"})
        
    data = database.getProjectUsers(id)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@app.route('/project/<string:id>/posts', methods=['GET'])
def get_project_post(id):
    limit = request.args.get('limit')
    offset = request.args.get('offset')

    if limit is not None and not isInt(limit):
        return jsonify({"error": "limit is not an integer"}), 400
    if offset is not None and not isInt(offset):
        return jsonify({"error": "offset is not an integer"}), 400

    data = database.getProjectPosts(id, limit, offset)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@app.route('/project/<string:id>', methods=['PUT'])
def put_project(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Fetch form data
    projectDetails = request.form
    title = projectDetails.get('title')
    content = projectDetails.get('content')
    visibility = projectDetails.get('visibility')

    # Check if all data is supplied
    if title is None:
        return jsonify({"error": "Project title not specified"}), 400
    if content is None:
        return jsonify({"error": "Project content not specified"}), 400
    if visibility is None:
        return jsonify({"error": "Project visibility not specified"}), 400
    if visibility not in allowed_project_visibilities:
        return jsonify({"error": "Project visibility not a legal value"}), 400

    # Check if project actually exists
    project = database.getProjectByID(id)
    if project is None:
        return jsonify({"error": "Specified project does not exist"})

    data = database.updateProject(id, title, content, visibility)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@app.route('/project/<string:id>/user', methods=['PUT'])
def put_project_user(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Fetch form data
    projectDetails = request.form
    user = projectDetails.get('user')
    role = projectDetails.get('role')

    # Check if all data is supplied
    if user is None:
        return jsonify({"error": "Projectuser id not specified"}), 400
    if role is None:
        return jsonify({"error": "Projectuser role not specified"}), 400
    if role not in allowed_projectUser_states:
        return jsonify({"error": "Projectuser role not a legal value"}), 400

    # Check if project actually exists
    project = database.getProjectByID(id)
    if project is None:
        return jsonify({"error": "Specified project does not exist"})

    data = database.updateProjectUser(id, user, role)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@app.route('/project/<string:id>', methods=['DELETE'])
def del_project(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400
    
    # Check if project actually exists
    project = database.getProjectByID(id)
    if project is None:
        return jsonify({"error": "Specified project does not exist"})
    
    # Delete project
    if database.deleteProject(id):
        return jsonify({"Info": "Project deleted successfully"}), 200
    else:
        return jsonify({"erorr": "Something went wrong deleting the project"}), 500

@app.route('/project/<string:id>/user', methods=['DELETE'])
def del_project_user(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Fetch form data
    projectDetails = request.form
    user = projectDetails.get('user')

    if user is None:
        return jsonify({"error": "Projectuser id not specified"}), 400

    # Check if project actually exists
    project = database.getProjectByID(id)
    if project is None:
        return jsonify({"error": "Specified project does not exist"})
    
    # Delete project user
    if database.deleteProjectUser(id, user):
        return jsonify({"Info": "Projectuser deleted successfully"}), 200
    else:
        return jsonify({"erorr": "Something went wrong deleting the projectuser"}), 500



# POSTS
@app.route('/post/<string:id>/comment', methods=['POST'])
def add_comment(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Fetch form data
    postDetails = request.form
    content = postDetails.get('content')
    parent = postDetails.get('parent')
    userID = postDetails.get('userID')

    if content is None:
        return jsonify({"error": "Comment content not specified"}), 400
    if parent is None:
        return jsonify({"error": "Comment parent id not specified"}), 400
    if userID is None:
        return jsonify({"error": "Comment user id not specified"}), 400

    # Add comment
    commentID = database.addPostComment(content, parent, userID)
    return jsonify({"id": commentID}), 201

@app.route('/post/<string:id>', methods=['GET'])
def get_post(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    data = database.getPostByID(id)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@app.route('/post/<string:id>/comments', methods=['GET'])
def get_post_comments(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400
    
    data = database.getPostComments(id)
    # TODO: return nested comments
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@app.route('/post/<string:id>', methods=['PUT'])
def put_post(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Fetch form data
    postDetails = request.form
    title = postDetails.get('title')
    content = postDetails.get('content')

    if content is None:
        return jsonify({"error": "Post content not specified"}), 400
    if title is None:
        return jsonify({"error": "Post title not specified"}), 400
    
    # Update post
    data = database.updatePost(id, title, content)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@app.route('/post/<string:id>', methods=['DELETE'])
def del_post(id): 
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Check if post actually exists
    post = database.getPostByID(id)
    if post is None:
        return jsonify({"error": "Specified post does not exist"})
    
    # Delete post
    data = database.deletePost(id)
    if data is not None:
        return jsonify({"Info": "Post deleted successfully"}), 200
    else:
        return jsonify({"error": "No results found"}), 404



# COMMENTS
@app.route('/comment/<string:id>', methods=['PUT'])
def put_comment(id):
    # Check if specified ID is an integer
    if not isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Fetch form data
    commentDetails = request.form
    content = commentDetails.get('content')

    if content is None:
        return jsonify({"error": "Comment content not specified"}), 400
    
    # Update comment
    data = database.updateComment(id, content)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404






if(__name__ == '__main__'):
    app.run(debug=True)