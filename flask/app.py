from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'admin' # Super encripted and safe password usage
app.config['MYSQL_DB'] = 'mydb'

#TODO fix cors access control 
# res.header("Access-Control-Allow-Origin", "http://localhost:8080");
# res.header("Access-Control-Allow-Headers", "Authorization, Origin, X-Requested-With, Content-Type, Accept");

mysql = MySQL(app)

# USERS
@app.route('/user', methods=['POST'])
def add_user():
    # Fetch form data
    userDetails = request.form
    name = userDetails['name']
    password = userDetails['password']
    picture = 'defaultPicture'

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user(userName, userPass, userPicture) VALUES(%s, %s, %s)", (name, password, picture))
    mysql.connection.commit()

    cur.execute("SELECT userID FROM user WHERE MAX(userID)")
    newUser = cur.fetchall()
    cur.close()
    # TODO picture
    return newUser, 200

@app.route('/user/<string:id>', methods=['GET'])
def get_user(id):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM user WHERE userDeleted = 0 AND userID = " + id)
    if resultValue > 0:
        userDetails = cur.fetchall()
        return userDetails, 200

@app.route('/user/<string:id>/projects', methods=['GET'])
def get_user_projects(id):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT Project_projectID FROM projectuser WHERE projectuserDeleted = 0 AND User_userID = " + id)
    if resultValue > 0:
        userDetails = cur.fetchall()
        return userDetails, 200

@app.route('/user/<string:id>/posts', methods=['GET'])
def get_user_posts(id):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM post WHERE postDeleted = 0 AND postUser = " + id)
    if resultValue > 0:
        userDetails = cur.fetchall()
        return userDetails, 200

@app.route('/user/<string:id>/comments', methods=['GET'])
def get_user_comments(id):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM comment WHERE commentDeleted = 0 AND commentUser = " + id)
    if resultValue > 0:
        userDetails = cur.fetchall()
        return userDetails, 200

@app.route('/user', methods=['GET'])
def get_user_name(name):
    name = request.args.get('name')
    limit = request.args.get('limit')
    offset = request.args.get('offset')

    cur = mysql.connection.cursor()

    if name == None:
        resultValue = cur.execute("SELECT userID, userName FROM user WHERE userDeleted = 0 ORDER BY userName LIMIT " + limit + " OFFSET " + offset)

    elif limit != None & offset != None:
        resultValue = cur.execute("SELECT userID, userName FROM user WHERE userDeleted = 0 AND userName LIKE %"+ name +"% ORDER BY userName LIMIT " + limit + " OFFSET " + offset)

    else:
        resultValue = cur.execute("SELECT userID, userName FROM user WHERE userDeleted = 0  AND userName LIKE %"+ name +"% ORDER BY userName")

    if resultValue > 0:
        userDetails = cur.fetchall()
        return userDetails, 200

@app.route('/user/<string:id>', methods=['PUT'])
def put_user(id):
    # Fetch form data
    userDetails = request.form
    name = userDetails['name']
    password = userDetails['password']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE user SET userName = %s, userPass = %s WHERE userID = " + id), (name, password)
    mysql.connection.commit()
    cur.close()
    return userDetails, 200
    
@app.route('/user/<string:id>', methods=['DELETE'])
def del_user(id):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE user SET userDeleted = true WHERE userID = " + id)
    mysql.connection.commit()
    cur.close()
    return id, 200




# Projects
@app.route('/project', methods=['POST'])
def add_project():
    # Fetch form data
    projectDetails = request.form
    name = projectDetails['name']
    description = projectDetails['description']
    visibility = projectDetails['visibility']
    owner = projectDetails['userID']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO project(projectName, projectDescription, projectVisibility, projectOwner) VALUES(%s, %s, %s, %s)", (name, description, visibility, owner))
    mysql.connection.commit()

    cur.execute("SELECT projectID FROM project WHERE MAX(projectID)")
    newProject = cur.fetchall()

    cur.close()
    return newProject, 200

@app.route('/project/<string:id>/post', methods=['POST'])
def add_post(id):
    # Fetch form data
    projectDetails = request.form
    title = projectDetails['title']
    content = projectDetails['content']
    owner = projectDetails['userID']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO post(postTitle, postContent, postUser, postProject) VALUES(%s, %s, %s, %s)", (title, content, owner, id))
    mysql.connection.commit()

    resultValue = cur.execute("SELECT postID FROM post WHERE MAX(postID)")
    newPost = cur.fetchall()

    cur.close()
    return newPost, 200

@app.route('/project/<string:id>/user', methods=['POST'])
def add_project_user(id):
    # Fetch form data
    projectDetails = request.form
    user = projectDetails['user']
    role = projectDetails['role']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO projectuser(User_userID, Project_projectID, projectuserRole) VALUES(%s, %s, %s)", (user, id, role))
    mysql.connection.commit()
    cur.close()
    # TODO return statement, picture
    return 200

