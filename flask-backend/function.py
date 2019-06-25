import re

def check_username(name):
    sql = "SELECT userName FROM user"
    cur.execute(sql)
    results = cur.fetchall()
    if name in results:
        return jsonify({"error": "name not unique"}), 400
    elif len(name) < 3:
        return jsonify({"error": "name must be at least 3 characters long"}), 400
    else:
        return 200
    

def check_password(password):    
    x = True
    while x:  
        if (len(password)<6):
            break
        elif not re.search("[a-z]",password):
            break
        elif not re.search("[0-9]",password):
            break
        elif not re.search("[A-Z]",password):
            break
        elif re.search(" ",password):
            break
        else:
            x=False
            return jsonify({"info": "Valid Password"}), 200

    if x:
        return jsonify({"error": "Not a Valid Password"}), 400