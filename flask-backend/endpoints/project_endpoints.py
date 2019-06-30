from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import (jwt_required, get_jwt_identity)
import database
import function

# Tuples to help check for correct enumerator inserts in the database
allowed_project_visibilities = ("PUBLIC", "RESTRICTED", "PRIVATE")
allowed_post_states = ("VISIBLE", "ARCHIVED", "DELETED")
allowed_projectUser_states = ("OWNER", "USER", "ADMIN", "PENDING", "INVITED")

project_endpoints = Blueprint('project_endpoints', __name__)

# Projects
@project_endpoints.route('/project', methods=['POST'])
@jwt_required
def add_project():
    # Fetch form data
    projectDetails = request.get_json()
    name = projectDetails.get('name')
    description = projectDetails.get('description')
    visibility = projectDetails.get('visibility')
    owner = get_jwt_identity()

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
    if not function.isInt(owner):
        return jsonify({"error": "ownerID should be string"})

    # Add project to the database
    projectid = database.addProject(name, description, visibility, owner)
    # Add owner of project to projectusers
    userid = database.addProjectUser(owner, projectid, 'OWNER')
    return jsonify({"id": projectid}), 201

@project_endpoints.route('/project/<string:id>/posts', methods=['POST'])
@jwt_required
def add_post(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Fetch form data
    projectDetails = request.get_json()
    title = projectDetails.get('title')
    content = projectDetails.get('content')
    owner = get_jwt_identity()

    # Check if all data is supplied
    if title is None:
        return jsonify({"error": "Post title not specified"}), 400
    if content is None:
        return jsonify({"error": "Post content not specified"}), 400
    if owner is None:
        return jsonify({"error": "Project owner not specified"}), 400
    if not function.isInt(owner):
        return jsonify({"error": "ownerID should be string"})
    
    # Check if project actually exists
    project = database.getProjectByID(id)
    if project is None:
        return jsonify({"error": "Specified project does not exist"})

    # Check if you have permission to post on this project
    userRole = function.getProjectUserRole(get_jwt_identity(), id)
    if not function.isProjectMember(userRole):
        return jsonify({"error": "Must be a project member to add post"}), 403

    # Add post to the database
    postid = database.addProjectPost(title, content, owner, id)
    return jsonify({"id": postid}), 201

@project_endpoints.route('/project/<string:id>/users', methods=['POST'])
@jwt_required
def add_project_user(id):
    # Fetch form data
    projectDetails = request.get_json()
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

    # Check if you have permission to add a user to this project
    projectVisibility = project['projectVisibility']
    userRole = function.getProjectUserRole(get_jwt_identity(), id)
    if userRole is None:
        if projectVisibility == 'PUBLIC':
            if role not in ['INVITED', 'USER']:
                return jsonify({"error": "May only invite or add user on public project"})
        elif projectVisibility == 'RESTRICTED':
            if role == 'INVITED':
                if not function.isProjectAdmin(userRole):
                    return jsonify({"error": "Only admins can invite users on restricted projects"})
            elif role == 'PENDING':
                if user != get_jwt_identity():
                    return jsonify({"error": "Only a user can request membership for himself"})
            else:
                return jsonify({"error": "May only invite or request user on restricted project"})
        elif projectVisibility == 'PRIVATE':
            if role == 'INVITED':
                if not function.isProjectAdmin(userRole):
                    return jsonify({"error": "Only admins can invite users on private projects"})
            else:
                return jsonify({"error": "You may only invite users for private projects"})
    else:
        return jsonify({"error": "User already has a project role"})

    projectUserID = database.addProjectUser(user, id, role)
    return jsonify({"id": projectUserID}), 201

@project_endpoints.route('/project', methods=['GET'])
def get_project():
    name = request.args.get('name')
    limit = request.args.get('limit')
    offset = request.args.get('offset')

    if limit is not None and not function.isInt(limit):
        return jsonify({"error": "limit is not an integer"}), 400
    if offset is not None and not function.isInt(offset):
        return jsonify({"error": "offset is not an integer"}), 400

    dataCount = database.getProjectsCount(name)
    data = database.getProjects(name, limit, offset)
    if data is None:
        return jsonify({"error": "No results found"}), 404
    else:
        for project in data:
            user = database.getUserInfo(str(project['projectOwner']))
            project['owner'] = user
        dataCount['data'] = data
        return jsonify(dataCount), 200

@project_endpoints.route('/project/<string:id>', methods=['GET'])
@jwt_required
def get_project_id(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    data = database.getProjectByID(id)
    if data is None:
        return jsonify({"error": "No results found"}), 404
    else:
        if(data['projectVisibility'] == 'PRIVATE'):
            userRole = function.getProjectUserRole(get_jwt_identity(), id)
            if not function.isProjectMember(userRole):
                return jsonify({"error": "Must be project member to view project"}), 403
        user = database.getUserInfo(str(data['projectOwner']))
        data['owner'] = user
        return jsonify(data), 200

@project_endpoints.route('/project/<string:id>/users', methods=['GET'])
@jwt_required
def get_project_users(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Check if project actually exists
    project = database.getProjectByID(id)
    if project is None:
        return jsonify({"error": "Specified project does not exist"})
        
    data = database.getProjectUsers(id)
    if data is None:
        return jsonify({"error": "No results found"}), 404
    else:
        for projectuser in data:
            user = database.getUserInfo(str(projectuser['User_userID']))
            projectuser['user'] = user
        return jsonify(data), 200

@project_endpoints.route('/project/<string:id>/posts', methods=['GET'])
@jwt_required
def get_project_post(id):
    limit = request.args.get('limit')
    offset = request.args.get('offset')

    if limit is not None and not function.isInt(limit):
        return jsonify({"error": "limit is not an integer"}), 400
    if offset is not None and not function.isInt(offset):
        return jsonify({"error": "offset is not an integer"}), 400

    dataCount = database.getProjectPostsCount(id)
    data = database.getProjectPosts(id, limit, offset)
    if data is None:
        return jsonify({"error": "No results found"}), 404
    else:
        project = database.getProjectByID(id)
        if(project['projectVisibility'] == 'PRIVATE'):
            userRole = function.getProjectUserRole(get_jwt_identity(), id)
            if not function.isProjectMember(userRole):
                return jsonify({"error": "Must be project member to view project posts"}), 403
        for projectpost in data:
            user = database.getUserInfo(str(projectpost['postUser']))
            projectpost['user'] = user
        dataCount['data'] = data
        return jsonify(dataCount), 200

@project_endpoints.route('/project/<string:id>', methods=['PUT'])
@jwt_required
def put_project(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Fetch form data
    projectDetails = request.get_json()
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

    # Check if you have permission to update the project
    userRole = function.getProjectUserRole(get_jwt_identity(), id)
    if not function.isProjectAdmin(userRole):
        return jsonify({"error": "Must be a project admin to update the project"}), 403

    data = database.updateProject(id, title, content, visibility)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@project_endpoints.route('/project/<string:id>/users', methods=['PUT'])
@jwt_required
def put_project_user(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Fetch form data
    projectDetails = request.get_json()
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

    # Check that you are not trying to change project owner
    if role == 'OWNER':
        return jsonify({"error": "Cannot set or tranfer project ownership"}), 403
    # Retrieve projectrole of user
    userRole = function.getProjectUserRole(get_jwt_identity(), id)
    # If user issuing the request is not changing his own data, check if user is admin
    if not (get_jwt_identity() == user):
        if not function.isProjectAdmin(userRole):
            return jsonify({"error": "Must be a project admin to update user roles"}), 403
    # If user issuing the request is changing own data, he can only change himself from invited to user
    elif userRole == 'PENDING':
        if role != 'USER':
            return jsonify({"error": "May only change your own role from pending to user"}), 403
    else:
        return jsonify({"error": "May only change your own role from pending to user"}), 403

    data = database.updateProjectUser(id, user, role)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@project_endpoints.route('/project/<string:id>', methods=['DELETE'])
@jwt_required
def del_project(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400
    
    # Check if project actually exists
    project = database.getProjectByID(id)
    if project is None:
        return jsonify({"error": "Specified project does not exist"})
    
    # Check if you are the owner of the project you are trying to delete
    userRole = function.getProjectUserRole(get_jwt_identity(), id)
    if not function.isProjectOwner(userRole):
        return jsonify({"error": "Must be project owner to delete a project"}), 403

    # Delete project
    if database.deleteProject(id):
        return jsonify({"Info": "Project deleted successfully"}), 200
    else:
        return jsonify({"erorr": "Something went wrong deleting the project"}), 500

@project_endpoints.route('/project/<string:id>/users', methods=['DELETE'])
@jwt_required
def del_project_user(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Fetch form data
    projectDetails = request.get_json()
    user = projectDetails.get('user')

    if user is None:
        return jsonify({"error": "Projectuser id not specified"}), 400

    # Check if project actually exists
    project = database.getProjectByID(id)
    if project is None:
        return jsonify({"error": "Specified project does not exist"})

    # Retrieve projectrole of user
    userRole = function.getProjectUserRole(get_jwt_identity(), id)
    # Retrieve projectrole of target
    targetRole = function.getProjectUserRole(user, id)

    # Check if both users are part of the same project
    if userRole is None:
        return jsonify({"error": "Must be a project member to delete users"}), 403
    elif targetRole is None:
        return jsonify({"error": "Target user is not a member of specified project"}), 403

    # User is trying to delete somebody else
    if not (get_jwt_identity() == user):
        if userRole not in ['ADMIN', 'OWNER']:
            return jsonify({"error": "Cannot delete project users without ADMIN or OWNER status"}), 403
        elif targetRole == 'OWNER':
            return jsonify({"error": "Cannot delete the owner of a project"}), 403
        elif targetRole == 'ADMIN':
            if userRole != 'OWNER':
                return jsonify({"error": "Cannot delete a project admin without OWNER permission"}), 403
    # User is trying to deleting himself, check that he is not the owner of the project
    else:
        if userRole == 'OWNER':
            return jsonify({"error": "Cannot delete yourself from your own project"}), 403
    
    # Delete project user
    if database.deleteProjectUser(id, user):
        return jsonify({"Info": "Projectuser deleted successfully"}), 200
    else:
        return jsonify({"erorr": "Something went wrong deleting the projectuser"}), 500
