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
    
    # Delete comment
    data = database.deleteComment(id)
    if data is not None:
        return jsonify({"Info": "Comment deleted successfully"}), 200
    else:
        return jsonify({"error": "No results found"}), 404