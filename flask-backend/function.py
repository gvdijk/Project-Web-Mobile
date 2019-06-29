import re
import os
import hashlib
import binascii
import database

# Helper function to check if a String represents an integer or not
def isInt(var):
    try:
        int(var)
        return True
    except ValueError as e:
        return False

# Hashes a password using HMAC-SHA512 for cryptographically secure storing
# Credit to https://www.vitoshacademy.com/hashing-passwords-in-python/ for the code implementation
def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

# Checks a hashed password against a provided password
# Credit to https://www.vitoshacademy.com/hashing-passwords-in-python/ for the code implementation
def verify_hashed_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

def check_username(name):
    # Check if name is at least 3 characters long
    if len(name) < 3:
        return "Name must be at least 3 characters long"
    # Check if name is no more than 45 characters long
    elif len(name) > 20:
        return "Name must be no more than 20 characters long"
    # Check if name only contains letters, numbers underscores or dashes
    elif not re.match("^[ A-Za-z0-9_-]*$", name):
        return "Name contains invalid characters"
    else:
        return "ok"

def check_password(password):
    # Check if password is at least 6 characters
    if len(password) < 6:
        return "Password must be at least 6 characters long"
    # Check if password contains a lowercase letter
    elif not re.search("[a-z]", password):
        return "Password must contain at least one lowercase letter"
    # Check if password contains an uppercase letter
    elif not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter"
    # Check if password contains a digit
    elif not re.search("[0-9]", password):
        return "Password must contain at least one digit"
    else:
        return "ok"

def nest_comments(comments):
    root = { 'top': { 'children': [] } }
    for comment in comments:
        parentID = comment['commentParent'] or 'top'
        root.setdefault(parentID, { 'children': [] })
        root.setdefault(comment['commentID'], { 'children': [] })
        root[comment['commentID']].update(comment)
        root[parentID]['children'].append(root[comment['commentID']])
    return root['top']['children']

# Check the role of a user in a project
def getProjectUserRole(userID, projectID):
    projectUser = database.getProjectUserByID(str(userID), str(projectID))
    if projectUser is None:
        return None
    else:
        return projectUser['projectuserRole']

def isProjectMember(userRole):
    return userRole in ['USER', 'ADMIN', 'OWNER']

def isProjectAdmin(userRole):
    return userRole in ['ADMIN', 'OWNER']

def isProjectOwner(userRole):
    return userRole == 'OWNER'
