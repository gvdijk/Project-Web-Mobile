import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool

connectionPool = None

def init(user, password, host, database):
    global connectionPool
    dbconfig = {
        "host": host,
        "user": user,
        "password": password,
        "database": database
    }
    connectionPool = MySQLConnectionPool(pool_name='connection_pool',
                                        pool_size=10,
                                        pool_reset_session=True,
                                        **dbconfig)

def getConnection():
    return connectionPool.get_connection()

# -----------------------------------------Login Related Functions--------------------------------------- #
def getUserByName(name):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "SELECT * FROM user WHERE userDeleted = 0 AND userName = %s"
    data = (name,)
    cur.execute(sql, data)
    results = cur.fetchone()
    cur.close()
    connection.close()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

# -----------------------------------------User Related Functions---------------------------------------- #
def getUserByID(id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "SELECT userCreated, userID, userName, userPicture FROM user WHERE userDeleted = 0 AND userID = " + id
    cur.execute(sql)
    results = cur.fetchone()
    cur.close()
    connection.close()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def getUserInfo(id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "SELECT userCreated, userID, userName, userPicture FROM user WHERE userDeleted = 0 AND userID = " + id
    cur.execute(sql)
    results = cur.fetchone()
    cur.close()
    connection.close()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def addUser(name, password):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "INSERT INTO user(userName, userPass) VALUES(%s, %s)"
    data = (name, password)
    cur.execute(sql, data)
    connection.commit()
    lastID = cur.lastrowid
    cur.close()
    connection.close()
    return getUserByID(str(lastID))

def getUserProjects(id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "SELECT * FROM projectuser WHERE projectuserDeleted = 0 AND User_userID = " + id
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    connection.close()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def getUserPosts(id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "SELECT * FROM post WHERE postDeleted = 0 AND postUser = " + id
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    connection.close()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def getUserComments(id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "SELECT * FROM comment WHERE commentDeleted = 0 AND commentUser = " + id
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    connection.close()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def getUser(name, limit, offset):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
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
    cur.close()
    connection.close()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def updateUser(id, name, password):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "UPDATE user SET userName = %s, userPass = %s WHERE userID = " + id
    data = (name, password)
    cur.execute(sql, data)
    connection.commit()
    user = getUserByID(id)
    cur.close()
    connection.close()
    return user

def deleteUser(id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    try:
        sql = "UPDATE user SET userDeleted = true WHERE userID = " + id
        cur.execute(sql)
        connection.commit()
        cur.close()
        connection.close()
        return True
    except Exception as e:
        cur.close()
        connection.close()
        print(e)
        return False

# ---------------------------------------Project Related Functions--------------------------------------- #
def addProject(name, description, visibility, owner):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "INSERT INTO project(projectName, projectDescription, projectVisibility, projectOwner) VALUES(%s, %s, %s, %s)"
    data = (name, description, visibility, owner)
    cur.execute(sql, data)
    connection.commit()
    lastID = cur.lastrowid
    cur.close()
    connection.close()
    return getProjectByID(str(lastID))

def addProjectPost(title, content, owner, projectID):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "INSERT INTO post(postTitle, postContent, postUser, postProject) VALUES(%s, %s, %s, %s)"
    data = (title, content, owner, projectID)
    cur.execute(sql, data)
    connection.commit()
    lastID = cur.lastrowid
    cur.close()
    connection.close()
    return getPostByID(str(lastID))

def addProjectUser(userID, projectID, role):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "INSERT INTO projectuser(User_userID, Project_projectID, projectuserRole) VALUES(%s, %s, %s)"
    data = (userID, projectID, role)
    cur.execute(sql, data)
    connection.commit()
    lastID = cur.lastrowid
    cur.close()
    connection.close()
    return getProjectUserByID(str(lastID), str(projectID))

def getProjectsCount(name):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "SELECT count(*) as count FROM project "\
    "WHERE projectDeleted = 0 AND (projectVisibility = 'PUBLIC' OR projectVisibility = 'RESTRICTED')"
    data = ()
    if (name is not None):
        sql += " AND projectName LIKE %s"
        data = data + ("%" + name + "%",)
    sql += " ORDER BY projectName"
    cur.execute(sql, data)
    results = cur.fetchone()
    cur.close()
    connection.close()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def getProjects(name, limit, offset):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
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
        sql += " ORDER BY projectCreated"
    cur.execute(sql, data)
    results = cur.fetchall()
    cur.close()
    connection.close()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results


def getProjectByID(id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "SELECT * FROM project WHERE projectDeleted = 0 AND projectID = " + id
    cur.execute(sql)
    results = cur.fetchone()
    cur.close()
    connection.close()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def getProjectUsers(id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "SELECT * FROM projectuser WHERE projectuserDeleted = 0 AND Project_projectID = " + id
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    connection.close()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def getProjectUserByID(userID, projectID):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "SELECT * FROM projectuser WHERE projectuserDeleted = 0 AND Project_projectID = %s AND User_userID = %s"
    data = (projectID, userID)
    cur.execute(sql,data)
    results = cur.fetchone()
    cur.close()
    connection.close()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def getProjectPostsCount(id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "SELECT count(*) as count FROM post WHERE postDeleted = 0 AND postProject = " + id
    cur.execute(sql)
    results = cur.fetchone()
    cur.close()
    connection.close()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def getProjectPosts(id, limit, offset):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "SELECT * FROM post WHERE postDeleted = 0 AND postProject = " + id
    if limit is not None:
        sql += " ORDER BY postCreated LIMIT " + limit
        if offset is not None:
            sql += " OFFSET " + offset
    else:
        sql += " ORDER BY postCreated"
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    connection.close()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def updateProject(id, title, content, visibility):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "UPDATE project SET projectName = %s, projectDescription = %s, projectVisibility = %s WHERE projectID = " + id
    data = (title, content, visibility)
    cur.execute(sql, data)
    connection.commit()
    project = getProjectByID(id)
    cur.close()
    connection.close()
    return project

def updateProjectUser(projectID, userID, role):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "UPDATE projectuser SET projectuserRole = %s WHERE User_userID = %s AND Project_projectID = %s"
    data = (role,userID,projectID,)
    cur.execute(sql, data)
    connection.commit()
    sql = "SELECT * FROM projectuser WHERE projectuserDeleted = 0 AND Project_projectID = %s AND User_userID = %s"
    data = (projectID,userID,)
    cur.execute(sql, data)
    result = cur.fetchone()
    cur.close()
    connection.close()
    return result

def deleteProject(id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    try:
        sql = "UPDATE project SET projectDeleted = true WHERE projectID = " + id
        cur.execute(sql)
        connection.commit()
        cur.close()
        connection.close()
        return True
    except Exception as e:
        cur.close()
        connection.close()
        print(e)
        return False

def deleteProjectUser(projectID, userID):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    try:
        sql = "DELETE FROM projectuser WHERE Project_projectID = %s AND User_userID = %s"
        data = (projectID,userID)
        cur.execute(sql,data)
        connection.commit()
        cur.close()
        connection.close()
        return True
    except Exception as e:
        cur.close()
        connection.close()
        print(e)
        return False

# -----------------------------------------Post Related Functions---------------------------------------- #
def addPostComment(content, parentID, userID, id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "INSERT INTO comment(commentContent, commentUser, commentParent, commentPost) VALUES(%s, %s, %s, %s)"
    data = (content,userID,parentID,id)
    cur.execute(sql, data)
    connection.commit()
    lastID = cur.lastrowid
    cur.close()
    connection.close()
    return getCommentByID(str(lastID))

def getPostByID(id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "SELECT * FROM post WHERE postDeleted = 0 AND postID = " + id
    cur.execute(sql)
    results = cur.fetchone()
    cur.close()
    connection.close()

    if results is not None:
        project = getProjectByID(str(results['postProject']))
        if project is None:
            results = None

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def getPostComments(id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "SELECT * FROM comment WHERE commentDeleted = 0 AND commentPost = " + id
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    connection.close()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def updatePost(id, content):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "UPDATE post SET postContent = %s WHERE postID = " + id
    data = (content,)
    cur.execute(sql, data)
    connection.commit()
    result = getPostByID(id)
    cur.close()
    connection.close()
    return result

def deletePost(id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    try:
        sql = "UPDATE post SET postDeleted = true WHERE postID = " + id
        cur.execute(sql)
        connection.commit()
        cur.close()
        connection.close()
        return True
    except Exception as e:
        cur.close()
        connection.close()
        print(e)
        return False

def deltePostComments(id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    try:
        sql = "UPDATE comment SET commentDeleted = true WHERE commentPost = " + id
        cur.execute(sql)
        connection.commit()
        cur.close()
        connection.close()
        return True
    except Exception as e:
        cur.close()
        connection.close()
        print(e)
        return False

# ---------------------------------------Comment Related Functions--------------------------------------- #
def getCommentByID(id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "SELECT * FROM comment WHERE commentDeleted = 0 AND commentID = " + id
    cur.execute(sql)
    results = cur.fetchone()
    cur.close()
    connection.close()

    if (results is not None and len(results) == 0):
        return None
    else:
        return results

def updateComment(id, content):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    sql = "UPDATE comment SET commentContent = %s, commentEdited = current_timestamp() WHERE commentID = " + id
    data = (content,)
    cur.execute(sql, data)
    connection.commit()
    cur.execute("SELECT * FROM comment WHERE commentDeleted = 0 AND commentID = " + id)
    result = cur.fetchone()
    cur.close()
    connection.close()
    return result

def deleteComment(id):
    connection = getConnection()
    cur = connection.cursor(dictionary=True)
    try:
        sql = "UPDATE comment SET commentContent = 'Deze reactie is verwijderd', commentState = 'DELETED' WHERE commentID = " + id
        cur.execute(sql)
        connection.commit()
        cur.close()
        connection.close()
        return True
    except Exception as e:
        cur.close()
        connection.close()
        print(e)
        return False
