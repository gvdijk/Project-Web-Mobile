from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import (jwt_required, get_jwt_identity)
import database
import function

comment_endpoints = Blueprint('comment_endpoints', __name__)

# COMMENTS
@comment_endpoints.route('/comment/<string:id>', methods=['PUT'])
@jwt_required
def put_comment(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Fetch form data
    commentDetails = request.get_json()
    content = commentDetails.get('content')

    if content is None:
        return jsonify({"error": "Comment content not specified"}), 400

    # Check if comment actually exists
    comment = database.getCommentByID(id)
    if comment is None:
        return jsonify({"error": "Specified comment does not exist"})

    # Check if the user trying to update the comment is the comment owner
    if comment['commentUser'] != get_jwt_identity():
        return jsonify({"error": "Only comment owner can update post"}), 400
    
    # Update comment
    data = database.updateComment(id, content)
    if data is not None:
        return jsonify(data), 200
    else:
        return jsonify({"error": "No results found"}), 404

@comment_endpoints.route('/comment/<string:id>', methods=['DELETE'])
@jwt_required
def delete_comment(id):
    # Check if specified ID is an integer
    if not function.isInt(id):
        return jsonify({"error": "id is not an integer"}), 400

    # Check if comment actually exists
    comment = database.getCommentByID(id)
    if comment is None:
        return jsonify({"error": "Specified comment does not exist"})

    # Check if the user trying to delete the post is the post owner
    post = database.getPostByID(comment['commentPost'])
    userRole = function.getProjectUserRole(get_jwt_identity(), post['postProject'])
    if not function.isProjectAdmin(userRole):
        if post['postUser'] != get_jwt_identity():
            return jsonify({"error": "Must be admin to delete comment of other user"}), 400
    
    # Delete comment
    commentDeleted = database.deleteComment(id)
    if commentDeleted is True:
        return jsonify({"Info": "Comment deleted successfully"}), 200
    else:
        return jsonify({"error": "Something went wrong deleting the comment"}), 500