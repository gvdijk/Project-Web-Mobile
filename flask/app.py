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
    cur.close()
    # TODO return statement, picture
    return 200

@app.route('/user/<string:id>', methods=['GET'])
def get_user(id):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM user WHERE userID = " + id)
    if resultValue > 0:
        userDetails = cur.fetchall()
        return userDetails, 200

@app.route('/user/<string:id>/projects', methods=['GET'])
def get_user_projects(id):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT Project_projectID FROM projectuser WHERE User_userID = " + id)
    if resultValue > 0:
        userDetails = cur.fetchall()
        return userDetails, 200

@app.route('/user/<string:id>/posts', methods=['GET'])
def get_user_posts(id):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM post WHERE postUser = " + id)
    if resultValue > 0:
        userDetails = cur.fetchall()
        return userDetails, 200

@app.route('/user/<string:id>/comments', methods=['GET'])
def get_user_comments(id):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM comments WHERE commentUser = " + id)
    if resultValue > 0:
        userDetails = cur.fetchall()
        return userDetails, 200

@app.route('/user/<string:name>', methods=['GET'])
def get_user_name(name):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT userName FROM user WHERE userName LIKE %"+ name +"%")
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
    # TODO return statement
    return 200
    
@app.route('/user/<string:id>', methods=['DELETE'])
def del_user(id):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE user SET userDeleted = true WHERE userID = " + id)
    mysql.connection.commit()
    cur.close()
    # TODO return statement
    return 200




# Projects
@app.route('/project', methods=['POST'])
def add_project():
    # Fetch form data
    userDetails = request.form
    name = userDetails['name']
    description = userDetails['description']
    visibility = userDetails['visibility']
    owner = userDetails['userID']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO project(projectName, projectDescription, projectVisibility, projectOwner) VALUES(%s, %s, %s, %s)", (name, description, visibility, owner))
    mysql.connection.commit()
    cur.close()
    # TODO return statement, picture
    return 200







if(__name__ == '__main__'):
    app.run(debug=True)