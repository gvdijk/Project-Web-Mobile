from flask import Flask, render_template
from data import Posts

app = Flask(__name__)

posts = Posts()

@app.route('/')
def index():
    return render_template('home.html', posts = posts)

@app.route('/post/<string:id>')
def post(id):
    return render_template('post.html', id = id)

if(__name__ == '__main__'):
    #TODO disable debugmode
    app.run(debug=True)