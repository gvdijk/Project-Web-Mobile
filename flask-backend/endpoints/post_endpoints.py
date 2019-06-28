from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import (jwt_required, get_jwt_identity)
import database
import function

post_endpoints = Blueprint('post_endpoints', __name__)

# POSTS
@post_endpoints.route('/post/<string:id>/comments', methods=['POST'])
@jwt_required
def add_comment(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Fetch form data
    postDetails = request.get_json()
    content = postDetails.get('content')
    parent = postDetails.get('parent')
    userID = postDetails.get('userID')

    if content is None:
        return jsonify({"error": "Comment content not specified"}), 400
    if userID is None:
        return jsonify({"error": "Comment user id not specified"}), 400

    # Check if post actually exists
    post = database.getPostByID(id)
    if post is None:
        return jsonify({"error": "Specified post does not exist"}), 400

    # Check if parent actually exists
    if parent is not None:
        comment = database.getCommentByID(str(parent))
        if comment is None:
            return jsonify({"error": "Parent comment does not exist"}), 400

    # Add comment
    commentID = database.addPostComment(content, parent, userID, id)
    return jsonify({"id": commentID}), 201

@post_endpoints.route('/post/<string:id>', methods=['GET'])
def get_post(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    data = database.getPostByID(id)
    if data is None:
        return jsonify({"error": "No results found"}), 404
    else:
        user = database.getUserInfo(str(data['postUser']))
        data['user'] = user
        return jsonify(data), 200

@post_endpoints.route('/post/<string:id>/comments', methods=['GET'])
def get_post_comments(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400
    
    data = database.getPostComments(id)
    if data is None:
        return jsonify({"error": "No results found"}), 404
    else:
        for comment in data:
            user = database.getUserInfo(str(comment['commentUser']))
            comment['user'] = user
        data = function.nest_comments(data)
        return jsonify(data), 200

@post_endpoints.route('/post/<string:id>', methods=['PUT'])
@jwt_required
def put_post(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Fetch form data
    postDetails = request.get_json()
    content = postDetails.get('content')

    if content is None:
        return jsonify({"error": "Post content not specified"}), 400
    
    # Update post
    data = database.updatePost(id, content)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@post_endpoints.route('/post/<string:id>', methods=['DELETE'])
@jwt_required
def del_post(id): 
    # Check if specified ID is an integer
    if not function.isInt(id):
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