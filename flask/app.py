from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'admin' # Super encripted and safe password usage 
app.config['MYSQL_DB'] = 'mydb'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        # id = userDetails['id']
        password = userDetails['password']
        picture = userDetails['picture']
        created = datetime.date.today()

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user(userName, userPass, userPicture ,userCreated) VALUES(%s, %s, %s, %s)", (name, password, picture, created))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM user")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

@app.route('/user/<string:id>')
def get_user(id):
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM user WHERE userID = " + id)
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if(__name__ == '__main__'):
    app.run(debug=True)