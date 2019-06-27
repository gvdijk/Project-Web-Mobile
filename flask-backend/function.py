import re
import os
import hashlib
import binascii
import database

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
    root = { 0: { 'children': [] } }
    for comment in comments:
        if comment['commentParent'] == None:
            comment['commentParent'] = 0
    for comment in comments:
        root.setdefault(comment['commentParent'], { 'children': [] })
        root.setdefault(comment['commentID'], { 'children': [] })
        root[comment['commentID']].update(comment)
        root[comment['commentParent']]['children'].append(root[comment['commentID']])
    return root[0]['children']