@app.route('/project', methods=['GET'])
def get_project():
    name = request.args.get('name')
    limit = request.args.get('limit')
    offset = request.args.get('offset')

    cur = mysql.connection.cursor()

    if name == None:
        resultValue = cur.execute("SELECT projectID, projectName FROM project WHERE projectDeleted = 0 ORDER BY projectName LIMIT " + limit + " OFFSET " + offset)

    elif limit != None & offset != None:
        resultValue = cur.execute("SELECT projectID, projectName FROM project WHERE projectDeleted = 0 AND projectName LIKE %"+ name +"% ORDER BY projectName LIMIT " + limit + " OFFSET " + offset)

    else:
        resultValue = cur.execute("SELECT projectID, projectName FROM project WHERE projectDeleted = 0  AND projectName LIKE %"+ name +"% ORDER BY projectName")

    if resultValue > 0:
        projectDetails = cur.fetchall()
        # TODO json
        return projectDetails, 200

@app.route('/project/<string:id>', methods=['GET'])
def get_project_id(id):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM project WHERE projectDeleted = 0 AND projectID = " + id)
    if resultValue > 0:
        projectDetails = cur.fetchall()
        return projectDetails, 200

@app.route('/project/<string:id>/user', methods=['GET'])
def get_project_users(id):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT User_userID FROM projectuser WHERE projectuserDeleted = 0 AND Project_projectID = " + id)
    if resultValue > 0:
        projectDetails = cur.fetchall()
        return projectDetails, 200

@app.route('/project/<string:id>/post', methods=['GET'])
def get_project_post(id):
    limit = request.args.get('limit')
    offset = request.args.get('offset')

    cur = mysql.connection.cursor()

    if limit != None & offset != None:
        resultValue = cur.execute("SELECT * FROM post WHERE postDeleted = 0 AND postProject = " + id + " ORDER BY postCreated LIMIT " + limit + " OFFSET " + offset)

    else:
        resultValue = cur.execute("SELECT * FROM post WHERE postDeleted = 0 AND postProject = " + id)

    if resultValue > 0:
        projectDetails = cur.fetchall()
        return projectDetails, 200

@app.route('/project/<string:id>', methods=['PUT'])
def put_project(id):
    # Fetch form data
    projectDetails = request.form
    title = projectDetails['title']
    content = projectDetails['content']
    visibility = projectDetails['visibility']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE project SET postTitle = %s, postContent = %s, postVisibility WHERE postID = " + id), (title, content, visibility)
    mysql.connection.commit()
    cur.close()
    # TODO return statement
    return 200

@app.route('/project/<string:id>/user', methods=['PUT'])
def put_project_user(id):
    # Fetch form data
    projectDetails = request.form
    user = projectDetails['user']
    role = projectDetails['role']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE projectuser SET projectuserRole = %s WHERE User_userID = "+ user +" AND Project_projectID = "+ id), (role)
    mysql.connection.commit()
    cur.close()
    # TODO return statement
    return 200

@app.route('/project/<string:id>', methods=['DELETE'])
def del_project(id):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE project SET projectDeleted = true WHERE projectID = " + id)
    mysql.connection.commit()
    cur.close()
    # TODO return statement
    return 200

@app.route('/project/<string:id>/user', methods=['DELETE'])
def del_project_user(id):
    projectDetails = request.form
    user = projectDetails['user']
    
    cur = mysql.connection.cursor()
    cur.execute("UPDATE project SET projectDeleted = true WHERE projectID = " + id)
    mysql.connection.commit()
    cur.close()
    # TODO return statement
    return 200



# POSTS
@app.route('/post/<string:id>/comment', methods=['POST'])
def add_comment():
    # Fetch form data
    postDetails = request.form
    content = postDetails['content']
    parent = postDetails['parent']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO comment(commentContent, commentPost) VALUES(%s, %s)", (content, parent))
    mysql.connection.commit()

    cur.execute("SELECT commentID FROM comment WHERE MAX(commentID)")
    newComment = cur.fetchall()

    cur.close()
    return newComment, 200

@app.route('/post/<string:id>', methods=['GET'])
def get_post(id):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM post WHERE postDeleted = 0 AND postID = " + id)
    if resultValue > 0:
        postDetails = cur.fetchall()
        # TODO Nested json
        return postDetails, 200

@app.route('/post/<string:id>/comments', methods=['GET'])
def get_post_comments(id):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM comment WHERE commentDeleted = 0 AND commentPost = " + id)
    if resultValue > 0:
        postDetails = cur.fetchall()
        # TODO nested json
        return postDetails, 200

@app.route('/post/<string:id>', methods=['PUT'])
def put_post(id):
    # Fetch form data
    postDetails = request.form
    title = postDetails['title']
    content = postDetails['content']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE post SET postTitle = %s, postContent = %s WHERE postID = "+ id), (title, content)
    mysql.connection.commit()
    cur.close()
    return 200

@app.route('/post/<string:id>', methods=['DELETE'])
def del_post(id): 
    cur = mysql.connection.cursor()
    cur.execute("UPDATE post SET postDeleted = true WHERE postID = " + id)
    mysql.connection.commit()
    cur.close()
    return id, 200



# COMMENTS
@app.route('/comment/<string:id>', methods=['PUT'])
def put_comment(id):
    # Fetch form data
    commentDetails = request.form
    content = commentDetails['content']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE comment SET commentContent = %s WHERE commentID = "+ id), (content)
    mysql.connection.commit()
    cur.close()
    return 200






if(__name__ == '__main__'):
    app.run(debug=True)