import mysql.connector

connection = None
cur = None

def connect(user, password, host, database):
    global connection
    global cur
    connection = mysql.connector.connect(
                                    user=user, password=password,
                                    host=host,
                                    database=database)
    cur = connection.cursor(dictionary=True)

def close_connection():
    cur.close()
    connection.close()

# -----------------------------------------Login Related Functions--------------------------------------- #
def getUserByName(name):
    sql = "SELECT * FROM user WHERE userDeleted = 0 AND userName = %s"
    data = (name,)
    cur.execute(sql, data)
    results = cur.fetchone()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

# -----------------------------------------User Related Functions---------------------------------------- #
def getUserByID(id):
    sql = "SELECT * FROM user WHERE userDeleted = 0 AND userID = " + id
    cur.execute(sql)
    results = cur.fetchone()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def addUser(name, password):
    sql = "INSERT INTO user(userName, userPass) VALUES(%s, %s)"
    data = (name, password)
    cur.execute(sql, data)
    connection.commit()
    return cur.lastrowid

def getUserProjects(id):
    sql = "SELECT Project_projectID FROM projectuser WHERE projectuserDeleted = 0 AND User_userID = " + id
    cur.execute(sql)
    results = cur.fetchall()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def getUserPosts(id):
    sql = "SELECT * FROM post WHERE postDeleted = 0 AND postUser = " + id
    cur.execute(sql)
    results = cur.fetchall()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def getUserComments(id):
    sql = "SELECT * FROM comment WHERE commentDeleted = 0 AND commentUser = " + id
    cur.execute(sql)
    results = cur.fetchall()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def getUser(name, limit, offset):
    sql = "SELECT userID, userName, userPicture, userCreated FROM user "\
    "WHERE userDeleted = 0"
    data = ()
    if (name is not None):
        sql += " AND userName LIKE %s"
        data = data + ("%" + name + "%",)
    if limit is not None:
        sql += " ORDER BY userName LIMIT " + limit
        if offset is not None:
            sql += " OFFSET " + offset
    else:
        sql += " ORDER BY userName"
    cur.execute(sql, data)
    results = cur.fetchall()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def updateUser(id, name, password):
    sql = "UPDATE user SET userName = %s, userPass = %s WHERE userID = " + id
    data = (name, password)
    cur.execute(sql, data)
    connection.commit()
    return getUserByID(id)

def deleteUser(id):
    try:
        sql = "UPDATE user SET userDeleted = true WHERE userID = " + id
        cur.execute(sql)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

# ---------------------------------------Project Related Functions--------------------------------------- #
def addProject(name, description, visibility, owner):
    sql = "INSERT INTO project(projectName, projectDescription, projectVisibility, projectOwner) VALUES(%s, %s, %s, %s)"
    data = (name, description, visibility, owner)
    cur.execute(sql, data)
    connection.commit()
    return cur.lastrowid

def addProjectPost(title, content, owner, projectID):
    sql = "INSERT INTO post(postTitle, postContent, postUser, postProject) VALUES(%s, %s, %s, %s)"
    data = (title, content, owner, projectID)
    cur.execute(sql, data)
    connection.commit()
    return cur.lastrowid

def addProjectUser(userID, projectID, role):
    sql = "INSERT INTO projectuser(User_userID, Project_projectID, projectuserRole) VALUES(%s, %s, %s)"
    data = (userID, projectID, role)
    cur.execute(sql, data)
    connection.commit()
    return cur.lastrowid

def getProjects(name, limit, offset):
    sql = "SELECT * FROM project "\
    "WHERE projectDeleted = 0 AND (projectVisibility = 'PUBLIC' OR projectVisibility = 'RESTRICTED')"
    data = ()
    if (name is not None):
        sql += " AND projectName LIKE %s"
        data = data + ("%" + name + "%",)
    if limit is not None:
        sql += " ORDER BY projectName LIMIT " + limit
        if offset is not None:
            sql += " OFFSET " + offset
    else:
        sql += " ORDER BY projectName"
    cur.execute(sql, data)
    results = cur.fetchall()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results


def getProjectByID(id):
    sql = "SELECT * FROM project WHERE projectDeleted = 0 AND projectID = " + id
    cur.execute(sql)
    results = cur.fetchone()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def getProjectUsers(id):
    sql = "SELECT User_userID FROM projectuser WHERE projectuserDeleted = 0 AND Project_projectID = " + id
    cur.execute(sql)
    results = cur.fetchall()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def getProjectPosts(id, limit, offset):
    sql = "SELECT * FROM post WHERE postDeleted = 0 AND postProject = " + id
    if limit is not None:
        sql += " ORDER BY postCreated LIMIT " + limit
        if offset is not None:
            sql += " OFFSET " + offset
    else:
        sql += " ORDER BY postCreated"
    cur.execute(sql)
    results = cur.fetchall()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def updateProject(id, title, content, visibility):
    sql = "UPDATE project SET projectName = %s, projectDescription = %s, projectVisibility = %s WHERE projectID = " + id
    data = (title, content, visibility)
    cur.execute(sql, data)
    connection.commit()
    return getProjectByID(id)

def updateProjectUser(projectID, userID, role):
    sql = "UPDATE projectuser SET projectuserRole = %s WHERE User_userID = " + userID + " AND Project_projectID = " + projectID
    data = (role,)
    cur.execute(sql, data)
    connection.commit()
    cur.execute("SELECT * FROM projectuser WHERE projectuserDeleted = 0 AND Project_projectID = " + projectID + " AND User_userID = " + userID)
    return cur.fetchone()

def deleteProject(id):
    try:
        sql = "UPDATE project SET projectDeleted = true WHERE projectID = " + id
        cur.execute(sql)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

def deleteProjectUser(projectID, userID):
    try:
        sql = "UPDATE projectuser SET projectuserDeleted = true WHERE Project_projectID = " + projectID + " AND User_userID = " + userID
        cur.execute(sql)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

# -----------------------------------------Post Related Functions---------------------------------------- #
def addPostComment(content, parentID, userID):
    sql = "INSERT INTO comment(commentContent, commentUser, commentPost) VALUES(%s, " +  userID + ", " + parentID + ")"
    data = (content,)
    cur.execute(sql, data)
    connection.commit()
    return cur.lastrowid

def getPostByID(id):
    sql = "SELECT * FROM post WHERE postDeleted = 0 AND postID = " + id
    cur.execute(sql)
    results = cur.fetchone()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def getPostComments(id):
    sql = "SELECT * FROM comment WHERE commentDeleted = 0 AND commentPost = " + id
    cur.execute(sql)
    results = cur.fetchall()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def updatePost(id, title, content):
    sql = "UPDATE post SET postTitle = %s, postContent = %s WHERE postID = " + id
    data = (title, content)
    cur.execute(sql, data)
    connection.commit()
    return getPostByID(id)

def deletePost(id):
    try:
        sql = "UPDATE post SET postDeleted = true WHERE postID = " + id
        cur.execute(sql)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False

# ---------------------------------------Comment Related Functions--------------------------------------- #
def updateComment(id, content):
    sql = "UPDATE comment SET commentContent = %s WHERE commentID = " + id
    data = (content,)
    cur.execute(sql, data)
    connection.commit()
    cur.execute("SELECT * FROM comment WHERE commentDeleted = 0 AND commentID = " + id)
    return cur.fetchone()